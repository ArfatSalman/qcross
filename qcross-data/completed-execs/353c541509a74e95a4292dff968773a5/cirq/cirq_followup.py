
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_ca4ae7 = Symbol('p_ca4ae7')
p_350212 = Symbol('p_350212')
p_3be268 = Symbol('p_3be268')
p_e86f21 = Symbol('p_e86f21')
p_8cc9b1 = Symbol('p_8cc9b1')
p_09c913 = Symbol('p_09c913')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_ca4ae7)( qr[1] ))
circuit.append(Gates.RZZGate(p_e86f21)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_350212, p_8cc9b1, p_09c913, 5.987304452123941)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(5.154187354656876)( qr[3], qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CXGate( qr[3], qr[0] ))
subcircuit.append(Gates.RZGate(p_3be268)( qr[2] ))
subcircuit.append(Gates.TdgGate( qr[0] ))
subcircuit.append(Gates.HGate( qr[1] ))
subcircuit.append(Gates.CU1Gate(4.229610589867865)( qr[1], qr[3] ))
subcircuit.append(Gates.ECRGate( qr[1], qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_ca4ae7": 6.163759533339787,
    "p_350212": 0.5112149185250571,
    "p_3be268": 3.8580685613059242,
    "p_e86f21": 4.066449154047175,
    "p_8cc9b1": 5.897054719225356,
    "p_09c913": 2.3864521352475245
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

