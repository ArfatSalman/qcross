
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_b6dd52 = Symbol('p_b6dd52')
p_02ac66 = Symbol('p_02ac66')
p_f623a3 = Symbol('p_f623a3')
p_57e546 = Symbol('p_57e546')
p_e01555 = Symbol('p_e01555')
p_3851a3 = Symbol('p_3851a3')
p_736182 = Symbol('p_736182')
p_8b193d = Symbol('p_8b193d')
p_0d1cd9 = Symbol('p_0d1cd9')
p_5da4d4 = Symbol('p_5da4d4')
p_414184 = Symbol('p_414184')
p_2096e5 = Symbol('p_2096e5')
p_b24006 = Symbol('p_b24006')
p_304e0e = Symbol('p_304e0e')
p_d9a218 = Symbol('p_d9a218')
p_8522da = Symbol('p_8522da')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_3851a3)( qr[2] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(p_2096e5)( qr[1], qr[2] ))
circuit.append(Gates.CUGate(p_f623a3, 5.897054719225356, p_57e546, p_b24006)( qr[1], qr[4] ))
circuit.append(Gates.C3SXGate( qr[3], qr[2], qr[0], qr[1] ))
circuit.append(Gates.CCXGate( qr[3], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[5], qr[4], qr[2] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(p_d9a218)( qr[3], qr[5] ))
circuit.append(Gates.RZGate(p_8b193d)( qr[3] ))
circuit.append(Gates.C3SXGate( qr[0], qr[1], qr[3], qr[4] ))
circuit.append(Gates.CU1Gate(p_e01555)( qr[4], qr[0] ))
circuit.append(Gates.UGate(p_736182, p_5da4d4, p_304e0e)( qr[5] ))
circuit.append(Gates.RZZGate(p_02ac66)( qr[0], qr[5] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CRZGate(p_414184)( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(p_b6dd52)( qr[3], qr[2] ))
circuit.append(Gates.C3SXGate( qr[4], qr[0], qr[2], qr[1] ))
circuit.append(Gates.CRZGate(p_8522da)( qr[1], qr[5] ))
circuit.append(Gates.CRXGate(p_0d1cd9)( qr[2], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[3], key='cr1'))
circuit.append(cirq.measure(qr[1], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[2], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_b6dd52": 4.028174522740928,
    "p_02ac66": 5.1829934776392745,
    "p_f623a3": 0.5112149185250571,
    "p_57e546": 2.3864521352475245,
    "p_e01555": 3.2142159669963557,
    "p_3851a3": 6.163759533339787,
    "p_736182": 5.887184334931191,
    "p_8b193d": 4.229610589867865,
    "p_0d1cd9": 2.6687018103754414,
    "p_5da4d4": 0.07157463504881167,
    "p_414184": 4.833923139882297,
    "p_2096e5": 4.2641612072511235,
    "p_b24006": 5.987304452123941,
    "p_304e0e": 1.4112277317699358,
    "p_d9a218": 4.167661441102218,
    "p_8522da": 2.586208953975239
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

