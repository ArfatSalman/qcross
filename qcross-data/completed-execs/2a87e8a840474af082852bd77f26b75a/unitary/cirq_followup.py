
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_80e8e5 = Symbol('p_80e8e5')
p_d391ad = Symbol('p_d391ad')
p_58cdd0 = Symbol('p_58cdd0')
p_899200 = Symbol('p_899200')
p_ff62da = Symbol('p_ff62da')
p_5b5ed2 = Symbol('p_5b5ed2')
p_4c1552 = Symbol('p_4c1552')
p_118d87 = Symbol('p_118d87')
p_683b64 = Symbol('p_683b64')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_683b64)( qr[3] ))
circuit.append(Gates.CRZGate(p_58cdd0)( qr[6], qr[3] ))
circuit.append(Gates.CRXGate(p_5b5ed2)( qr[1], qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(p_d391ad)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(p_4c1552)( qr[1] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[4], qr[8] ))
circuit.append(Gates.CCXGate( qr[4], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[7], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CRZGate(p_899200)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_118d87, p_ff62da)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[9] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.RZGate(p_80e8e5)( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))



circuit = cirq.resolve_parameters(circuit, {
    "p_80e8e5": 5.014941143947427,
    "p_d391ad": 4.167661441102218,
    "p_58cdd0": 4.2641612072511235,
    "p_899200": 2.586208953975239,
    "p_ff62da": 2.1276323672732023,
    "p_5b5ed2": 5.987304452123941,
    "p_4c1552": 4.229610589867865,
    "p_118d87": 2.5163050709890156,
    "p_683b64": 6.163759533339787
}, recursive=True)
        

UNITARY = cirq.unitary(circuit)








simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

