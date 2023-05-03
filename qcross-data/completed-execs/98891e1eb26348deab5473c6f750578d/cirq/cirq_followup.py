
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



circuit = cirq.Circuit()

circuit.append(Gates.CRYGate(1.075739919522674)( qr[8], qr[2] ))
circuit.append(Gates.RC3XGate( qr[6], qr[2], qr[5], qr[3] ))
circuit.append(Gates.CRZGate(1.6326010370730453)( qr[1], qr[8] ))
circuit.append(Gates.CRZGate(6.113712295160513)( qr[0], qr[1] ))
circuit.append(Gates.UGate(1.4807775550519449, 4.708394834982332, 5.108906631758365)( qr[6] ))
circuit.append(Gates.CU3Gate(1.445874138242965, 0.4812746367052968, 1.4437703311652539)( qr[2], qr[6] ))
circuit.append(Gates.U1Gate(1.55032177844381)( qr[2] ))
circuit.append(Gates.RZZGate(0.023161113352440612)( qr[2], qr[6] ))
circuit.append(Gates.C3XGate( qr[5], qr[2], qr[3], qr[8] ))
circuit.append(Gates.C3XGate( qr[3], qr[8], qr[0], qr[1] ))
circuit.append(Gates.U1Gate(5.302777250135231)( qr[3] ))
circuit.append(Gates.UGate(1.7927964637983416, 0.8353911218777099, 1.5856512163121241)( qr[1] ))
circuit.append(Gates.CU3Gate(4.746133300531744, 4.497432396200483, 4.25035932691423)( qr[8], qr[5] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.HGate( qr[5] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.PhaseGate(4.466750388800541)( qr[8] ))
circuit.append(Gates.HGate( qr[7] ))
circuit.append(Gates.SwapGate( qr[5], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
