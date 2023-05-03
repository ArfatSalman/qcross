
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.U3Gate(0.25389907280649565, 2.779350782980329, 4.0325416129476945)( qr[6] ))
circuit.append(Gates.HGate( qr[7] ))
circuit.append(Gates.U1Gate(0.3295500658949094)( qr[9] ))
circuit.append(Gates.U3Gate(3.6652643129524427, 3.6818876186109124, 2.469344104714078)( qr[7] ))
circuit.append(Gates.XGate( qr[5] ))
circuit.append(Gates.iSwapGate( qr[3], qr[9] ))
circuit.append(Gates.SwapGate( qr[0], qr[7] ))
circuit.append(Gates.DCXGate( qr[4], qr[3] ))
circuit.append(Gates.CXGate( qr[9], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[6], qr[9] ))
circuit.append(Gates.U1Gate(4.379482838154957)( qr[0] ))
circuit.append(Gates.DCXGate( qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[5], qr[0] ))
circuit.append(Gates.PhaseGate(3.0078842093393288)( qr[0] ))
circuit.append(Gates.DCXGate( qr[4], qr[6] ))
circuit.append(Gates.CRXGate(4.021310180959978)( qr[2], qr[3] ))
circuit.append(Gates.RZZGate(1.6685155387019077)( qr[4], qr[0] ))
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













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

