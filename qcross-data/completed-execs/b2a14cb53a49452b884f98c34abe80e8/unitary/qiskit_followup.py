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
p_ec106f = Parameter('p_ec106f')
p_5f113d = Parameter('p_5f113d')
p_cf8439 = Parameter('p_cf8439')
p_7e38fe = Parameter('p_7e38fe')
p_50c455 = Parameter('p_50c455')
p_e13c2b = Parameter('p_e13c2b')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_ec106f), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U3Gate(p_7e38fe, p_5f113d, 0.4903361071050254), qargs=[qr
    [1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(p_e13c2b, p_50c455, p_cf8439), qargs=[qr[4]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
# SECTION

# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data


qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_ec106f: 6.163759533339787,
    p_5f113d: 5.154187354656876,
    p_cf8439: 1.2128092629174942,
    p_7e38fe: 4.094867647151279,
    p_50c455: 5.190931186022931,
    p_e13c2b: 5.01836135520768,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6e23615515b34e5b925cb21f7b88f7ef = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6e23615515b34e5b925cb21f7b88f7ef, shots=7838).result().get_counts(qc)
RESULT = counts
