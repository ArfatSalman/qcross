
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

p_53e66c = Symbol('p_53e66c')
p_6b5eeb = Symbol('p_6b5eeb')
p_c550ed = Symbol('p_c550ed')
p_1bf9a6 = Symbol('p_1bf9a6')
p_71ceaf = Symbol('p_71ceaf')
p_3b8ed5 = Symbol('p_3b8ed5')
p_34c784 = Symbol('p_34c784')
p_dc073a = Symbol('p_dc073a')

circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(6.163759533339787)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_53e66c)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRXGate(p_34c784)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CRZGate(p_dc073a)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(p_6b5eeb)( qr[1] ))
circuit.append(Gates.RZGate(p_c550ed)( qr[1] ))
circuit.append(Gates.CU1Gate(p_71ceaf)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RZZGate(p_3b8ed5)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.RYYGate(p_1bf9a6)( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))



circuit = cirq.resolve_parameters(circuit, {
    "p_53e66c": 1.977559237989846,
    "p_6b5eeb": 5.320621737498446,
    "p_c550ed": 5.512260524440591,
    "p_1bf9a6": 3.3705408413231095,
    "p_71ceaf": 1.6723037552953224,
    "p_3b8ed5": 6.086884486572108,
    "p_34c784": 5.987304452123941,
    "p_dc073a": 2.2498881927557752
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

