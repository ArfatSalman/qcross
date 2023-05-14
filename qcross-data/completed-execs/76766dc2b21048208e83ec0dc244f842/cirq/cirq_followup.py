
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_bec6f4 = Symbol('p_bec6f4')
p_6e47ec = Symbol('p_6e47ec')
p_b52923 = Symbol('p_b52923')
p_b0edf1 = Symbol('p_b0edf1')
p_7fdf26 = Symbol('p_7fdf26')
p_c19a9b = Symbol('p_c19a9b')
p_4a7236 = Symbol('p_4a7236')
p_eca484 = Symbol('p_eca484')
p_7c75a3 = Symbol('p_7c75a3')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_4a7236)( qr[3] ))
circuit.append(Gates.CRZGate(p_7fdf26)( qr[6], qr[3] ))
circuit.append(Gates.CRXGate(p_bec6f4)( qr[1], qr[7] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CPhaseGate(4.63837786161633)( qr[3], qr[0] ))
subcircuit.append(Gates.U2Gate(p_c19a9b, p_b0edf1)( qr[8] ))
subcircuit.append(Gates.CXGate( qr[2], qr[4] ))
subcircuit.append(Gates.SXGate( qr[0] ))
subcircuit.append(Gates.CRZGate(p_b52923)( qr[0], qr[5] ))
subcircuit.append(Gates.RCCXGate( qr[9], qr[1], qr[8] ))
subcircuit.append(Gates.RXXGate(p_6e47ec)( qr[4], qr[6] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(p_7c75a3)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(p_eca484)( qr[1] ))
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



circuit = cirq.resolve_parameters(circuit, {
    "p_bec6f4": 5.987304452123941,
    "p_6e47ec": 5.25962645863375,
    "p_b52923": 2.008796895454228,
    "p_b0edf1": 0.07157463504881167,
    "p_7fdf26": 4.2641612072511235,
    "p_c19a9b": 5.887184334931191,
    "p_4a7236": 6.163759533339787,
    "p_eca484": 4.229610589867865,
    "p_7c75a3": 4.167661441102218
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0', 'm_cr9_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

