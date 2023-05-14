
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_01ce9b = Symbol('p_01ce9b')
p_4f7ff2 = Symbol('p_4f7ff2')
p_17defe = Symbol('p_17defe')
p_e7ae71 = Symbol('p_e7ae71')
p_17befe = Symbol('p_17befe')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_4f7ff2)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_17defe)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_e7ae71, p_17befe, 2.3864521352475245, p_01ce9b)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.U1Gate(6.2047416485134805)( qr[0] ))
subcircuit.append(Gates.CPhaseGate(4.63837786161633)( qr[0], qr[2] ))
subcircuit.append(Gates.RZXGate(4.563562108824195)( qr[4], qr[0] ))
subcircuit.append(Gates.C3XGate(5.94477504571567)( qr[4], qr[5], qr[2], qr[1] ))
subcircuit.append(Gates.XGate( qr[4] ))
subcircuit.append(Gates.CYGate( qr[2], qr[0] ))
subcircuit.append(Gates.SXGate( qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_01ce9b": 5.987304452123941,
    "p_4f7ff2": 6.163759533339787,
    "p_17defe": 4.2641612072511235,
    "p_e7ae71": 0.5112149185250571,
    "p_17befe": 5.897054719225356
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

