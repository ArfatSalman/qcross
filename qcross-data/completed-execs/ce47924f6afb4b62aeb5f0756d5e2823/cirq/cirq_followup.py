
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[4], qr[2] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[3], qr[2] ))
circuit.append(Gates.C3SXGate( qr[4], qr[1], qr[2], qr[5] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[2], qr[1] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[3], qr[1] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[3] ))
circuit.append(Gates.SXGate( qr[4] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[7], qr[4] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[2], qr[7] ))
circuit.append(Gates.RZZGate(5.1829934776392745)( qr[1], qr[4] ))
circuit.append(Gates.CSXGate( qr[4], qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.RZGate(3.775592041307464)( qr[7] ))
circuit.append(Gates.CRXGate(0.7279391018916035)( qr[4], qr[5] ))
circuit.append(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305)( qr[2], qr[0] ))
circuit.append(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( qr[0] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SdgGate( qr[4] ))
circuit.append(Gates.RZZGate(3.950837470808744)( qr[5], qr[7] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.RYYGate(1.9669252191306448)( qr[7], qr[0] ))
circuit.append(Gates.C3SXGate( qr[3], qr[5], qr[0], qr[6] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( qr[0] ))
circuit.append(cirq.measure(qr[4], key='cr0'))
circuit.append(cirq.measure(qr[3], key='cr1'))
circuit.append(cirq.measure(qr[0], key='cr2'))
circuit.append(cirq.measure(qr[5], key='cr3'))
circuit.append(cirq.measure(qr[7], key='cr4'))
circuit.append(cirq.measure(qr[6], key='cr5'))
circuit.append(cirq.measure(qr[2], key='cr6'))
circuit.append(cirq.measure(qr[1], key='cr7'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

