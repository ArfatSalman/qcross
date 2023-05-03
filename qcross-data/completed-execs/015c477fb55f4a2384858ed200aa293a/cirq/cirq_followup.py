
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[2], qr[5] ))
circuit.append(Gates.C3SXGate( qr[6], qr[0], qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[4], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[6], qr[3] ))
circuit.append(Gates.SdgGate( qr[6] ))
circuit.append(Gates.RCCXGate( qr[2], qr[5], qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[4], qr[6] ))
circuit.append(Gates.CHGate( qr[4], qr[0] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[3], qr[4] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.CRZGate(4.833923139882297)( qr[0], qr[6] ))
circuit.append(Gates.CU1Gate(4.028174522740928)( qr[1], qr[4] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[5], qr[4] ))
circuit.append(Gates.CRZGate(2.586208953975239)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(3.950837470808744)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RYYGate(1.9669252191306448)( qr[4], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

