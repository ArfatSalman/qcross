
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_3c4bb1 = Symbol('p_3c4bb1')
p_5e74b9 = Symbol('p_5e74b9')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_3c4bb1)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_5e74b9)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_3c4bb1": 6.163759533339787,
    "p_5e74b9": 2.0099472182748075
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

