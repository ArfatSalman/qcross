
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_dda1d3 = Symbol('p_dda1d3')
p_ce61f1 = Symbol('p_ce61f1')
p_d9b1ff = Symbol('p_d9b1ff')
p_98dc6e = Symbol('p_98dc6e')
p_e3b9a1 = Symbol('p_e3b9a1')
p_1bb590 = Symbol('p_1bb590')
p_ac58f5 = Symbol('p_ac58f5')
p_a8532b = Symbol('p_a8532b')
p_42b602 = Symbol('p_42b602')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_a8532b)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_dda1d3)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_1bb590)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_42b602, 4.167661441102218, p_98dc6e, p_d9b1ff)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(p_ce61f1)( qr[1] ))
circuit.append(Gates.RYYGate(p_e3b9a1)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(5.887184334931191, p_ac58f5, 1.4112277317699358)( qr[4] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RYYGate(0.5501056885328758)( qr[3], qr[0] ))
subcircuit.append(Gates.SXdgGate( qr[3] ))
subcircuit.append(Gates.CRXGate(3.401136029677084)( qr[1], qr[2] ))
subcircuit.append(Gates.RYYGate(0.6724371252296606)( qr[0], qr[4] ))
subcircuit.append(Gates.SdgGate( qr[0] ))
subcircuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_dda1d3": 2.0099472182748075,
    "p_ce61f1": 4.229610589867865,
    "p_d9b1ff": 3.865496458458116,
    "p_98dc6e": 4.623446645668956,
    "p_e3b9a1": 5.398622178940033,
    "p_1bb590": 1.0296448789776642,
    "p_ac58f5": 0.07157463504881167,
    "p_a8532b": 6.163759533339787,
    "p_42b602": 5.708725119517347
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

