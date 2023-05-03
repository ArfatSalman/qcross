
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.CRXGate(5.2771665030277894)( qr[2], qr[5] ))
circuit.append(Gates.RYGate(2.7769187719860096)( qr[5] ))
circuit.append(Gates.CRYGate(2.1848751379170706)( qr[0], qr[2] ))
circuit.append(Gates.C3XGate( qr[0], qr[1], qr[5], qr[4] ))
circuit.append(Gates.RYGate(0.43166458716598444)( qr[0] ))
circuit.append(Gates.DCXGate( qr[1], qr[3] ))
circuit.append(Gates.RXGate(4.785958015357605)( qr[0] ))
circuit.append(Gates.CRXGate(5.271022058006445)( qr[3], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
