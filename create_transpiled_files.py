from pathlib import Path
from transpiler import CirqCircuit


qiskit_circuits_folder = "data/qmt_v53/programs/source/"
cirq_circuits_folder = "data/qmt-cirq/cirq-src/"
exec_metadata_path = "data/qmt-cirq/exec-metadata/"

Path(cirq_circuits_folder).mkdir(parents=True, exist_ok=True)
Path(exec_metadata_path).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    import sys

    program_id = sys.argv[1]
    with open(f"data/qmt_v52/programs/source/{program_id}.py", encoding="utf-8") as f:
        content = f.read()
        c = CirqCircuit(content)
        config = {
            "add_unitary": False,
            # "null_circuit": True,
            # "qasm_roundtrip": True,
            "transformations": [
                "defer_measurements",
                "merge_k_qubit_unitaries",
                "drop_empty_moments",
                "eject_z",
                "eject_phased_paulis",
                "drop_negligible_operations",
                "stratified_circuit",
                "synchronize_terminal_measurements",
            ],
        }
        a, b = c.get_follow_up(config)
        print(b)
