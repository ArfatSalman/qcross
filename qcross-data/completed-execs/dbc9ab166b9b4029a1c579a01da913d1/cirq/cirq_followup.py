
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

p_c69e12 = Symbol('p_c69e12')
p_23fe7b = Symbol('p_23fe7b')
p_3b83fb = Symbol('p_3b83fb')
p_d5ab30 = Symbol('p_d5ab30')
p_9f1173 = Symbol('p_9f1173')
p_8cc75e = Symbol('p_8cc75e')
p_ed89c2 = Symbol('p_ed89c2')
p_f1fd0a = Symbol('p_f1fd0a')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_f1fd0a)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[2], qr[5] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.TGate( qr[0] ))
subcircuit.append(Gates.IGate( qr[3] ))
subcircuit.append(Gates.PhaseGate(0.4827903095199283)( qr[6] ))
subcircuit.append(Gates.RZGate(1.2484842640635918)( qr[0] ))
subcircuit.append(Gates.CRZGate(4.747288222618085)( qr[1], qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.C3SXGate( qr[6], qr[0], qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[4], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[6], qr[3] ))
circuit.append(Gates.SdgGate( qr[6] ))
circuit.append(Gates.RCCXGate( qr[2], qr[5], qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RZGate(p_9f1173)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_d5ab30)( qr[4], qr[6] ))
circuit.append(Gates.CHGate( qr[4], qr[0] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[3], qr[4] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.CRZGate(p_3b83fb)( qr[0], qr[6] ))
circuit.append(Gates.CU1Gate(p_8cc75e)( qr[1], qr[4] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[5], qr[4] ))
circuit.append(Gates.CRZGate(p_23fe7b)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_c69e12, p_ed89c2)( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_c69e12": 2.5163050709890156,
    "p_23fe7b": 2.586208953975239,
    "p_3b83fb": 4.833923139882297,
    "p_d5ab30": 5.94477504571567,
    "p_9f1173": 4.229610589867865,
    "p_8cc75e": 4.028174522740928,
    "p_ed89c2": 2.1276323672732023,
    "p_f1fd0a": 6.163759533339787
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

