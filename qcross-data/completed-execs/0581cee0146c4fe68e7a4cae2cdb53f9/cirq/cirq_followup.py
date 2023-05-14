
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[0] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[4], qr[2] ))
circuit.append(Gates.ZGate( qr[10] ))
circuit.append(Gates.CCXGate( qr[3], qr[1], qr[8] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.RCCXGate( qr[5], qr[4], qr[9] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[6] ))
circuit.append(Gates.CCXGate( qr[8], qr[5], qr[2] ))
circuit.append(Gates.SdgGate( qr[8] ))
circuit.append(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( qr[5] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[6], qr[8] ))
circuit.append(Gates.CU1Gate(4.028174522740928)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(5.0063780207098425)( qr[4] ))
circuit.append(cirq.measure(qr[6], key='cr0'))
circuit.append(cirq.measure(qr[10], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[0], key='cr3'))
circuit.append(cirq.measure(qr[7], key='cr4'))
circuit.append(cirq.measure(qr[3], key='cr5'))
circuit.append(cirq.measure(qr[4], key='cr6'))
circuit.append(cirq.measure(qr[8], key='cr7'))
circuit.append(cirq.measure(qr[9], key='cr8'))
circuit.append(cirq.measure(qr[1], key='cr9'))
circuit.append(cirq.measure(qr[5], key='cr10'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0', 'm_cr9_0', 'm_cr10_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

