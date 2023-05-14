
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr_1 = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



qc_1 = cirq.Circuit()

qc_1.append(Gates.RZGate(6.163759533339787)( qr_1[1] ))
qc_1.append(Gates.CRZGate(4.2641612072511235)( qr_1[3], qr_1[1] ))
qc_1.append(Gates.CRXGate(5.987304452123941)( qr_1[0], qr_1[4] ))
qc_1.append(Gates.CCXGate( qr_1[2], qr_1[5], qr_1[4] ))
qc_1.append(Gates.ZGate( qr_1[6] ))
qc_1.append(Gates.TGate( qr_1[5] ))
qc_1.append(Gates.CRZGate(4.167661441102218)( qr_1[0], qr_1[3] ))
qc_1.append(cirq.measure(qr_1[0], key='cr0'))
qc_1.append(cirq.measure(qr_1[1], key='cr1'))
qc_1.append(cirq.measure(qr_1[2], key='cr2'))
qc_1.append(cirq.measure(qr_1[3], key='cr3'))
qc_1.append(cirq.measure(qr_1[4], key='cr4'))
qc_1.append(cirq.measure(qr_1[5], key='cr5'))
qc_1.append(cirq.measure(qr_1[6], key='cr6'))
qc_1.append(cirq.measure(qr_1[7], key='cr7'))
qc_1.append(cirq.measure(qr_1[8], key='cr8'))









qasm_output = cirq.qasm(cirq.expand_composite(qc_1))
qc_1 = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result_1 = simulator.run(qc_1, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_1, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0'])

RESULT_1 = counts




# Circuit 2

            

qr_2 = [cirq.NamedQubit('q' + str(i)) for i in range(1)]



qc_2 = cirq.Circuit()

qc_2.append(Gates.XGate( qr_2[0] ))
qc_2.append(cirq.measure(qr_2[0], key='cr0'))









qasm_output = cirq.qasm(cirq.expand_composite(qc_2))
qc_2 = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result_2 = simulator.run(qc_2, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_2, keys=['m_cr0_0'])

RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from qcross.utils import display_results
    for i in RESULT:
        display_results( {"result": i })


