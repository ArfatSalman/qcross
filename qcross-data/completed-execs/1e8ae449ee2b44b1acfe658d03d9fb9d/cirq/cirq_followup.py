
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_a0ca5d = Symbol('p_a0ca5d')
p_8b617c = Symbol('p_8b617c')
p_1fce1b = Symbol('p_1fce1b')
p_32ce54 = Symbol('p_32ce54')
p_6530e4 = Symbol('p_6530e4')
p_bcda17 = Symbol('p_bcda17')
p_45f58e = Symbol('p_45f58e')
p_3962ff = Symbol('p_3962ff')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_a0ca5d)( qr[1] ))
circuit.append(Gates.RZZGate(4.066449154047175)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(0.5112149185250571, p_32ce54, p_1fce1b, 5.987304452123941)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_3962ff)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[2], qr[0] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(2.9790366726895714)( qr[0], qr[1] ))
circuit.append(Gates.C3SXGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_bcda17)( qr[0], qr[3] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CRXGate(p_6530e4)( qr[2], qr[0] ))
circuit.append(Gates.U2Gate(p_8b617c, p_45f58e)( qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_a0ca5d": 6.163759533339787,
    "p_8b617c": 4.214504315296764,
    "p_1fce1b": 2.3864521352475245,
    "p_32ce54": 5.897054719225356,
    "p_6530e4": 5.94477504571567,
    "p_bcda17": 3.2142159669963557,
    "p_45f58e": 4.6235667602042065,
    "p_3962ff": 5.154187354656876
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

