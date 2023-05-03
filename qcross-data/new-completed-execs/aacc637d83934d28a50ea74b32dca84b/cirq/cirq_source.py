
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.CRYGate(4.682220755041814)( qr[0], qr[1] ))
circuit.append(Gates.CUGate(5.960866266876448, 5.945098421875394, 4.418481228600101, 3.972623244718876)( qr[1], qr[0] ))
circuit.append(Gates.PhaseGate(2.031442273399285)( qr[0] ))
circuit.append(Gates.U1Gate(1.1449128292629545)( qr[1] ))
circuit.append(Gates.CRYGate(1.8638911468677428)( qr[0], qr[1] ))
circuit.append(Gates.CSdgGate( qr[0], qr[1] ))
circuit.append(Gates.RVGate(3.2561786456517483, 4.027853623334148, 0.7501118686992972)( qr[1] ))
circuit.append(Gates.PhaseGate(3.1265936864110326)( qr[0] ))
circuit.append(Gates.PhaseGate(2.7301494704572584)( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.CRZGate(2.967811594681098)( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

