
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.UGate(4.403788193532198, 5.238005217278175, 2.414376925356305)( qr[1] ))
circuit.append(Gates.RGate(3.9800961208659213, 2.54258238968427)( qr[0] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(Gates.CRXGate(3.0761375449158193)( qr[1], qr[0] ))
circuit.append(Gates.CSdgGate( qr[0], qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.CU3Gate(3.359364374345002, 4.018048446348199, 2.251031643786726)( qr[0], qr[1] ))
circuit.append(Gates.CZGate( qr[1], qr[0] ))
circuit.append(Gates.RGate(4.3040860238694725, 4.7611258330830655)( qr[1] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.UGate(3.820196974130503, 1.381440535002157, 5.6467633400840755)( qr[1] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
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

