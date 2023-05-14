
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_9c95f7 = Symbol('p_9c95f7')
p_201117 = Symbol('p_201117')
p_3f3854 = Symbol('p_3f3854')
p_eeece4 = Symbol('p_eeece4')
p_8ca533 = Symbol('p_8ca533')
p_47be8d = Symbol('p_47be8d')
p_0c155d = Symbol('p_0c155d')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_201117)( qr[1] ))
circuit.append(Gates.RZZGate(p_3f3854)( qr[2], qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RXXGate(0.2906326206587185)( qr[3], qr[0] ))
subcircuit.append(Gates.ZGate( qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_eeece4, p_0c155d, p_8ca533, p_9c95f7)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_47be8d)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[2], qr[0] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_9c95f7": 5.987304452123941,
    "p_201117": 6.163759533339787,
    "p_3f3854": 4.066449154047175,
    "p_eeece4": 0.5112149185250571,
    "p_8ca533": 2.3864521352475245,
    "p_47be8d": 5.154187354656876,
    "p_0c155d": 5.897054719225356
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

