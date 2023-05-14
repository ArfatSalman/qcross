
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr_1 = [cirq.NamedQubit('q' + str(i)) for i in range(1)]



qc_1 = cirq.Circuit()

qc_1.append(Gates.ZGate( qr_1[0] ))
qc_1.append(Gates.TGate( qr_1[0] ))
qc_1.append(Gates.SXdgGate( qr_1[0] ))
qc_1.append(cirq.measure(qr_1[0], key='cr0'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result_1 = simulator.run(qc_1, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_1, keys=['cr0'])

RESULT_1 = counts




# Circuit 2

            

qr_2 = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



qc_2 = cirq.Circuit()

qc_2.append(Gates.RZGate(6.163759533339787)( qr_2[2] ))
qc_2.append(Gates.CRZGate(4.2641612072511235)( qr_2[5], qr_2[1] ))
qc_2.append(Gates.CCXGate( qr_2[4], qr_2[8], qr_2[6] ))
qc_2.append(Gates.ZGate( qr_2[1] ))
qc_2.append(Gates.XGate( qr_2[6] ))
qc_2.append(Gates.RCCXGate( qr_2[9], qr_2[5], qr_2[7] ))
qc_2.append(Gates.RZGate(4.229610589867865)( qr_2[0] ))
qc_2.append(Gates.CCXGate( qr_2[6], qr_2[9], qr_2[1] ))
qc_2.append(Gates.SdgGate( qr_2[6] ))
qc_2.append(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( qr_2[9] ))
qc_2.append(Gates.CSXGate( qr_2[2], qr_2[1] ))
qc_2.append(Gates.CHGate( qr_2[0], qr_2[6] ))
qc_2.append(Gates.CU1Gate(4.028174522740928)( qr_2[8], qr_2[0] ))
qc_2.append(Gates.RZGate(5.0063780207098425)( qr_2[5] ))
qc_2.append(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( qr_2[1] ))
qc_2.append(Gates.TGate( qr_2[0] ))
qc_2.append(Gates.RZZGate(3.950837470808744)( qr_2[3], qr_2[0] ))
qc_2.append(Gates.TGate( qr_2[0] ))
qc_2.append(Gates.SXdgGate( qr_2[4] ))
qc_2.append(Gates.RZGate(4.722103101046168)( qr_2[1] ))
qc_2.append(Gates.CRZGate(0.6393443962862078)( qr_2[4], qr_2[2] ))
qc_2.append(Gates.CU1Gate(2.5476776328466872)( qr_2[2], qr_2[7] ))
qc_2.append(Gates.RZGate(3.6614081973587154)( qr_2[5] ))
qc_2.append(cirq.measure(qr_2[0], key='cr0'))
qc_2.append(cirq.measure(qr_2[1], key='cr1'))
qc_2.append(cirq.measure(qr_2[2], key='cr2'))
qc_2.append(cirq.measure(qr_2[3], key='cr3'))
qc_2.append(cirq.measure(qr_2[4], key='cr4'))
qc_2.append(cirq.measure(qr_2[5], key='cr5'))
qc_2.append(cirq.measure(qr_2[6], key='cr6'))
qc_2.append(cirq.measure(qr_2[7], key='cr7'))
qc_2.append(cirq.measure(qr_2[8], key='cr8'))
qc_2.append(cirq.measure(qr_2[9], key='cr9'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result_2 = simulator.run(qc_2, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_2, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from qcross.utils import display_results
    for i in RESULT:
        display_results( {"result": i })


