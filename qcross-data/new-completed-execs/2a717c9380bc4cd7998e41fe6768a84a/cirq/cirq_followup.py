
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.RC3XGate( qr[9], qr[2], qr[0], qr[6] ))
circuit.append(Gates.C4XGate( qr[5], qr[0], qr[9], qr[8], qr[6] ))
circuit.append(Gates.UGate(3.1560639900200687, 5.736507853795902, 5.182419857278261)( qr[3] ))
circuit.append(Gates.C3SXGate( qr[6], qr[3], qr[5], qr[9] ))
circuit.append(Gates.U1Gate(5.966509081754044)( qr[2] ))
circuit.append(Gates.SXGate( qr[6] ))
circuit.append(Gates.CU1Gate(4.213559936940442)( qr[0], qr[6] ))
circuit.append(Gates.CCZGate( qr[6], qr[5], qr[1] ))
circuit.append(Gates.SdgGate( qr[6] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.SXGate( qr[9] ))
circuit.append(Gates.TdgGate( qr[6] ))
circuit.append(Gates.CRYGate(1.543339878695638)( qr[5], qr[1] ))
circuit.append(Gates.TdgGate( qr[9] ))
circuit.append(Gates.CYGate( qr[9], qr[3] ))
circuit.append(Gates.RXXGate(3.253117584460498)( qr[2], qr[4] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[1], qr[6] ))
circuit.append(Gates.U1Gate(4.922680836398291)( qr[1] ))
circuit.append(Gates.CU1Gate(4.44382187374409)( qr[7], qr[4] ))
circuit.append(Gates.CCXGate( qr[9], qr[2], qr[4] ))
circuit.append(Gates.U1Gate(6.275086588388869)( qr[9] ))
circuit.append(Gates.CCXGate( qr[7], qr[1], qr[3] ))
circuit.append(Gates.CSGate( qr[9], qr[5] ))
circuit.append(Gates.CYGate( qr[1], qr[8] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.RXXGate(4.826421202599676)( qr[5], qr[7] ))
circuit.append(Gates.CRYGate(0.6390825368890776)( qr[6], qr[3] ))
circuit.append(Gates.C4XGate( qr[9], qr[2], qr[4], qr[8], qr[7] ))
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













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

