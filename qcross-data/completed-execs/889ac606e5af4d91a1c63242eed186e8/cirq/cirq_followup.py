
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_e4a82b = Symbol('p_e4a82b')
p_897fa0 = Symbol('p_897fa0')
p_4c8c10 = Symbol('p_4c8c10')
p_42a1d4 = Symbol('p_42a1d4')
p_b41b47 = Symbol('p_b41b47')
p_f7f517 = Symbol('p_f7f517')
p_3d4bf9 = Symbol('p_3d4bf9')
p_258753 = Symbol('p_258753')
p_a5e20b = Symbol('p_a5e20b')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.CRZGate(p_42a1d4)( qr[6], qr[3] ))
circuit.append(Gates.CRXGate(p_258753)( qr[1], qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(p_a5e20b)( qr[1] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[4], qr[8] ))
circuit.append(Gates.CCXGate( qr[4], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[7], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CRZGate(p_f7f517)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_b41b47, p_4c8c10)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[9] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.RZGate(p_e4a82b)( qr[1] ))
circuit.append(Gates.CRXGate(5.970852306777193)( qr[7], qr[1] ))
circuit.append(Gates.UGate(p_897fa0, p_3d4bf9, 2.271164628944128)( qr[2] ))
circuit.append(Gates.ECRGate( qr[4], qr[8] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.ZGate( qr[8] ))
circuit.append(Gates.CSXGate( qr[1], qr[7] ))
circuit.append(Gates.RZGate(3.6614081973587154)( qr[5] ))
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
    "p_e4a82b": 5.014941143947427,
    "p_897fa0": 5.080799300534071,
    "p_4c8c10": 2.1276323672732023,
    "p_42a1d4": 4.2641612072511235,
    "p_b41b47": 2.5163050709890156,
    "p_f7f517": 2.586208953975239,
    "p_3d4bf9": 5.023617931957853,
    "p_258753": 5.987304452123941,
    "p_a5e20b": 4.229610589867865
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0', 'm_cr9_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

