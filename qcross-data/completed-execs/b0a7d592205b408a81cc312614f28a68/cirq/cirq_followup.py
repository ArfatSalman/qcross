
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

p_8f5281 = Symbol('p_8f5281')
p_39dba4 = Symbol('p_39dba4')
p_5f2994 = Symbol('p_5f2994')
p_b6dc31 = Symbol('p_b6dc31')
p_078f44 = Symbol('p_078f44')
p_7ad57d = Symbol('p_7ad57d')
p_bb9f8c = Symbol('p_bb9f8c')
p_31d873 = Symbol('p_31d873')
p_ab882a = Symbol('p_ab882a')
p_3d1a45 = Symbol('p_3d1a45')
p_14147f = Symbol('p_14147f')
p_584aac = Symbol('p_584aac')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_bb9f8c)( qr[8] ))
circuit.append(Gates.CSXGate( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_8f5281, p_b6dc31, p_ab882a, p_31d873)( qr[0], qr[6] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[8], qr[7], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[5] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.SGate( qr[8] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[2], qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_078f44)( qr[8], qr[3] ))
circuit.append(Gates.CRZGate(p_7ad57d)( qr[5], qr[8] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CSwapGate( qr[0], qr[6], qr[5] ))
subcircuit.append(Gates.CSXGate( qr[6], qr[1] ))
subcircuit.append(Gates.SXGate( qr[3] ))
subcircuit.append(Gates.SXdgGate( qr[6] ))
subcircuit.append(Gates.RYYGate(p_3d1a45)( qr[0], qr[4] ))
subcircuit.append(Gates.iSwapGate( qr[5], qr[7] ))
subcircuit.append(Gates.UGate(p_39dba4, p_14147f, p_5f2994)( qr[3] ))
subcircuit.append(Gates.PhaseGate(p_584aac)( qr[8] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))



circuit = cirq.resolve_parameters(circuit, {
    "p_8f5281": 0.5112149185250571,
    "p_39dba4": 2.438459595578943,
    "p_5f2994": 3.4232119351142516,
    "p_b6dc31": 5.897054719225356,
    "p_078f44": 3.2142159669963557,
    "p_7ad57d": 1.4112277317699358,
    "p_bb9f8c": 6.163759533339787,
    "p_31d873": 5.987304452123941,
    "p_ab882a": 2.3864521352475245,
    "p_3d1a45": 0.6724371252296606,
    "p_14147f": 3.326780904591333,
    "p_584aac": 0.4827903095199283
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

