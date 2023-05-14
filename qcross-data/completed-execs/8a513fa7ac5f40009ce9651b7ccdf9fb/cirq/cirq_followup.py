
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

p_6981a8 = Symbol('p_6981a8')
p_ab5b20 = Symbol('p_ab5b20')
p_41c813 = Symbol('p_41c813')
p_209e7d = Symbol('p_209e7d')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_ab5b20)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRXGate(p_209e7d)( qr[2], qr[5] ))
circuit.append(Gates.C3SXGate( qr[6], qr[0], qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[4], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[6], qr[3] ))
circuit.append(Gates.SdgGate( qr[6] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CZGate( qr[4], qr[1] ))
subcircuit.append(Gates.IGate( qr[1] ))
subcircuit.append(Gates.RXGate(p_6981a8)( qr[0] ))
subcircuit.append(Gates.RZXGate(4.563562108824195)( qr[4], qr[0] ))
subcircuit.append(Gates.C3XGate(p_41c813)( qr[4], qr[6], qr[2], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RCCXGate( qr[2], qr[5], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_6981a8": 0.2906326206587185,
    "p_ab5b20": 6.163759533339787,
    "p_41c813": 5.94477504571567,
    "p_209e7d": 2.0099472182748075
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

