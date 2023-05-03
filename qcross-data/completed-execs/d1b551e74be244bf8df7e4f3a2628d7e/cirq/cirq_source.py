
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.CU1Gate(1.4006987211512518)( qr[0], qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[2] ))
circuit.append(Gates.RZGate(2.5786401929143787)( qr[1] ))
circuit.append(Gates.RYGate(3.1208310247400375)( qr[0] ))
circuit.append(Gates.CU3Gate(3.4965748481666385, 5.407902101595624, 0.6970696680696589)( qr[0], qr[1] ))
circuit.append(Gates.CSwapGate( qr[0], qr[1], qr[2] ))
circuit.append(Gates.iSwapGate( qr[0], qr[1] ))
circuit.append(Gates.CU3Gate(3.3635160723245443, 2.227557670457083, 1.4424895697923088)( qr[0], qr[2] ))
circuit.append(Gates.RZXGate(0.4418060716084386)( qr[0], qr[1] ))
circuit.append(Gates.CUGate(5.925227014563219, 0.21934961519025842, 2.906368483395291, 4.602208997736638)( qr[1], qr[2] ))
circuit.append(Gates.CYGate( qr[1], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.iSwapGate( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(2.3677386437434818, 4.094703991955255)( qr[2] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

