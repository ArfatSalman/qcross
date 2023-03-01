import os
import traceback
from os.path import join, exists
from pathlib import Path
import json
from termcolor import colored
import numpy as np

from qcross.utils import (
    execute_single_py_program,
    fix_cx3,
    get_file_data,
    red,
    green,
    blue,
    yellow,
)

import sqlite3 as sl


def get_database_connection(db_filename: str = "done.db"):
    """Get the database."""
    DB_PATH = os.path.join("data", db_filename)
    con = sl.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS completed(name TEXT NOT NULL)")
    return con


def is_completed(program):
    con = get_database_connection()
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM completed WHERE name = "{program}"')
    return res.fetchone() is not None


def add_to_db(program):
    con = get_database_connection()
    cur = con.cursor()
    res = cur.execute(f"INSERT INTO completed VALUES ('{program}')")
    con.commit()


np.seterr(divide="ignore")
np.seterr(invalid="ignore")


def replace_qasm_2_with_3(qiskit_src):
    qasm_2_str = "qc = QuantumCircuit.from_qasm_str(qc.qasm())"

    if qasm_2_str in qiskit_src:
        qasm3_roundtrip_str = """
from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))
"""
        return qiskit_src.replace(qasm_2_str, qasm3_roundtrip_str)

    multi_qasm_1 = "qc_1 = QuantumCircuit.from_qasm_str(qc_1.qasm())"
    multi_qasm_2 = "qc_2 = QuantumCircuit.from_qasm_str(qc_2.qasm())"
    if multi_qasm_1 in qiskit_src and multi_qasm_1 in qiskit_src:
        qasm3_roundtrip_str = """
from qiskit.qasm3 import loads, dumps
qc_1 = loads(dumps(qc_1))
"""
        qc_2 = """
qc_2 = loads(dumps(qc_2))
"""
        return qiskit_src.replace(multi_qasm_1, qasm3_roundtrip_str).replace(
            multi_qasm_2, qc_2
        )

    raise ValueError("MR relation has QASM rountrip but no QASM calls found")


def get_metadata_from_file(metadata_path):
    with open(metadata_path, encoding="utf-8") as f:
        data = json.loads(f.read())
        return data


def execute(src, followup_path, metadata_path):
    metadata = {}
    data = get_metadata_from_file(metadata_path)
    relations = data["followup"]["metamorphic_transformations"]

    if "ToQasmAndBack" not in relations:
        return

    metadata["metamorphic_transformations"] = relations
    yellow("Found QASM Roundtrip MR. Converting to QASM 3:")
    qiskit_src = fix_cx3(get_file_data(followup_path))
    try:
        instrumented = replace_qasm_2_with_3(qiskit_src)
        green("Running modified Qiskit followup")
        res, _ = execute_single_py_program(instrumented)

        metadata["res"] = res
    except Exception as error:
        red(error)
        metadata["exception"] = str(error)

    return instrumented, metadata


def get_paths(folder, file):
    src = join(folder, "source", file)
    followup = join(folder, "followup", file)
    prog_id = file.split(".")[0]
    metadata = join(folder, "metadata", prog_id + ".json")

    return src, followup, metadata


def write_file(path, content, as_json=False):
    with open(path, "w", encoding="utf-8") as f:
        if as_json:
            f.write(json.dumps(content, indent=4))
        else:
            f.write(content)


if __name__ == "__main__":
    COMPLETED_EXEC_FOLDER = "data/completed-execs/"
    Path(COMPLETED_EXEC_FOLDER).mkdir(parents=True, exist_ok=True)

    folder = "data/qmt_v53/programs"
    paths = os.listdir(join(folder, "source"))

    skip = [
        "ae3bbf48e2c44b47b7dacd5ce3f1ea86.py",  # 55
        "e72010e17db0408fa9c544b869c64ac2.py",  # 53
        "f438624aef78412285662ea8b54da3fe.py",  # 53
        "37832dae28054a1580a0e3944f1fe0ca.py",  # 53
        "f438624aef78412285662ea8b54da3fe.py",
        "d839de0808ce46a5a7e53dd26377ed87.py",
        "735021e569654163a70ff97b7cc19904.py",
        "fd593735bf8d4714bb78de4f42f5bcd7.py",
        "617853584b7d4fdfbb71bf72de8aaab4.py",
        "f7adbdb5856f480fb510da14042e62ce.py",
        "d0e293d8045145f8bcb9bdffdd150863.py",
        "47d54f19b0ae4ab3a9906a22a473cc61.py",
        "b9aff279662446df9d89e6b0338538bb.py",
        "341aa727bf924bdfa578c6247b781c66.py",
    ]

    count = 0
    for p in paths:
        if p in skip:
            continue

        prog_id = p.split(".", maxsplit=1)[0]
        save_path = join(COMPLETED_EXEC_FOLDER, prog_id, "qiskit")

        if is_completed(p):
            continue

        if exists(join(save_path, prog_id + ".json")):
            continue

        src, followup, metadata_path = get_paths(folder, p)

        add_to_db(p)

        if not exists(metadata_path):
            blue(f"Metadata file {metadata_path} does not exist")
            continue
        if not exists(followup):
            blue(f"Followup file {followup} does not exist")
            continue

        yellow(f"{count}: Opening {p}")
        res = execute(src, followup, metadata_path)
        if res is None:
            # not a file with qasm conversion
            continue
        Path(save_path).mkdir(parents=True, exist_ok=True)
        code, metadata = res
        write_file(join(save_path, prog_id + ".followup.py"), code)
        write_file(join(save_path, prog_id + ".json"), metadata, as_json=True)
        count += 1
        print()

    green(f"EXECUTED {count} files this run")
