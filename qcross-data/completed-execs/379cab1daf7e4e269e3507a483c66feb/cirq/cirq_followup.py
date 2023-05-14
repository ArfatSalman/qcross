
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_a097d1 = Symbol('p_a097d1')
p_fbe730 = Symbol('p_fbe730')
p_e16421 = Symbol('p_e16421')
p_136200 = Symbol('p_136200')
p_2941ca = Symbol('p_2941ca')
p_00d3fa = Symbol('p_00d3fa')
p_2c8bf5 = Symbol('p_2c8bf5')
p_61b250 = Symbol('p_61b250')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_a097d1)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_61b250)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_2c8bf5)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_00d3fa)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_136200)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_2941ca)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_fbe730)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_e16421)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_a097d1": 6.163759533339787,
    "p_fbe730": 5.94477504571567,
    "p_e16421": 5.1829934776392745,
    "p_136200": 4.167661441102218,
    "p_2941ca": 4.229610589867865,
    "p_00d3fa": 1.740253089260498,
    "p_2c8bf5": 1.0296448789776642,
    "p_61b250": 5.987304452123941
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

