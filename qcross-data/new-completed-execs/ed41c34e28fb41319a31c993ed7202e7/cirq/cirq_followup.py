
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.CCZGate( qr[2], qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(2.6781418933705265, 5.033873892484971, 0.8205539045157343)( qr[0], qr[2] ))
circuit.append(Gates.CSGate( qr[2], qr[0] ))
circuit.append(Gates.CSdgGate( qr[2], qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CYGate( qr[1], qr[2] ))
subcircuit.append(Gates.CRZGate(2.0238721057673663)( qr[0], qr[2] ))
subcircuit.append(Gates.U2Gate(4.584479443719739, 1.724423394919128)( qr[0] ))
subcircuit.append(Gates.CSXGate( qr[1], qr[0] ))
subcircuit.append(Gates.CRYGate(0.8712775153371473)( qr[0], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRYGate(1.4158427363998418)( qr[0], qr[1] ))
circuit.append(Gates.CU3Gate(3.033025708292916, 4.882023158927633, 2.498989202347216)( qr[0], qr[1] ))
circuit.append(Gates.CSGate( qr[1], qr[0] ))
circuit.append(Gates.U2Gate(1.2920361589137734, 0.11522677196421838)( qr[2] ))
circuit.append(Gates.CUGate(0.5771195062234611, 6.03105941204732, 5.250698623145584, 4.055221339124102)( qr[1], qr[2] ))
circuit.append(Gates.CU3Gate(1.40128081782857, 0.22745116565007226, 1.0942942714535664)( qr[2], qr[1] ))
circuit.append(Gates.CU3Gate(5.272901276657899, 4.665266516802061, 4.874107923353778)( qr[0], qr[2] ))
circuit.append(Gates.CXGate( qr[1], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

