# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_4f8db3 = Parameter('p_4f8db3')
p_daae8b = Parameter('p_daae8b')
p_89f9ae = Parameter('p_89f9ae')
p_6f799f = Parameter('p_6f799f')
p_25d5a8 = Parameter('p_25d5a8')
p_eadd70 = Parameter('p_eadd70')
p_efceeb = Parameter('p_efceeb')
p_0cd2a2 = Parameter('p_0cd2a2')
p_574806 = Parameter('p_574806')
p_2907ce = Parameter('p_2907ce')
p_a8217e = Parameter('p_a8217e')
p_cf4aa0 = Parameter('p_cf4aa0')
p_a87faa = Parameter('p_a87faa')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_0cd2a2), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_a8217e), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_25d5a8), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_a87faa), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_6f799f, 4.167661441102218, 4.623446645668956, p_daae8b),
    qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(p_4f8db3), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_efceeb), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_574806), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, 0.07157463504881167, p_89f9ae), qargs=[
    qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU1Gate(p_cf4aa0), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[3], qr[1]], cargs=[])
qc.append(CUGate(5.03147076606842, p_eadd70, p_2907ce, 4.940217775579305),
    qargs=[qr[4], qr[3]], cargs=[])
qc.append(CRZGate(3.839241945509346), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_4f8db3: 4.229610589867865, p_daae8b: 3.865496458458116, p_89f9ae: 1.4112277317699358, p_6f799f: 5.708725119517347, p_25d5a8: 1.0296448789776642, p_eadd70: 5.0063780207098425, p_efceeb: 5.398622178940033, p_0cd2a2: 6.163759533339787, p_574806: 3.2142159669963557, p_2907ce: 3.1562533916051736,
    p_a8217e: 2.0099472182748075,
    p_cf4aa0: 4.028174522740928,
    p_a87faa: 1.6723037552953224,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c214cb22331d43e0a37bad87e8016837 = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_c214cb22331d43e0a37bad87e8016837, shots=979).result().get_counts(qc)
RESULT = counts
