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
p_b96123 = Parameter('p_b96123')
p_016d54 = Parameter('p_016d54')
p_99427e = Parameter('p_99427e')
p_93d5ac = Parameter('p_93d5ac')
p_7691c4 = Parameter('p_7691c4')
p_7ec4f4 = Parameter('p_7ec4f4')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(HGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RZZGate(p_99427e), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CRZGate(p_016d54), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RYYGate(0.5501056885328758), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(p_93d5ac), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_b96123), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_7691c4), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_7ec4f4), qargs=[qr[4], qr[6]], cargs=[])
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
    p_b96123: 4.229610589867865,
    p_016d54: 2.008796895454228,
    p_99427e: 5.017245588344839,
    p_93d5ac: 2.0099472182748075,
    p_7691c4: 3.2142159669963557,
    p_7ec4f4: 5.94477504571567,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_bbdebb65717c413db1b9c4158d88f683 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_bbdebb65717c413db1b9c4158d88f683, shots=1959).result().get_counts(qc)
RESULT = counts
