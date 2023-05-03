# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_bf86c5 = Parameter('p_bf86c5')
p_12cca6 = Parameter('p_12cca6')
p_7c142a = Parameter('p_7c142a')
p_a3bcf5 = Parameter('p_a3bcf5')
p_451cf1 = Parameter('p_451cf1')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_bf86c5), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_7c142a), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_12cca6), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_a3bcf5), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_451cf1), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_bf86c5: 6.163759533339787,
    p_12cca6: 5.987304452123941,
    p_7c142a: 4.2641612072511235,
    p_a3bcf5: 4.167661441102218,
    p_451cf1: 4.229610589867865,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_07df460318714ba0a0e06de1cf7b714b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_07df460318714ba0a0e06de1cf7b714b, shots=5542).result().get_counts(qc)
RESULT = counts
print(RESULT)