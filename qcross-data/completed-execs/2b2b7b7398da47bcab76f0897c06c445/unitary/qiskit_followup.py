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
p_1b7413 = Parameter('p_1b7413')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SXdgGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_1b7413), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
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
    p_1b7413: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2, coupling_map=[[0, 1], [0, 5], [1, 0], [1, 3], [2, 3], [3, 1], [3, 2], [3, 6], [4, 5], [5, 0], [5, 4], [6, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a2e8f9784ea6415996eab8dc23b24366 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a2e8f9784ea6415996eab8dc23b24366, shots=979).result().get_counts(qc)
RESULT = counts
