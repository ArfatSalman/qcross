
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

p_c8a5e6 = Symbol('p_c8a5e6')

circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(p_c8a5e6)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))



circuit = cirq.resolve_parameters(circuit, {
    "p_c8a5e6": 6.163759533339787
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

