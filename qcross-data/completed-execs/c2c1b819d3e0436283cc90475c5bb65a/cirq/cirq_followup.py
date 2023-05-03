
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

p_59c694 = Symbol('p_59c694')
p_4da120 = Symbol('p_4da120')
p_bfc32f = Symbol('p_bfc32f')
p_080b1a = Symbol('p_080b1a')
p_6db7be = Symbol('p_6db7be')
p_d86b30 = Symbol('p_d86b30')
p_fdfc00 = Symbol('p_fdfc00')
p_63b789 = Symbol('p_63b789')

circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(p_d86b30)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_bfc32f)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRXGate(p_59c694)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CRZGate(p_63b789)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(p_080b1a)( qr[1] ))
circuit.append(Gates.RZGate(p_fdfc00)( qr[1] ))
circuit.append(Gates.CU1Gate(p_4da120)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RZZGate(p_6db7be)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))



circuit = cirq.resolve_parameters(circuit, {
    "p_59c694": 5.987304452123941,
    "p_4da120": 1.6723037552953224,
    "p_bfc32f": 1.977559237989846,
    "p_080b1a": 5.320621737498446,
    "p_6db7be": 6.086884486572108,
    "p_d86b30": 6.163759533339787,
    "p_fdfc00": 5.512260524440591,
    "p_63b789": 2.2498881927557752
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

