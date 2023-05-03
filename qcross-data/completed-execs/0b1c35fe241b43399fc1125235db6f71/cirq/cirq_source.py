
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054)( qr[4], qr[3] ))
circuit.append(Gates.RZGate(3.1208310247400375)( qr[6] ))
circuit.append(Gates.RZGate(1.7510965512636645)( qr[6] ))
circuit.append(Gates.UGate(1.4424895697923088, 5.472664875176172, 2.66053590714238)( qr[0] ))
circuit.append(Gates.C3XGate( qr[1], qr[2], qr[6], qr[5] ))
circuit.append(Gates.CCXGate( qr[6], qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[1], qr[6] ))
circuit.append(Gates.RXXGate(1.3311670849927728)( qr[6], qr[2] ))
circuit.append(Gates.RYGate(5.99120670299654)( qr[3] ))
circuit.append(Gates.CUGate(5.709276284014425, 1.1243723913896708, 5.481400346001526, 3.157375188814291)( qr[0], qr[6] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CSwapGate( qr[4], qr[3], qr[1] ))
circuit.append(Gates.CU1Gate(4.388257530988808)( qr[3], qr[4] ))
circuit.append(Gates.CUGate(2.945697832726557, 3.322311684185455, 2.468007457013939, 1.7221796439586554)( qr[6], qr[3] ))
circuit.append(Gates.RYGate(4.206888046259435)( qr[1] ))
circuit.append(Gates.RZGate(5.89153421924888)( qr[6] ))
circuit.append(Gates.TdgGate( qr[4] ))
circuit.append(Gates.RXXGate(3.9517064865019407)( qr[1], qr[6] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

