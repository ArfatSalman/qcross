
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_845551 = Symbol('p_845551')
p_1ada4b = Symbol('p_1ada4b')
p_2b124e = Symbol('p_2b124e')
p_f7bbfa = Symbol('p_f7bbfa')
p_f1397b = Symbol('p_f1397b')
p_b60795 = Symbol('p_b60795')
p_505de8 = Symbol('p_505de8')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_b60795)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_2b124e, 5.897054719225356, p_f7bbfa, 5.987304452123941)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[5] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(p_f1397b)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_505de8, 0.07157463504881167, 1.4112277317699358)( qr[5] ))
circuit.append(Gates.RZZGate(p_1ada4b)( qr[0], qr[5] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(4.833923139882297)( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(p_845551)( qr[1], qr[4] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[4], qr[2] ))
circuit.append(Gates.CRZGate(2.586208953975239)( qr[2], qr[5] ))
circuit.append(Gates.CRXGate(2.6687018103754414)( qr[4], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_845551": 4.028174522740928,
    "p_1ada4b": 5.1829934776392745,
    "p_2b124e": 0.5112149185250571,
    "p_f7bbfa": 2.3864521352475245,
    "p_f1397b": 3.2142159669963557,
    "p_b60795": 6.163759533339787,
    "p_505de8": 5.887184334931191
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

