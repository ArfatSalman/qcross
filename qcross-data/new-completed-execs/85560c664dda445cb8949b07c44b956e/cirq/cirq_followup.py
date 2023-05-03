
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.CRXGate(6.189367290017951)( qr[6], qr[0] ))
subcircuit.append(Gates.HGate( qr[1] ))
subcircuit.append(Gates.CU3Gate(3.795093132245643, 5.482804960064541, 3.392543408251406)( qr[0], qr[6] ))
subcircuit.append(Gates.RXGate(2.870607397554538)( qr[4] ))
subcircuit.append(Gates.CPhaseGate(4.002346068007423)( qr[3], qr[0] ))
subcircuit.append(Gates.RVGate(4.068029717857408, 0.567304873816878, 3.215798805925656)( qr[6] ))
subcircuit.append(Gates.RZZGate(3.9665175003040227)( qr[0], qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

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

