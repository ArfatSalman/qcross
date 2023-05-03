# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(DCXGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(RVGate(6.18003471835015, 5.977025954690239, 2.6287210175731346), qargs=[qr[4]], cargs=[])
qc.append(U1Gate(0.18970742217530903), qargs=[qr[3]], cargs=[])
qc.append(CPhaseGate(2.916558815706837), qargs=[qr[2], qr[1]], cargs=[])
qc.append(U2Gate(1.5787156628547458, 2.0930109781345063), qargs=[qr[2]], cargs=[])
qc.append(CRXGate(5.786879734179932), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CPhaseGate(4.358574517050474), qargs=[qr[3], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(U1Gate(2.950818625000669), qargs=[qr[0]], cargs=[])
qc.append(CPhaseGate(1.6476787886644708), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CPhaseGate(4.051497867526455), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fe5b835116984e9aaa0a8736892b9b93 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fe5b835116984e9aaa0a8736892b9b93, shots=979).result().get_counts(qc)
RESULT = counts
