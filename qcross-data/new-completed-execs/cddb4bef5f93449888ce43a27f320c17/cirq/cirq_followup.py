
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.RC3XGate( qr[9], qr[6], qr[0], qr[2] ))
circuit.append(Gates.PhaseGate(6.09316043121222)( qr[7] ))
circuit.append(Gates.CHGate( qr[3], qr[9] ))
circuit.append(Gates.XGate( qr[7] ))
circuit.append(Gates.CU1Gate(3.0503162741407537)( qr[8], qr[6] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.U1Gate(5.75020155959207)( qr[3] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.IGate( qr[6] ))
circuit.append(Gates.RYGate(6.135776937038943)( qr[5] ))
circuit.append(Gates.RXGate(0.5846665175165219)( qr[2] ))
circuit.append(Gates.DCXGate( qr[0], qr[5] ))
circuit.append(Gates.RZZGate(5.985328734366836)( qr[0], qr[8] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CRXGate(0.7524962069161311)( qr[1], qr[6] ))
subcircuit.append(Gates.CCZGate( qr[7], qr[1], qr[6] ))
subcircuit.append(Gates.RZZGate(0.46490371756219195)( qr[7], qr[5] ))
subcircuit.append(Gates.DCXGate( qr[4], qr[9] ))
subcircuit.append(Gates.RVGate(5.04524665062051, 1.7636237549722318, 4.690324347774963)( qr[9] ))
subcircuit.append(Gates.U1Gate(2.4842501674681814)( qr[6] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRYGate(2.033688313756901)( qr[8], qr[7] ))
circuit.append(Gates.SdgGate( qr[6] ))
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

