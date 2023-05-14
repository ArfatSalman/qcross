# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[6]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[5], qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[9], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[0], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[9], qr[5]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[9]], cargs=[])
qc.append(SXGate(), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[7], qr[4]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[0], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[7], qr[8], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[8], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[8]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[9], qr[3]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[3]],
    cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RZGate(5.014941143947427), qargs=[qr[9]], cargs=[])
qc.append(CRXGate(5.970852306777193), qargs=[qr[1], qr[9]], cargs=[])
qc.append(UGate(5.080799300534071, 5.023617931957853, 2.271164628944128),
    qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[7], qr[4]], cargs=[])
# SECTION

# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data


qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_afd7f16070b64b6a9058f6a9cddb12e6 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_afd7f16070b64b6a9058f6a9cddb12e6, shots=5542).result().get_counts(qc)
RESULT = counts
