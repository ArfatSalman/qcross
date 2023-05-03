
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[2], qr[1] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[0], qr[1] ))
circuit.append(Gates.C3SXGate( qr[2], qr[6], qr[1], qr[4] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[1], qr[6] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[0], qr[6] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[0] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[1], qr[3] ))
circuit.append(Gates.RZZGate(5.1829934776392745)( qr[6], qr[2] ))
circuit.append(Gates.CSXGate( qr[2], qr[5] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.RZGate(3.775592041307464)( qr[3] ))
circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[0], key='cr1'))
circuit.append(cirq.measure(qr[5], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[3], key='cr4'))
circuit.append(cirq.measure(qr[7], key='cr5'))
circuit.append(cirq.measure(qr[1], key='cr6'))
circuit.append(cirq.measure(qr[6], key='cr7'))













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

