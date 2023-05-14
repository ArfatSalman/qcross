
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr_1 = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



qc_1 = cirq.Circuit()

qc_1.append(Gates.RZGate(6.163759533339787)( qr_1[1] ))
qc_1.append(Gates.ZGate( qr_1[0] ))
qc_1.append(cirq.measure(qr_1[0], key='cr0'))
qc_1.append(cirq.measure(qr_1[1], key='cr1'))
qc_1.append(cirq.measure(qr_1[2], key='cr2'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result_1 = simulator.run(qc_1, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_1, keys=['cr0', 'cr1', 'cr2'])

RESULT_1 = counts




# Circuit 2

            

qr_2 = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



qc_2 = cirq.Circuit()

qc_2.append(Gates.ZGate( qr_2[3] ))
qc_2.append(Gates.XGate( qr_2[3] ))
qc_2.append(Gates.CRXGate(5.987304452123941)( qr_2[0], qr_2[3] ))
qc_2.append(Gates.CRZGate(1.0296448789776642)( qr_2[1], qr_2[3] ))
qc_2.append(Gates.C3SXGate( qr_2[0], qr_2[4], qr_2[3], qr_2[2] ))
qc_2.append(cirq.measure(qr_2[0], key='cr0'))
qc_2.append(cirq.measure(qr_2[1], key='cr1'))
qc_2.append(cirq.measure(qr_2[2], key='cr2'))
qc_2.append(cirq.measure(qr_2[3], key='cr3'))
qc_2.append(cirq.measure(qr_2[4], key='cr4'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result_2 = simulator.run(qc_2, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_2, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from qcross.utils import display_results
    for i in RESULT:
        display_results( {"result": i })


