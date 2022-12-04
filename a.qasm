// Generated from Cirq v1.0.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6), q(7), q(8)]
qreg q[9];
creg m_cr7[1];
creg m_cr8[1];
creg m_cr5[1];
creg m_cr2[1];
creg m_cr3[1];
creg m_cr6[1];
creg m_cr4[1];
creg m_cr1[1];
creg m_cr0[1];


// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7589d0>.on(cirq.LineQubit(6)),
 //            <__main__.PhaseGate object at 0x12a758370>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(6)),
 //            <__main__.PhaseGate object at 0x12a758910>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            <__main__.UGate object at 0x12a758af0>.on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(6)),
 //            <__main__.PhaseGate object at 0x12a75f5e0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.UGate object at 0x12a758c10>.on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            cirq.S(cirq.LineQubit(6)),
 //        ),
 //    ]),
 //), 'merged')
u3(0,0,pi*1.4412702455) q[6];
u3(0,0,pi*1.9058181987) q[0];
ry(pi*-0.5) q[6];
u3(0,0,pi*1.318361062) q[0];
cz q[0],q[6];
ry(pi*0.5) q[6];
u3(pi*0.0813623813,pi*1.0,pi*1.681638938) q[6];
ry(pi*-0.5) q[6];
cz q[0],q[6];
ry(pi*0.5) q[6];
u3(0,0,pi*0.0625) q[0];
u3(pi*0.0813623813,pi*1.8770908165,0) q[6];
s q[6];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(4)),
 //            <__main__.PhaseGate object at 0x12a72ca00>.on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a751d00>.on(cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(4)),
 //            cirq.Z(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a74a3d0>.on(cirq.LineQubit(4)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(4)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(4)),
 //        ),
 //    ]),
 //), 'merged')
ry(pi*0.5) q[4];
u3(0,0,pi*0.25) q[2];
rx(pi*1.0) q[4];
ry(pi*-0.5) q[4];
cz q[2],q[4];
ry(pi*0.5) q[4];
u3(0,0,pi*1.75) q[4];
ry(pi*-0.5) q[4];
cz q[2],q[4];
ry(pi*0.5) q[4];
z q[2];
u3(0,0,pi*0.25) q[4];
ry(pi*-0.5) q[2];
ry(pi*0.5) q[4];
rx(pi*1.0) q[4];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a767460>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a767580>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];
cz q[0],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*1.9375) q[5];
ry(pi*-0.5) q[5];
cz q[0],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*0.0625) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.Rz(rads=6.163759533339787).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a75f820>.on(cirq.LineQubit(8)),
 //        ),
 //    ]),
 //), 'merged')
rz(pi*1.9619855955) q[8];
ry(pi*-0.5) q[8];
cz q[0],q[8];
ry(pi*0.5) q[8];
u3(0,0,pi*1.9375) q[8];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a767e80>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a767fa0>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
cz q[8],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*0.0625) q[5];
ry(pi*-0.5) q[5];
cz q[8],q[5];
ry(pi*0.5) q[5];
ry(pi*-0.5) q[8];
u3(0,0,pi*1.9375) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a75fa00>.on(cirq.LineQubit(8)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[8];
ry(pi*0.5) q[8];
u3(0,0,pi*0.0625) q[8];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7698e0>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a769a00>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
cz q[8],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*1.9375) q[5];
ry(pi*-0.5) q[5];
cz q[8],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*0.0625) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a75fbe0>.on(cirq.LineQubit(7)),
 //        ),
 //    ]),
 //), 'merged')
ry(pi*-0.5) q[7];
cz q[8],q[7];
ry(pi*0.5) q[7];
u3(0,0,pi*1.9375) q[7];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76b340>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76b460>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
cz q[7],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*0.0625) q[5];
ry(pi*-0.5) q[5];
cz q[7],q[5];
ry(pi*0.5) q[5];
ry(pi*-0.5) q[7];
u3(0,0,pi*1.9375) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a75fdc0>.on(cirq.LineQubit(7)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[7];
ry(pi*0.5) q[7];
u3(0,0,pi*0.0625) q[7];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76bd60>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76be80>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
cz q[7],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*1.9375) q[5];
ry(pi*-0.5) q[5];
cz q[7],q[5];
ry(pi*0.5) q[5];
ry(pi*-0.5) q[7];
u3(0,0,pi*0.0625) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(7)),
 //            cirq.S(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a75ffa0>.on(cirq.LineQubit(7)),
 //            <__main__.PhaseGate object at 0x12a797a90>.on(cirq.LineQubit(8)),
 //        ),
 //    ]),
 //), 'merged')
cz q[8],q[7];
ry(pi*0.5) q[7];
s q[8];
u3(0,0,pi*1.9375) q[7];
u3(0,0,pi*0.5115583593) q[8];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76c7c0>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76c8e0>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
cz q[7],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*0.0625) q[5];
ry(pi*-0.5) q[5];
cz q[7],q[5];
ry(pi*0.5) q[5];
ry(pi*-0.5) q[7];
u3(0,0,pi*1.9375) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
ry(pi*-0.5) q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(7)),
 //            cirq.S(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7671c0>.on(cirq.LineQubit(7)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[7];
ry(pi*0.5) q[7];
s q[0];
u3(0,0,pi*0.0625) q[7];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76e220>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(7), cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //            cirq.Z(cirq.LineQubit(7)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a76e340>.on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(5)),
 //        ),
 //        cirq.Moment(
 //            cirq.X(cirq.LineQubit(5)),
 //        ),
 //    ]),
 //), 'merged')
cz q[7],q[5];
ry(pi*0.5) q[5];
u3(0,0,pi*1.9375) q[5];
ry(pi*-0.5) q[5];
cz q[7],q[5];
ry(pi*0.5) q[5];
z q[7];
u3(0,0,pi*0.0625) q[5];
ry(pi*0.5) q[5];
rx(pi*1.0) q[5];
x q[5];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            <__main__.SdgGate object at 0x12a70dd90>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a77b6d0>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7815b0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7816d0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
u3(0,0,pi*1.5) q[1];
u3(0,0,pi*0.0625) q[1];
cz q[1],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*1.9375) q[0];
ry(pi*-0.5) q[0];
cz q[1],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*0.0625) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a77b970>.on(cirq.LineQubit(3)),
 //        ),
 //    ]),
 //), 'merged')
ry(pi*-0.5) q[3];
cz q[1],q[3];
ry(pi*0.5) q[3];
u3(0,0,pi*1.9375) q[3];

measure q[7] -> m_cr7[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a781fd0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a783130>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[3],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*0.0625) q[0];
ry(pi*-0.5) q[0];
cz q[3],q[0];
ry(pi*0.5) q[0];
ry(pi*-0.5) q[3];
u3(0,0,pi*1.9375) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a77bb50>.on(cirq.LineQubit(3)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[3];
ry(pi*0.5) q[3];
u3(0,0,pi*0.0625) q[3];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a783a30>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a783b50>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[3],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*1.9375) q[0];
ry(pi*-0.5) q[0];
cz q[3],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*0.0625) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a77bd30>.on(cirq.LineQubit(2)),
 //        ),
 //    ]),
 //), 'merged')
cz q[3],q[2];
ry(pi*0.5) q[2];
u3(0,0,pi*1.9375) q[2];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a784490>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7845b0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[2],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*0.0625) q[0];
ry(pi*-0.5) q[0];
cz q[2],q[0];
ry(pi*0.5) q[0];
ry(pi*-0.5) q[2];
u3(0,0,pi*1.9375) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a77bf10>.on(cirq.LineQubit(2)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[2];
ry(pi*0.5) q[2];
u3(0,0,pi*0.0625) q[2];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a784eb0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a784fd0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[2],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*1.9375) q[0];
ry(pi*-0.5) q[0];
cz q[2],q[0];
ry(pi*0.5) q[0];
ry(pi*-0.5) q[2];
u3(0,0,pi*0.0625) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a781130>.on(cirq.LineQubit(2)),
 //        ),
 //    ]),
 //), 'merged')
cz q[3],q[2];
ry(pi*0.5) q[2];
ry(pi*-0.5) q[3];
u3(0,0,pi*1.9375) q[2];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a786910>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a786a30>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[2],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*0.0625) q[0];
ry(pi*-0.5) q[0];
cz q[2],q[0];
ry(pi*0.5) q[0];
ry(pi*-0.5) q[2];
u3(0,0,pi*1.9375) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a797880>.on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(8), cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(3)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a797970>.on(cirq.LineQubit(3)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7e0c40>.on(cirq.LineQubit(3)),
 //        ),
 //    ]),
 //), 'merged')
cz q[8],q[3];
ry(pi*0.5) q[3];
u3(0,0,pi*1.4884416407) q[3];
ry(pi*-0.5) q[3];
cz q[8],q[3];
ry(pi*0.5) q[3];
ry(pi*-0.5) q[8];
u3(0,0,pi*0.5115583593) q[3];
u3(0,0,pi*0.25) q[3];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //            (cirq.Z**1.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a781310>.on(cirq.LineQubit(2)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[2];
ry(pi*0.5) q[2];
rz(pi*1.5) q[1];
u3(0,0,pi*0.0625) q[2];
ry(pi*-0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(5), cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Z**1.7753961306604513).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(5), cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Z**0.22460386933954862).on(cirq.LineQubit(8)),
 //        ),
 //        cirq.Moment(
 //            cirq.T(cirq.LineQubit(8)),
 //        ),
 //    ]),
 //), 'merged')
cz q[5],q[8];
ry(pi*0.5) q[8];
rz(pi*1.7753961307) q[8];
ry(pi*-0.5) q[8];
cz q[5],q[8];
ry(pi*0.5) q[8];
rz(pi*0.2246038693) q[8];
t q[8];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a788370>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(2), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //            cirq.Z(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a788490>.on(cirq.LineQubit(0)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.SXGate object at 0x12a7161f0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7dbc70>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7dbf10>.on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7e0070>.on(cirq.LineQubit(2)),
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //    ]),
 //), 'merged')
cz q[2],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*1.9375) q[0];
ry(pi*-0.5) q[0];
cz q[2],q[0];
ry(pi*0.5) q[0];
z q[2];
u3(0,0,pi*0.0625) q[0];
ry(pi*0.5) q[2];
ry(pi*0.5) q[0];
rx(pi*1.0) q[2];
rx(pi*1.0) q[0];
ry(pi*-0.5) q[2];
u3(pi*0.5,pi*1.5,pi*0.5) q[0];
u3(0,0,pi*0.25) q[0];
cz q[0],q[2];
ry(pi*0.5) q[2];
u3(0,0,pi*1.75) q[2];
ry(pi*-0.5) q[2];
cz q[0],q[2];
ry(pi*0.5) q[2];
ry(pi*0.5) q[0];
u3(0,0,pi*0.25) q[2];
rx(pi*1.0) q[0];
ry(pi*0.5) q[2];
ry(pi*-0.5) q[0];
rx(pi*1.0) q[2];
ry(pi*-0.5) q[2];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(6), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Z**1.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.24999999999999992).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(6), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //            cirq.T(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.24999999999999992).on(cirq.LineQubit(1)),
 //            (cirq.Y**-0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            cirq.Z(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[6],q[1];
ry(pi*0.5) q[1];
rz(pi*1.5) q[1];
ry(pi*0.25) q[1];
ry(pi*-0.5) q[1];
cz q[6],q[1];
ry(pi*0.5) q[1];
t q[6];
ry(pi*-0.25) q[1];
ry(pi*-0.5) q[6];
z q[1];

measure q[8] -> m_cr8[0];
measure q[5] -> m_cr5[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Z**1.588392061106321).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(2)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(2)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Z**0.4116079388936794).on(cirq.LineQubit(2)),
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.U2Gate object at 0x12a716a00>.on(cirq.LineQubit(2)),
 //            cirq.T(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[2];
ry(pi*0.5) q[2];
rz(pi*1.5883920611) q[2];
ry(pi*-0.5) q[2];
cz q[1],q[2];
ry(pi*0.5) q[2];
ry(pi*0.5) q[1];
rz(pi*0.4116079389) q[2];
rx(pi*1.0) q[1];
u3(pi*0.5,pi*0.8009647808,pi*0.6772464167) q[2];
t q[1];
ry(pi*-0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7e0ee0>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(3), cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7e4040>.on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            cirq.T(cirq.LineQubit(0)),
 //        ),
 //    ]),
 //), 'merged')
cz q[3],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*1.75) q[0];
ry(pi*-0.5) q[0];
cz q[3],q[0];
ry(pi*0.5) q[0];
u3(0,0,pi*0.25) q[0];
ry(pi*0.5) q[0];
rx(pi*1.0) q[0];
t q[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[1];
ry(pi*0.5) q[1];

measure q[2] -> m_cr2[0];
measure q[3] -> m_cr3[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.T**-1).on(cirq.LineQubit(1)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //            cirq.T(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(6)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[6];
tdg q[1];
ry(pi*0.5) q[6];
ry(pi*-0.5) q[1];
t q[6];
ry(pi*-0.5) q[6];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[1];
ry(pi*0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.T**-1).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(6)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[6];
ry(pi*-0.5) q[1];
ry(pi*0.5) q[6];
tdg q[6];
ry(pi*-0.5) q[6];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[1];
ry(pi*0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.T**-1).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(6)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[6];
ry(pi*-0.5) q[1];
ry(pi*0.5) q[6];
tdg q[6];
ry(pi*-0.5) q[6];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[1];
ry(pi*0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(1), cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //            (cirq.Y**0.5).on(cirq.LineQubit(6)),
 //        ),
 //        cirq.Moment(
 //            cirq.XPowGate(global_shift=-0.25).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.U2Gate object at 0x12a7ea1c0>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7ead90>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[1],q[6];
ry(pi*0.5) q[1];
ry(pi*0.5) q[6];
rx(pi*1.0) q[1];
u3(pi*0.5,0,pi*1.0) q[1];
u3(0,0,pi*0.25) q[1];
ry(pi*-0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7ea910>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[1];
ry(pi*0.5) q[1];
u3(0,0,pi*1.75) q[1];
ry(pi*-0.5) q[1];

measure q[6] -> m_cr6[0];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(4), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7eaa90>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**-0.5).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[4],q[1];
ry(pi*0.5) q[1];
u3(0,0,pi*0.25) q[1];
ry(pi*-0.5) q[1];

// Operation: cirq.TaggedOperation(cirq.CircuitOperation(
 //    circuit=cirq.FrozenCircuit([
 //        cirq.Moment(
 //            cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            (cirq.Y**0.5).on(cirq.LineQubit(1)),
 //            cirq.T(cirq.LineQubit(0)),
 //        ),
 //        cirq.Moment(
 //            <__main__.PhaseGate object at 0x12a7eabb0>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            <__main__.U2Gate object at 0x12a7eacd0>.on(cirq.LineQubit(1)),
 //        ),
 //        cirq.Moment(
 //            cirq.Rz(rads=5.014941143947427).on(cirq.LineQubit(1)),
 //        ),
 //    ]),
 //), 'merged')
cz q[0],q[1];
ry(pi*0.5) q[1];
t q[0];
u3(0,0,pi*1.75) q[1];
u3(pi*0.5,0,pi*1.0) q[1];
rz(pi*1.5963053447) q[1];

measure q[4] -> m_cr4[0];
measure q[1] -> m_cr1[0];
measure q[0] -> m_cr0[0];

