
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_78601e = Symbol('p_78601e')
p_91bcc8 = Symbol('p_91bcc8')
p_0a0a4b = Symbol('p_0a0a4b')
p_0ecc7a = Symbol('p_0ecc7a')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_0ecc7a)( qr[1] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.iSwapGate( qr[2], qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.UGate(2.9790366726895714, p_0a0a4b, 3.2287759437031154)( qr[1] ))
subcircuit.append(Gates.SdgGate( qr[1] ))
subcircuit.append(Gates.RYYGate(0.2906326206587185)( qr[2], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.CRXGate(p_91bcc8)( qr[0], qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.CRZGate(p_78601e)( qr[2], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_78601e": 4.167661441102218,
    "p_91bcc8": 5.987304452123941,
    "p_0a0a4b": 5.974354952564585,
    "p_0ecc7a": 6.163759533339787
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

