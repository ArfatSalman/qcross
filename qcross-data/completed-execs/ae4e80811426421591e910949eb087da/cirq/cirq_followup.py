
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[2] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[0], qr[2] ))
circuit.append(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941)( qr[0], qr[4] ))
circuit.append(Gates.C3SXGate( qr[5], qr[2], qr[1], qr[0] ))
circuit.append(Gates.CCXGate( qr[5], qr[3], qr[1] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[3], qr[1] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[3], qr[4], qr[2] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[5], qr[3] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[5] ))
circuit.append(Gates.C3SXGate( qr[1], qr[0], qr[5], qr[4] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[4], qr[1] ))
circuit.append(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( qr[3] ))
circuit.append(Gates.RZZGate(5.1829934776392745)( qr[1], qr[3] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CRZGate(4.833923139882297)( qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(4.028174522740928)( qr[5], qr[2] ))
circuit.append(Gates.C3SXGate( qr[4], qr[1], qr[2], qr[0] ))
circuit.append(Gates.CRZGate(2.586208953975239)( qr[0], qr[3] ))
circuit.append(Gates.CRXGate(2.6687018103754414)( qr[2], qr[3] ))
circuit.append(Gates.CRZGate(5.742126321682921)( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[1], key='cr0'))
circuit.append(cirq.measure(qr[5], key='cr1'))
circuit.append(cirq.measure(qr[0], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[2], key='cr4'))
circuit.append(cirq.measure(qr[3], key='cr5'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

