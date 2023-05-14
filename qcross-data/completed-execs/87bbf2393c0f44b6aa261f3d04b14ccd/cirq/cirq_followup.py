
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_f80351 = Symbol('p_f80351')
p_cb603f = Symbol('p_cb603f')
p_9a6428 = Symbol('p_9a6428')
p_14882b = Symbol('p_14882b')
p_229656 = Symbol('p_229656')
p_d83aa6 = Symbol('p_d83aa6')
p_1e7763 = Symbol('p_1e7763')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_1e7763)( qr[3] ))
circuit.append(Gates.CRZGate(p_cb603f)( qr[6], qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.SXdgGate( qr[5] ))
subcircuit.append(Gates.DCXGate( qr[4], qr[7] ))
subcircuit.append(Gates.CU3Gate(4.2220417977098705, 1.672427069032094, 2.447994042088217)( qr[5], qr[3] ))
subcircuit.append(Gates.CUGate(4.783709962939332, 4.509839071764646, 3.631024984774394, 2.3799139963609854)( qr[7], qr[3] ))
subcircuit.append(Gates.PhaseGate(5.949169145894372)( qr[2] ))
subcircuit.append(Gates.CSXGate( qr[1], qr[7] ))
subcircuit.append(Gates.CXGate( qr[2], qr[5] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRXGate(5.987304452123941)( qr[1], qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(p_229656)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[4], qr[8] ))
circuit.append(Gates.CCXGate( qr[4], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[7], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CRZGate(p_9a6428)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_14882b, p_d83aa6)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[9] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.RZGate(5.014941143947427)( qr[1] ))
circuit.append(Gates.CRXGate(p_f80351)( qr[7], qr[1] ))
circuit.append(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( qr[2] ))
circuit.append(Gates.ECRGate( qr[4], qr[8] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.ZGate( qr[8] ))
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
    "p_f80351": 5.970852306777193,
    "p_cb603f": 4.2641612072511235,
    "p_9a6428": 2.586208953975239,
    "p_14882b": 2.5163050709890156,
    "p_229656": 4.167661441102218,
    "p_d83aa6": 2.1276323672732023,
    "p_1e7763": 6.163759533339787
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

