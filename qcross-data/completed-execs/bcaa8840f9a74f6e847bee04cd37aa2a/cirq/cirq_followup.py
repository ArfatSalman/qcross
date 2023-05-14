
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

p_42891c = Symbol('p_42891c')
p_92144e = Symbol('p_92144e')
p_cbf8a5 = Symbol('p_cbf8a5')
p_9f3b29 = Symbol('p_9f3b29')
p_914ffd = Symbol('p_914ffd')
p_155411 = Symbol('p_155411')
p_4ab831 = Symbol('p_4ab831')
p_e5e350 = Symbol('p_e5e350')

circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.SXGate( qr[1] ))
subcircuit.append(Gates.SXGate( qr[1] ))
subcircuit.append(Gates.RYGate(5.398622178940033)( qr[0] ))
subcircuit.append(Gates.XGate( qr[0] ))
subcircuit.append(Gates.CU3Gate(1.3471739101750193, 3.2142159669963557, 2.852678572380205)( qr[0], qr[1] ))
subcircuit.append(Gates.U1Gate(2.3568871696687452)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZZGate(6.163759533339787)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_92144e)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRXGate(p_e5e350)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CRZGate(p_4ab831)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(p_914ffd)( qr[1] ))
circuit.append(Gates.RZGate(5.512260524440591)( qr[1] ))
circuit.append(Gates.CU1Gate(p_155411)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RZZGate(6.086884486572108)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.RYYGate(p_42891c)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(p_9f3b29)( qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_cbf8a5)( qr[1], qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))



circuit = cirq.resolve_parameters(circuit, {
    "p_42891c": 3.3705408413231095,
    "p_92144e": 1.977559237989846,
    "p_cbf8a5": 5.167261531657622,
    "p_9f3b29": 5.190931186022931,
    "p_914ffd": 5.320621737498446,
    "p_155411": 1.6723037552953224,
    "p_4ab831": 2.2498881927557752,
    "p_e5e350": 5.987304452123941
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

