
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.DCXGate( qr[7], qr[1] ))
circuit.append(Gates.CRZGate(3.5837947443419367)( qr[7], qr[3] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[3], qr[2] ))
circuit.append(Gates.CRYGate(4.123021946449677)( qr[5], qr[1] ))
circuit.append(Gates.CSXGate( qr[4], qr[7] ))
circuit.append(Gates.RZXGate(4.811413391581055)( qr[5], qr[0] ))
circuit.append(Gates.CU1Gate(3.648178050626694)( qr[6], qr[4] ))
circuit.append(Gates.RYGate(5.8216640063628375)( qr[1] ))
circuit.append(Gates.CU1Gate(0.7038286154091901)( qr[7], qr[1] ))
circuit.append(Gates.DCXGate( qr[2], qr[5] ))
circuit.append(Gates.CYGate( qr[6], qr[5] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(0.18001367059010623)( qr[1], qr[6] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[2], qr[6] ))
circuit.append(Gates.PhaseGate(5.414747327887186)( qr[1] ))
circuit.append(Gates.CRYGate(4.001439863248854)( qr[1], qr[5] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
