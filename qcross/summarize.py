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

    query = f"{query}"
    issues = g.search_issues(query, repo=repository_name, sort="created", order="desc")

    return list(issues.get_page(0))


def get_exception_data():
    df_data = []
    jsonpath_expr = parse("$..exception")
    for filename in os.listdir("qcross-data/completed-execs"):
        try:
            with open(
                os.path.join(
                    "qcross-data/completed-execs", filename, "exec-metadata.json"
                ),
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

    groups = group_strings_by_similarity({sanitize_string(el) for el in df[column]}, 70)
    return groups


def summarize_groups():
    df = get_exception_data()

    exceptions = {
        "qasm3_exceptions": {
            "groups": get_groups_for(df, "qiskit.qasm3_roundtrip.exception"),
            "repo": ["Qiskit/qiskit-terra", "Qiskit/qiskit-qasm3-import"],
        },
        "qpy_exceptions": {
            "groups": get_groups_for(df, "qiskit.qpy_roundtrip.exception"),
            "repo": ["Qiskit/qiskit-terra"],
        },
        "qiskit_followup_exceptions": {
            "groups": get_groups_for(
                df,
                "qiskit.qiskit_followup.exception",
                # ["qiskit.qiskit_source.exception"],
            ),
            "repo": ["Qiskit/qiskit-terra"],
        },
    }

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


if __name__ == "__main__":
    summarize_groups()
