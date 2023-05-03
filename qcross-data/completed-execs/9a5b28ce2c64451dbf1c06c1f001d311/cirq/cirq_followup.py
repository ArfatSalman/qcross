
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_7d7ce5 = Symbol('p_7d7ce5')
p_7291d9 = Symbol('p_7291d9')
p_f3c89a = Symbol('p_f3c89a')
p_8a1a82 = Symbol('p_8a1a82')
p_922074 = Symbol('p_922074')
p_6c1345 = Symbol('p_6c1345')
p_4bcda6 = Symbol('p_4bcda6')
p_45c2b7 = Symbol('p_45c2b7')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_7291d9)( qr[1] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.iSwapGate( qr[2], qr[1] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.CRXGate(p_922074)( qr[0], qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.RYYGate(p_4bcda6)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RYYGate(p_7d7ce5)( qr[2], qr[0] ))
subcircuit.append(Gates.U1Gate(p_45c2b7)( qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.CRZGate(p_6c1345)( qr[2], qr[1] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CRZGate(p_f3c89a)( qr[2], qr[1] ))
circuit.append(Gates.RYYGate(p_8a1a82)( qr[1], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_7d7ce5": 0.2906326206587185,
    "p_7291d9": 6.163759533339787,
    "p_f3c89a": 0.05525155902669336,
    "p_8a1a82": 3.2287759437031154,
    "p_922074": 5.987304452123941,
    "p_6c1345": 4.167661441102218,
    "p_4bcda6": 1.6723037552953224,
    "p_45c2b7": 1.4447770477048325
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

