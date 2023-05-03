
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.RYYGate(2.10593478876119)( qr[2], qr[1] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CZGate( qr[2], qr[3] ))
circuit.append(Gates.CZGate( qr[0], qr[3] ))
circuit.append(Gates.CZGate( qr[1], qr[2] ))
circuit.append(Gates.CU3Gate(5.177552214723695, 3.7847055340640803, 5.596894918056728)( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[2], qr[3] ))
circuit.append(Gates.CPhaseGate(5.982058731459433)( qr[2], qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.C3XGate( qr[3], qr[1], qr[2], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
