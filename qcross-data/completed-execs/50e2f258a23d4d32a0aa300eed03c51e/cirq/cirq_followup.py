
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_7268fa = Symbol('p_7268fa')
p_1ced18 = Symbol('p_1ced18')
p_943f31 = Symbol('p_943f31')
p_7168a9 = Symbol('p_7168a9')
p_d46b4e = Symbol('p_d46b4e')
p_cc0d68 = Symbol('p_cc0d68')
p_a7ec6e = Symbol('p_a7ec6e')
p_a346be = Symbol('p_a346be')
p_165b3b = Symbol('p_165b3b')
p_ea9bf0 = Symbol('p_ea9bf0')
p_e30407 = Symbol('p_e30407')
p_29d856 = Symbol('p_29d856')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_7268fa)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.SwapGate( qr[4], qr[0] ))
subcircuit.append(Gates.CRYGate(3.1402006997068588)( qr[2], qr[0] ))
subcircuit.append(Gates.CUGate(5.0063780207098425, 3.1562533916051736, 4.940217775579305, 2.419481683937988)( qr[2], qr[1] ))
subcircuit.append(Gates.C3XGate(2.6687018103754414)( qr[3], qr[4], qr[2], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_cc0d68)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_d46b4e)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(p_165b3b)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_943f31, p_1ced18, p_a7ec6e, p_e30407)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.RYYGate(p_29d856)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_7168a9)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_ea9bf0, p_a346be, 1.4112277317699358)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_7268fa": 6.163759533339787,
    "p_1ced18": 4.167661441102218,
    "p_943f31": 5.708725119517347,
    "p_7168a9": 3.2142159669963557,
    "p_d46b4e": 1.0296448789776642,
    "p_cc0d68": 2.0099472182748075,
    "p_a7ec6e": 4.623446645668956,
    "p_a346be": 0.07157463504881167,
    "p_165b3b": 1.6723037552953224,
    "p_ea9bf0": 5.887184334931191,
    "p_e30407": 3.865496458458116,
    "p_29d856": 5.398622178940033
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

