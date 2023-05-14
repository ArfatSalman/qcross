
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr_1 = [cirq.NamedQubit('q' + str(i)) for i in range(1)]



qc_1 = cirq.Circuit()

qc_1.append(Gates.TGate( qr_1[0] ))
qc_1.append(cirq.measure(qr_1[0], key='cr0'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result_1 = simulator.run(qc_1, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_1, keys=['cr0'])

RESULT_1 = counts




# Circuit 2

            

qr_2 = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



qc_2 = cirq.Circuit()

qc_2.append(Gates.RZGate(6.163759533339787)( qr_2[4] ))
qc_2.append(Gates.ZGate( qr_2[5] ))
qc_2.append(Gates.XGate( qr_2[5] ))
qc_2.append(Gates.CRXGate(5.987304452123941)( qr_2[0], qr_2[5] ))
qc_2.append(Gates.CRZGate(1.0296448789776642)( qr_2[1], qr_2[5] ))
qc_2.append(Gates.C3SXGate( qr_2[0], qr_2[6], qr_2[5], qr_2[3] ))
qc_2.append(Gates.ZGate( qr_2[2] ))
qc_2.append(Gates.XGate( qr_2[1] ))
qc_2.append(Gates.RYYGate(1.740253089260498)( qr_2[5], qr_2[6] ))
qc_2.append(Gates.CRZGate(4.167661441102218)( qr_2[1], qr_2[6] ))
qc_2.append(Gates.RZGate(4.229610589867865)( qr_2[1] ))
qc_2.append(Gates.SXGate( qr_2[0] ))
qc_2.append(Gates.CU1Gate(3.2142159669963557)( qr_2[4], qr_2[0] ))
qc_2.append(Gates.CRXGate(5.94477504571567)( qr_2[5], qr_2[4] ))
qc_2.append(Gates.RZZGate(5.1829934776392745)( qr_2[6], qr_2[0] ))
qc_2.append(Gates.CSXGate( qr_2[0], qr_2[2] ))
qc_2.append(Gates.ZGate( qr_2[5] ))
qc_2.append(Gates.RZGate(3.775592041307464)( qr_2[4] ))
qc_2.append(Gates.CRXGate(0.7279391018916035)( qr_2[0], qr_2[3] ))
qc_2.append(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305)( qr_2[5], qr_2[2] ))
qc_2.append(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( qr_2[2] ))
qc_2.append(Gates.TGate( qr_2[5] ))
qc_2.append(Gates.SdgGate( qr_2[0] ))
qc_2.append(Gates.RZZGate(3.950837470808744)( qr_2[3], qr_2[4] ))
qc_2.append(cirq.measure(qr_2[0], key='cr0'))
qc_2.append(cirq.measure(qr_2[1], key='cr1'))
qc_2.append(cirq.measure(qr_2[2], key='cr2'))
qc_2.append(cirq.measure(qr_2[3], key='cr3'))
qc_2.append(cirq.measure(qr_2[4], key='cr4'))
qc_2.append(cirq.measure(qr_2[5], key='cr5'))
qc_2.append(cirq.measure(qr_2[6], key='cr6'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result_2 = simulator.run(qc_2, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_2, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from qcross.utils import display_results
    for i in RESULT:
        display_results( {"result": i })


