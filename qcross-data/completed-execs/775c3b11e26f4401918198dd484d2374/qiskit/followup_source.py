# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_c99d8f = Parameter('p_c99d8f')
p_9cd4bb = Parameter('p_9cd4bb')
p_bacf18 = Parameter('p_bacf18')
p_a85ee4 = Parameter('p_a85ee4')
p_a479d9 = Parameter('p_a479d9')
p_85569c = Parameter('p_85569c')
p_8880d3 = Parameter('p_8880d3')
p_fece30 = Parameter('p_fece30')
p_dd152f = Parameter('p_dd152f')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_bacf18), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U2Gate(p_85569c, p_8880d3), qargs=[qr[2]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[2], qr[0], qr[1]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CU3Gate(6.086884486572108, p_a479d9, p_dd152f), qargs=[qr
    [2], qr[0]], cargs=[])
subcircuit.append(U3Gate(p_fece30, p_a85ee4, p_9cd4bb), qargs=[qr[1]], cargs=[]
    )
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_c99d8f), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_f02815 = QuantumRegister(7, name='qr_f02815')
qc.add_register(qr_f02815)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_c99d8f: 5.987304452123941, p_9cd4bb: 1.2128092629174942, p_bacf18: 6.163759533339787, p_a85ee4: 5.190931186022931, p_a479d9: 3.06538533241841, p_85569c: 0.03501337194718552, p_8880d3: 2.6397681660693015,
    p_fece30: 5.01836135520768,
    p_dd152f: 1.7532443887147882,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_09b5690e34e649a9a041c41a2423721e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_09b5690e34e649a9a041c41a2423721e, shots=489).result().get_counts(qc)
RESULT = counts
