
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_f22bb0 = Symbol('p_f22bb0')
p_c746bf = Symbol('p_c746bf')
p_bd1c3c = Symbol('p_bd1c3c')
p_2c205c = Symbol('p_2c205c')
p_132f3b = Symbol('p_132f3b')
p_72ab38 = Symbol('p_72ab38')
p_d5c708 = Symbol('p_d5c708')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_72ab38)( qr[5] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[0], qr[5] ))
circuit.append(Gates.CRXGate(p_d5c708)( qr[9], qr[3] ))
circuit.append(Gates.CCXGate( qr[6], qr[4], qr[3] ))
circuit.append(Gates.ZGate( qr[8] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CRZGate(p_f22bb0)( qr[9], qr[0] ))
circuit.append(Gates.RZGate(p_132f3b)( qr[9] ))
circuit.append(Gates.SXGate( qr[8] ))
circuit.append(Gates.CSXGate( qr[7], qr[2] ))
circuit.append(Gates.CCXGate( qr[7], qr[4], qr[6] ))
circuit.append(Gates.C3SXGate( qr[8], qr[7], qr[1], qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[8] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CHGate( qr[3], qr[9] ))
circuit.append(Gates.CSXGate( qr[8], qr[1] ))
circuit.append(Gates.CRZGate(p_bd1c3c)( qr[9], qr[8] ))
circuit.append(Gates.U2Gate(2.5163050709890156, p_2c205c)( qr[8] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[4] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.RZGate(p_c746bf)( qr[9] ))
circuit.append(cirq.measure(qr[1], key='cr0'))
circuit.append(cirq.measure(qr[9], key='cr1'))
circuit.append(cirq.measure(qr[8], key='cr2'))
circuit.append(cirq.measure(qr[5], key='cr3'))
circuit.append(cirq.measure(qr[7], key='cr4'))
circuit.append(cirq.measure(qr[6], key='cr5'))
circuit.append(cirq.measure(qr[0], key='cr6'))
circuit.append(cirq.measure(qr[3], key='cr7'))
circuit.append(cirq.measure(qr[2], key='cr8'))
circuit.append(cirq.measure(qr[4], key='cr9'))



circuit = cirq.resolve_parameters(circuit, {
    "p_f22bb0": 4.167661441102218,
    "p_c746bf": 5.014941143947427,
    "p_bd1c3c": 2.586208953975239,
    "p_2c205c": 2.1276323672732023,
    "p_132f3b": 4.229610589867865,
    "p_72ab38": 6.163759533339787,
    "p_d5c708": 5.987304452123941
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

