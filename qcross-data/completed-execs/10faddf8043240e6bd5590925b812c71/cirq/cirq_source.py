
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.CSXGate( qr[1], qr[2] ))
circuit.append(Gates.U3Gate(5.449671872109171, 3.00254832672447, 1.991190402029831)( qr[1] ))
circuit.append(Gates.CCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.CU3Gate(3.490361155617595, 2.1967031852441936, 3.6089446638145946)( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.CUGate(5.96415316326551, 5.459163154688654, 3.541730522116933, 2.478896182682137)( qr[1], qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
