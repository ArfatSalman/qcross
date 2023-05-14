
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



circuit = cirq.Circuit()

circuit.append(Gates.YGate( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZXGate(3.16172626234211)( qr[8], qr[7] ))
subcircuit.append(Gates.IGate( qr[2] ))
subcircuit.append(Gates.RZXGate(2.6189671924535145)( qr[1], qr[6] ))
subcircuit.append(Gates.CCXGate( qr[6], qr[8], qr[5] ))
subcircuit.append(Gates.U3Gate(2.1917712015201105, 6.242718257689912, 4.756709623150395)( qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.SwapGate( qr[5], qr[8] ))
circuit.append(Gates.CRYGate(0.4514529683521159)( qr[3], qr[4] ))
circuit.append(Gates.iSwapGate( qr[2], qr[8] ))
circuit.append(Gates.CYGate( qr[4], qr[3] ))
circuit.append(Gates.SXdgGate( qr[7] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })
