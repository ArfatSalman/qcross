
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.UGate(1.0932143214299395, 6.100531540039404, 4.859714896792146)( qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CYGate( qr[1], qr[0] ))
subcircuit.append(Gates.RVGate(2.4118372331017857, 4.007316327236995, 4.304922836512128)( qr[1] ))
subcircuit.append(Gates.RZXGate(4.840163560981886)( qr[1], qr[0] ))
subcircuit.append(Gates.RXGate(2.7792529037894678)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.RXGate(4.335996068527454)( qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RXGate(6.070601620234646)( qr[0] ))
circuit.append(Gates.RZXGate(3.9660842997699097)( qr[0], qr[1] ))
circuit.append(Gates.HGate( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

