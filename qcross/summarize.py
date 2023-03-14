import json
import os
import re
from dotenv import load_dotenv

import pandas as pd
from fuzzywuzzy import fuzz
from github import Github
from termcolor import colored
from jsonpath_ng import parse

from qcross.utils import Log
import numpy as np

load_dotenv()  # take environment variables from .env.


def sanitize_string(string):
    # remove some strings between brackets of different types
    string = re.sub(r"\[.*\]", "", string)
    string = re.sub(r"\(.*\)", "", string)
    string = re.sub(r"{.*}", "", string)
    string = re.sub(r"<.*>", "", string)
    # remove numbers
    string = re.sub(r"\d+", "", string)
    # remove special characters
    string = re.sub(r"[^a-zA-Z0-9]", " ", string)

    # remove extra spaces
    string = re.sub(r"\s+", " ", string)
    return string.strip()


def group_strings_by_similarity(strings, threshold=80):
    groups = []
    for string in strings:
        found_group = False
        for group in groups:
            for other_string in group:
                similarity = fuzz.partial_token_sort_ratio(string, other_string)
                if similarity >= threshold:
                    group.append(string)
                    found_group = True
                    break
            if found_group:
                break
        if not found_group:
            groups.append([string])
    return groups


def search_github_issues(repository_name, query):
    # Authenticate with GitHub using an access token
    token = os.environ.get("GITHUB_ACCESS_TOKEN")
    g = Github(token, per_page=5)

    query = f"{query} is:issue"
    issues = g.search_issues(query, repo=repository_name, sort="created", order="desc")

    return list(issues.get_page(0))


def get_exception_data(folder="qcross-data/completed-execs"):
    df_data = []
    jsonpath_expr = parse("$..exception")
    for filename in os.listdir(folder):
        try:
            with open(
                os.path.join(folder, filename, "exec-metadata.json"),
                encoding="utf-8",
            ) as f:
                data = json.load(f)
                exceptions = {
                    str(match.full_path): match.value
                    for match in jsonpath_expr.find(data)
                    if match.value is not None
                }
                df_data.append(
                    {
                        "prog_id": data["prog_id"],
                        **exceptions,
                    }
                )
        except IOError:
            continue
    return pd.DataFrame(df_data)


def get_groups_for(df, column, excluded_columns=None):
    df = df.loc[:, df.columns != "prog_id"]

    df = df[~df[column].isna()]

    if excluded_columns is None:
        excluded_columns = [col for col in df.columns if col != column]
    else:
        excluded_columns = [
            col for col in df.columns if col != column and col not in excluded_columns
        ]

    def _filter(row, test_col, cols):
        for col in cols:
            if pd.isna(row[col]) or pd.isna(row[test_col]):
                continue
            if fuzz.partial_token_sort_ratio(row[test_col], row[col]) > 70:
                return False
        return True

    df = df[
        df.apply(
            lambda row: _filter(row, column, excluded_columns),
            axis=1,
        )
    ]

    if df.empty:
        return []

    groups = group_strings_by_similarity({sanitize_string(el) for el in df[column]}, 70)
    return groups


def summarize_groups():
    df = get_exception_data()

    all_columns_dict = {
        "qiskit": [
            "qiskit.qiskit_source.exception",
            "qiskit.qiskit_followup.exception",
            "qiskit.qasm3_roundtrip.exception",
            "qiskit.qpy_roundtrip.exception",
        ],
        "cirq": [
            "cirq.cirq_source.exception",
            "cirq.cirq_followup.exception",
            "cirq.cirq_qasm_qiskit.exception",
        ],
        "pyquil": [
            "pyquil.pyquil_source.exception",
            "pyquil.pyquil_followup.exception",
        ],
    }

    # flatten a list of lists

    all_columns = [name for l in all_columns_dict.values() for name in l]
    for column in all_columns:
        if column not in df.columns:
            # add a column with all NaNs
            df[column] = np.nan

    qiskit_columns = df[all_columns_dict["qiskit"] + ["prog_id"]]

    cirq_columns = df[all_columns_dict["cirq"] + ["prog_id"]]

    exceptions = {
        "qiskit.qiskit_source.exception": {
            "groups": get_groups_for(
                qiskit_columns,
                "qiskit.qiskit_source.exception",
                excluded_columns=[
                    "qiskit.qiskit_followup.exception",
                    "qiskit.qasm3_roundtrip.exception",
                    "qiskit.qpy_roundtrip.exception",
                ],
            ),
            "repo": ["Qiskit/qiskit-terra"],
        },
        "qiskit.qiskit_followup.exception": {
            "groups": get_groups_for(
                qiskit_columns,
                "qiskit.qiskit_followup.exception",
                excluded_columns=[
                    "qiskit.qasm3_roundtrip.exception",
                    "qiskit.qpy_roundtrip.exception",
                ],
            ),
            "repo": ["Qiskit/qiskit-terra"],
        },
        "qiskit.qasm3_roundtrip.exception": {
            "groups": get_groups_for(
                qiskit_columns,
                "qiskit.qasm3_roundtrip.exception",
                excluded_columns=["qiskit.qpy_roundtrip.exception"],
            ),
            "repo": ["Qiskit/qiskit-terra", "Qiskit/qiskit-qasm3-import"],
        },
        "qiskit.qpy_roundtrip.exception": {
            "groups": get_groups_for(qiskit_columns, "qiskit.qpy_roundtrip.exception"),
            "repo": ["Qiskit/qiskit-terra"],
        },
        "pyquil.pyquil_source.exception": {
            "groups": get_groups_for(
                df,
                "pyquil.pyquil_source.exception",
                excluded_columns=["pyquil.pyquil_followup.exception"],
            ),
            "repo": ["rigetti/pyquil"],
        },
        "pyquil.pyquil_followup.exception": {
            "groups": get_groups_for(df, "pyquil.pyquil_followup.exception"),
            "repo": ["rigetti/pyquil"],
        },
        "cirq.cirq_source.exception": {
            "groups": get_groups_for(
                cirq_columns,
                "cirq.cirq_source.exception",
                excluded_columns=["cirq.cirq_followup.exception"],
            ),
            "repo": ["quantumlib/Cirq"],
        },
        "cirq.cirq_followup.exception": {
            "groups": get_groups_for(
                cirq_columns,
                "cirq.cirq_followup.exception",
                excluded_columns=["cirq.cirq_qasm_qiskit.exception"],
            ),
            "repo": ["quantumlib/Cirq"],
        },
        "cirq.cirq_qasm_qiskit.exception": {
            "groups": get_groups_for(
                cirq_columns,
                "cirq.cirq_qasm_qiskit.exception",
            ),
            "repo": ["quantumlib/Cirq"],
        },
    }

    return exceptions

    def _get_issues_for_group(group):
        for exception in group:
            for repo in data["repo"]:
                print(f"Searching for '{colored(exception, color='red')}' in {repo}")
                issues = search_github_issues(repo, exception)
                if len(issues) > 0:
                    Log.yellow(f"Found {len(issues)} issues for {exception}")
                    for issue in issues:
                        print(
                            f" > \"{colored(issue.title, color='yellow')}\" ({issue.number})"
                        )
                else:
                    Log.green(f"No issues found for {exception}")
            print()

    for exception_category, data in exceptions.items():
        Log.blue(f"Searching for '{exception_category}'")
        for exception_group in data["groups"]:
            _get_issues_for_group(exception_group)
    return exceptions


def get_prog_ids_with_error(err: str):
    pass


if __name__ == "__main__":
    summarize_groups()
