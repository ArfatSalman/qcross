
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[2] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.U3Gate(2.6397681660693015, 5.320621737498446, 3.427505621225153)( qr[2] ))
subcircuit.append(Gates.RYYGate(6.033961191253911)( qr[0], qr[2] ))
subcircuit.append(Gates.CU3Gate(6.086884486572108, 3.06538533241841, 1.7532443887147882)( qr[0], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.iSwapGate( qr[0], qr[2] ))
circuit.append(Gates.CSXGate( qr[2], qr[1] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[1], qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(cirq.measure(qr[1], key='cr0'))
circuit.append(cirq.measure(qr[2], key='cr1'))
circuit.append(cirq.measure(qr[0], key='cr2'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

