
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_22f003 = Symbol('p_22f003')
p_b0e1f1 = Symbol('p_b0e1f1')
p_74570c = Symbol('p_74570c')
p_2ab273 = Symbol('p_2ab273')
p_0e1639 = Symbol('p_0e1639')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.CRZGate(p_22f003)( qr[6], qr[2] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[7] ))
circuit.append(Gates.RCCXGate( qr[10], qr[6], qr[8] ))
circuit.append(Gates.RZGate(p_74570c)( qr[0] ))
circuit.append(Gates.CCXGate( qr[7], qr[10], qr[2] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZGate(4.940217775579305)( qr[1] ))
subcircuit.append(Gates.RYYGate(0.6724371252296606)( qr[9], qr[0] ))
subcircuit.append(Gates.PhaseGate(p_0e1639)( qr[0] ))
subcircuit.append(Gates.ECRGate( qr[3], qr[0] ))
subcircuit.append(Gates.PhaseGate(p_2ab273)( qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.U2Gate(4.214504315296764, p_b0e1f1)( qr[10] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))
circuit.append(cirq.measure(qr[10], key='cr10'))



circuit = cirq.resolve_parameters(circuit, {
    "p_22f003": 4.2641612072511235,
    "p_b0e1f1": 4.6235667602042065,
    "p_74570c": 4.229610589867865,
    "p_2ab273": 0.4827903095199283,
    "p_0e1639": 5.5146057452272546
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0', 'm_cr9_0', 'm_cr10_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

