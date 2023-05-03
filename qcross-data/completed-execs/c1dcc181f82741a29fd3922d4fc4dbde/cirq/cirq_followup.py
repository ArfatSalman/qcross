
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_752feb = Symbol('p_752feb')
p_2ded38 = Symbol('p_2ded38')
p_5fc981 = Symbol('p_5fc981')
p_636ed6 = Symbol('p_636ed6')
p_c6e6fc = Symbol('p_c6e6fc')
p_8e5ab7 = Symbol('p_8e5ab7')
p_68a976 = Symbol('p_68a976')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_752feb)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(0.5112149185250571, p_636ed6, p_5fc981, 5.987304452123941)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[5] ))
circuit.append(Gates.RZGate(p_68a976)( qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RCCXGate( qr[4], qr[5], qr[1] ))
subcircuit.append(Gates.CRYGate(3.1402006997068588)( qr[3], qr[0] ))
subcircuit.append(Gates.SXdgGate( qr[4] ))
subcircuit.append(Gates.DCXGate( qr[1], qr[2] ))
subcircuit.append(Gates.RYYGate(0.6724371252296606)( qr[0], qr[5] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_2ded38, p_8e5ab7, 1.4112277317699358)( qr[5] ))
circuit.append(Gates.RZZGate(p_c6e6fc)( qr[0], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_752feb": 6.163759533339787,
    "p_2ded38": 5.887184334931191,
    "p_5fc981": 2.3864521352475245,
    "p_636ed6": 5.897054719225356,
    "p_c6e6fc": 5.1829934776392745,
    "p_8e5ab7": 0.07157463504881167,
    "p_68a976": 4.229610589867865
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

