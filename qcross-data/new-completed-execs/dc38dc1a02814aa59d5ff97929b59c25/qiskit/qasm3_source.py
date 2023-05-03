# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SdgGate(), qargs=[qr[9]], cargs=[])
qc.append(HGate(), qargs=[qr[6]], cargs=[])
qc.append(U3Gate(6.248539137506652, 3.0437559890158274, 3.877040016955039), qargs=[qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RYGate(2.4289944643648695), qargs=[qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[9], qr[1]], cargs=[])
qc.append(RYYGate(2.092741391579245), qargs=[qr[6], qr[3]], cargs=[])
qc.append(RZGate(2.184568031539945), qargs=[qr[9]], cargs=[])
qc.append(RZGate(0.6748073587752819), qargs=[qr[4]], cargs=[])
qc.append(U1Gate(1.4687935154189555), qargs=[qr[9]], cargs=[])
qc.append(UGate(2.4455568111156785, 3.2132129187211773, 5.7839656565594115), qargs=[qr[3]], cargs=[])
qc.append(U1Gate(2.6497338339327143), qargs=[qr[9]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(RXGate(0.6137530841617304), qargs=[qr[0]], cargs=[])
qc.append(CSGate(), qargs=[qr[9], qr[4]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RGate(3.863590788996665,1.7755874178641218), qargs=[qr[0]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[7]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(HGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[8], qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[9], qr[7]], cargs=[])
qc.append(CPhaseGate(4.048113620213937), qargs=[qr[5], qr[9]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[7], qr[2]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_30ca0e3873314869b4ca9c4b2bab5d6b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_30ca0e3873314869b4ca9c4b2bab5d6b, shots=5542).result().get_counts(qc)
RESULT = counts
