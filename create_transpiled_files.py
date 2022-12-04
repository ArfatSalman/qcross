from pathlib import Path
from transpiler import CirqCircuit


qiskit_circuits_folder = "data/qmt_v53/programs/source/"
cirq_circuits_folder = "data/qmt-cirq/cirq-src/"
exec_metadata_path = "data/qmt-cirq/exec-metadata/"

Path(cirq_circuits_folder).mkdir(parents=True, exist_ok=True)
Path(exec_metadata_path).mkdir(parents=True, exist_ok=True)


code = """

# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZXGate(3.4148838654876075), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U1Gate(3.916311088799146), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(RYGate(0.30914088102270665), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(2.05519166016469), qargs=[qr[1], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[2]], cargs=[])
qc.append(U1Gate(2.19375409896333), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXXGate(0.6958411378279826), qargs=[qr[1], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U1Gate(2.5118976499714747), qargs=[qr[2]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[2], qr[1], qr[3], qr[0]], cargs=[])
qc.append(U1Gate(5.406194560026072), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(4.385627314003304), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[3]], cargs=[])
qc.append(RYGate(6.139804541076739), qargs=[qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[3], qr[0], qr[2]], cargs=[])
qc.append(UGate(2.7159856050146742,2.4635653656106844,5.909205091787408), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(2.730791138901111), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RXXGate(5.4691544369544545), qargs=[qr[3], qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(UGate(1.2541495406941519,3.6300156777625117,0.8739290527186184), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e1e30142c35d4d72a6e6051b22e81691 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e1e30142c35d4d72a6e6051b22e81691, shots=692).result().get_counts(qc)
RESULT = counts
print(counts)
"""
c = CirqCircuit(code)
# a = c.get_equivalent()
config = {
    "add_unitary": True,
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
# print(b)
