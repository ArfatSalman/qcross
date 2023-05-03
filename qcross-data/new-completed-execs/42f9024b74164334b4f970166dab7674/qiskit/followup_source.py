# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_f5ce15 = Parameter('p_f5ce15')
p_fa05b6 = Parameter('p_fa05b6')
p_75b77c = Parameter('p_75b77c')
p_e32c43 = Parameter('p_e32c43')
p_d9b3a9 = Parameter('p_d9b3a9')
p_415e22 = Parameter('p_415e22')
p_6c6aa2 = Parameter('p_6c6aa2')
p_66d326 = Parameter('p_66d326')
p_cf1375 = Parameter('p_cf1375')
p_9b1974 = Parameter('p_9b1974')
p_638ece = Parameter('p_638ece')
p_ee1794 = Parameter('p_ee1794')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(UGate(p_415e22, p_66d326, p_fa05b6), qargs=[qr[1]], cargs=[])
qc.append(RGate(3.9800961208659213, p_9b1974), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(p_f5ce15), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CU3Gate(p_6c6aa2, p_638ece, p_e32c43), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RGate(p_ee1794, p_d9b3a9), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(UGate(p_75b77c, p_cf1375, 5.6467633400840755), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_d66e91 = QuantumRegister(8, name='qr_d66e91')
qc.add_register(qr_d66e91)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_f5ce15: 3.0761375449158193, p_fa05b6: 2.414376925356305, p_75b77c: 3.820196974130503, p_e32c43: 2.251031643786726, p_d9b3a9: 4.7611258330830655, p_415e22: 4.403788193532198, p_6c6aa2: 3.359364374345002, p_66d326: 5.238005217278175, p_cf1375: 1.381440535002157, p_9b1974: 2.54258238968427, p_638ece: 4.018048446348199, p_ee1794: 4.3040860238694725})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1ead1f5c4766491b96e9a32f39b7cda8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1ead1f5c4766491b96e9a32f39b7cda8, shots=346).result().get_counts(qc)
RESULT = counts
