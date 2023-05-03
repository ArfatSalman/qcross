# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name="qr")
cr = ClassicalRegister(6, name="cr")
qc = QuantumCircuit(qr, cr, name="qc")
qc.append(RZXGate(5.294170317838349), qargs=[qr[2], qr[4]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[5]], cargs=[])
qc.append(
    U3Gate(5.951221312078038, 5.377869177229497, 4.13307667574035),
    qargs=[qr[2]],
    cargs=[],
)
qc.append(ECRGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[4]], cargs=[])
qc.append(
    U3Gate(3.127390581057496, 0.8951620930728853, 2.9211253533322705),
    qargs=[qr[4]],
    cargs=[],
)
qc.append(CPhaseGate(3.2345621726383063), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRYGate(1.5739612232900921), qargs=[qr[4], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(RXGate(2.1921350525840335), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(4.81139250369156), qargs=[qr[0], qr[3]], cargs=[])
qc.append(
    CU3Gate(0.5792738051909873, 5.615330906310357, 2.660875175684596),
    qargs=[qr[5], qr[0]],
    cargs=[],
)
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(U2Gate(4.245494087381378, 0.35899282563221724), qargs=[qr[0]], cargs=[])
qc.append(
    UGate(1.0608924835540103, 2.415674942808992, 0.8187346879786549),
    qargs=[qr[3]],
    cargs=[],
)
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXGate(5.956960136241147), qargs=[qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[4], qr[5]], cargs=[])
qc.append(
    U3Gate(1.5683345978951369, 1.4287408195765756, 2.3460687004856973),
    qargs=[qr[1]],
    cargs=[],
)
qc.append(CU1Gate(1.9757038692524151), qargs=[qr[3], qr[1]], cargs=[])
qc.append(
    U3Gate(0.4602821600746163, 5.414451003251248, 4.293440251468374),
    qargs=[qr[4]],
    cargs=[],
)
qc.append(CZGate(), qargs=[qr[4], qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(4.463598643942479), qargs=[qr[1], qr[5]], cargs=[])
qc.append(
    CU3Gate(3.8745722202781416, 3.2737382848299332, 3.2686683844993465),
    qargs=[qr[5], qr[0]],
    cargs=[],
)
qc.append(SdgGate(), qargs=[qr[4]], cargs=[])  # SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile

qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute

backend_cb1eced4fa3a47cb8a42c7d0bea463c9 = Aer.get_backend("qasm_simulator")
counts = (
    execute(qc, backend=backend_cb1eced4fa3a47cb8a42c7d0bea463c9, shots=1385)
    .result()
    .get_counts(qc)
)
RESULT = counts
