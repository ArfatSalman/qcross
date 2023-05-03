
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(Gates.CRYGate(0.8476513988624245)( qr[4], qr[0] ))
circuit.append(Gates.CU1Gate(1.5710197357755318)( qr[3], qr[2] ))
circuit.append(Gates.TdgGate( qr[2] ))
circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(Gates.CCZGate( qr[2], qr[1], qr[3] ))
circuit.append(Gates.UGate(0.708502006099043, 2.97765669736744, 5.6444063351584415)( qr[2] ))
circuit.append(Gates.CPhaseGate(5.597667172921795)( qr[3], qr[4] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CRYGate(0.3177314062860099)( qr[4], qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CSGate( qr[3], qr[0] ))
subcircuit.append(Gates.SdgGate( qr[3] ))
subcircuit.append(Gates.CRYGate(2.8571614999629205)( qr[1], qr[0] ))
subcircuit.append(Gates.RZXGate(1.1653856966610614)( qr[2], qr[1] ))
subcircuit.append(Gates.RXGate(5.646774609269053)( qr[4] ))
subcircuit.append(Gates.CXGate( qr[2], qr[1] ))
subcircuit.append(Gates.ZGate( qr[4] ))
subcircuit.append(Gates.YGate( qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CU1Gate(1.9730677082046415)( qr[4], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

