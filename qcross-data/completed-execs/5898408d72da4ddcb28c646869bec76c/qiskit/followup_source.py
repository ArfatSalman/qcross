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
p_bdf701 = Parameter('p_bdf701')
p_9d6cc2 = Parameter('p_9d6cc2')
p_86ace7 = Parameter('p_86ace7')
p_8bc5a1 = Parameter('p_8bc5a1')
p_3abe65 = Parameter('p_3abe65')
p_28fe7c = Parameter('p_28fe7c')
p_ec0d90 = Parameter('p_ec0d90')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3abe65), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_bdf701), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_ec0d90, p_28fe7c, p_9d6cc2, p_86ace7), qargs=[qr[0], qr[
    2]], cargs=[])
qc.append(CU1Gate(p_8bc5a1), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_bdf701: 4.066449154047175,
    p_9d6cc2: 2.3864521352475245,
    p_86ace7: 5.987304452123941,
    p_8bc5a1: 5.154187354656876,
    p_3abe65: 6.163759533339787,
    p_28fe7c: 5.897054719225356,
    p_ec0d90: 0.5112149185250571,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1e1182192d9c497c9660975951b60401 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1e1182192d9c497c9660975951b60401, shots=692).result().get_counts(qc)
RESULT = counts
