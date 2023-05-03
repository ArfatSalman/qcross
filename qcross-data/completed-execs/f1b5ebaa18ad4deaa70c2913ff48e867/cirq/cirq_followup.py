
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[9], qr[4] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.TdgGate( qr[2] ))
subcircuit.append(Gates.CYGate( qr[5], qr[2] ))
subcircuit.append(Gates.SXGate( qr[8] ))
subcircuit.append(Gates.CRZGate(2.008796895454228)( qr[8], qr[6] ))
subcircuit.append(Gates.RCCXGate( qr[3], qr[7], qr[1] ))
subcircuit.append(Gates.RXXGate(5.25962645863375)( qr[2], qr[9] ))
subcircuit.append(Gates.DCXGate( qr[5], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRXGate(5.987304452123941)( qr[7], qr[0] ))
circuit.append(Gates.CCXGate( qr[6], qr[3], qr[0] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[7], qr[9] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[7] ))
circuit.append(Gates.SXGate( qr[5] ))
circuit.append(Gates.CSXGate( qr[2], qr[1] ))
circuit.append(cirq.measure(qr[8], key='cr0'))
circuit.append(cirq.measure(qr[7], key='cr1'))
circuit.append(cirq.measure(qr[5], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[2], key='cr4'))
circuit.append(cirq.measure(qr[6], key='cr5'))
circuit.append(cirq.measure(qr[9], key='cr6'))
circuit.append(cirq.measure(qr[0], key='cr7'))
circuit.append(cirq.measure(qr[1], key='cr8'))
circuit.append(cirq.measure(qr[3], key='cr9'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

