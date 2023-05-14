
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_7f87cd = Symbol('p_7f87cd')
p_6e3856 = Symbol('p_6e3856')
p_cb84fc = Symbol('p_cb84fc')
p_85980f = Symbol('p_85980f')
p_d1f1d7 = Symbol('p_d1f1d7')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_7f87cd)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_cb84fc, 5.897054719225356, 2.3864521352475245, p_85980f)( qr[2], qr[3] ))
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
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( qr[5] ))
circuit.append(Gates.RZZGate(5.1829934776392745)( qr[0], qr[5] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(4.833923139882297)( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(4.028174522740928)( qr[1], qr[4] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[4], qr[2] ))
circuit.append(Gates.CRZGate(p_6e3856)( qr[2], qr[5] ))
circuit.append(Gates.CRXGate(2.6687018103754414)( qr[4], qr[5] ))
circuit.append(Gates.CRZGate(p_d1f1d7)( qr[2], qr[0] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(3.950837470808744)( qr[3], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_7f87cd": 4.2641612072511235,
    "p_6e3856": 2.586208953975239,
    "p_cb84fc": 0.5112149185250571,
    "p_85980f": 5.987304452123941,
    "p_d1f1d7": 5.742126321682921
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

