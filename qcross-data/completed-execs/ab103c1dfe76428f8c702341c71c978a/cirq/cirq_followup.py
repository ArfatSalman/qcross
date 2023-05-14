
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_44bd2b = Symbol('p_44bd2b')
p_2e218a = Symbol('p_2e218a')

circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.U1Gate(p_2e218a)( qr[2] ))
subcircuit.append(Gates.SwapGate( qr[1], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(p_44bd2b)( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_44bd2b": 6.163759533339787,
    "p_2e218a": 6.225782237242023
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

