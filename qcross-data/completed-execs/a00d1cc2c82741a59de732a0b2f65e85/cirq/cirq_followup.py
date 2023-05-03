
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_1b0063 = Symbol('p_1b0063')
p_43b9a6 = Symbol('p_43b9a6')
p_831b02 = Symbol('p_831b02')
p_0584aa = Symbol('p_0584aa')
p_40c0da = Symbol('p_40c0da')
p_d34f58 = Symbol('p_d34f58')
p_aed827 = Symbol('p_aed827')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_831b02)( qr[3] ))
circuit.append(Gates.CRZGate(p_0584aa)( qr[6], qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZXGate(1.1412693567569159)( qr[1], qr[8] ))
subcircuit.append(Gates.SwapGate( qr[1], qr[7] ))
subcircuit.append(Gates.iSwapGate( qr[2], qr[7] ))
subcircuit.append(Gates.RCCXGate( qr[2], qr[0], qr[5] ))
subcircuit.append(Gates.CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004)( qr[3], qr[1] ))
subcircuit.append(Gates.CXGate( qr[8], qr[9] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRXGate(p_d34f58)( qr[1], qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(p_43b9a6)( qr[1] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[4], qr[8] ))
circuit.append(Gates.CCXGate( qr[4], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[7], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CRZGate(p_1b0063)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_aed827, p_40c0da)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[9] ))
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
    "p_1b0063": 2.586208953975239,
    "p_43b9a6": 4.229610589867865,
    "p_831b02": 6.163759533339787,
    "p_0584aa": 4.2641612072511235,
    "p_40c0da": 2.1276323672732023,
    "p_d34f58": 5.987304452123941,
    "p_aed827": 2.5163050709890156
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

