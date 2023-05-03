
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_566c5c = Symbol('p_566c5c')
p_d15eb0 = Symbol('p_d15eb0')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_566c5c)( qr[1] ))
circuit.append(Gates.SXdgGate( qr[3] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.ECRGate( qr[1], qr[3] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[4], qr[1] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[1], qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[4] ))
circuit.append(Gates.RYYGate(p_d15eb0)( qr[0], qr[3] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[2], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[2], key='cr1'))
circuit.append(cirq.measure(qr[3], key='cr2'))
circuit.append(cirq.measure(qr[1], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_566c5c": 6.163759533339787,
    "p_d15eb0": 1.6723037552953224
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

