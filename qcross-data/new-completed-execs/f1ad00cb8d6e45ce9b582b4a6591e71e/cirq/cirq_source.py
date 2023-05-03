
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(Gates.CRYGate(0.8476513988624245)( qr[4], qr[0] ))
circuit.append(Gates.CU1Gate(1.5710197357755318)( qr[3], qr[2] ))
circuit.append(Gates.TdgGate( qr[2] ))
circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(Gates.CCZGate( qr[2], qr[1], qr[3] ))
circuit.append(Gates.UGate(0.708502006099043, 2.97765669736744, 5.6444063351584415)( qr[2] ))
circuit.append(Gates.CPhaseGate(5.597667172921795)( qr[3], qr[4] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CRYGate(0.3177314062860099)( qr[4], qr[1] ))
circuit.append(Gates.CU1Gate(1.9730677082046415)( qr[4], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

