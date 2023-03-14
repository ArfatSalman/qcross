from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *


qr = QuantumRegister(7, name="qr")
cr = ClassicalRegister(7, name="cr")
qc = QuantumCircuit(qr, cr, name="qc")
qc.append(
    UGate(2.2050953212701585, 3.3615540885941595, 4.353999488160196),
    qargs=[qr[4]],
    cargs=[],
)
qc.append(C3XGate(), qargs=[qr[4], qr[1], qr[3], qr[5]], cargs=[])
qc.append(
    CUGate(
        1.8216381126900292, 1.1397633674319172, 5.883270079132554, 6.151280357960994
    ),
    qargs=[qr[2], qr[6]],
    cargs=[],
)
qc.append(RZGate(0.8251147604978816), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(3.4573000463617367), qargs=[qr[5], qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[3], qr[4]], cargs=[])
qc.append(U2Gate(2.647545737192122, 3.1045763954315304), qargs=[qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(
    CU3Gate(1.3925947961767187, 3.8341186215245604, 3.461675537985181),
    qargs=[qr[5], qr[1]],
    cargs=[],
)
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[0], qr[4], qr[2]], cargs=[])
qc.append(RZXGate(6.045230636776243), qargs=[qr[4], qr[6]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(1.627140919622475), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[5], qr[1], qr[2]], cargs=[])
qc.append(
    CU3Gate(1.4873061282104487, 6.193271645272907, 0.08920760414730318),
    qargs=[qr[5], qr[1]],
    cargs=[],
)
qc.append(IGate(), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[4]], cargs=[])
qc.append(C4XGate(), qargs=[qr[0], qr[2], qr[6], qr[5], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[6], qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[6], qr[1]], cargs=[])

qc.measure(qr, cr)

from qiskit import transpile

qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
