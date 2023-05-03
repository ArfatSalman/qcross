
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054)( qr[5], qr[3] ))
circuit.append(Gates.U2Gate(0.49960530614896387, 3.4965748481666385)( qr[0] ))
circuit.append(Gates.RYGate(1.6125723299807893)( qr[0] ))
circuit.append(Gates.C3XGate( qr[9], qr[1], qr[5], qr[2] ))
circuit.append(Gates.RYGate(5.620914585085149)( qr[9] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.ZGate( qr[7] ))
circuit.append(Gates.CSwapGate( qr[4], qr[2], qr[9] ))
circuit.append(Gates.CRYGate(1.9836175804480751)( qr[6], qr[9] ))
circuit.append(Gates.CU1Gate(4.388257530988808)( qr[3], qr[6] ))
circuit.append(Gates.CYGate( qr[5], qr[9] ))
circuit.append(Gates.RYGate(4.206888046259435)( qr[1] ))
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













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

