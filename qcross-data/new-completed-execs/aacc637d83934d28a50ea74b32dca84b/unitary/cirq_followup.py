
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.CRYGate(4.682220755041814)( qr[0], qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.SdgGate( qr[0] ))
subcircuit.append(Gates.SXdgGate( qr[0] ))
subcircuit.append(Gates.CSGate( qr[1], qr[0] ))
subcircuit.append(Gates.PhaseGate(5.507061057045591)( qr[1] ))
subcircuit.append(Gates.XGate( qr[0] ))
subcircuit.append(Gates.TGate( qr[1] ))
subcircuit.append(Gates.U2Gate(2.3723321578370635, 0.23310288505979176)( qr[1] ))
subcircuit.append(Gates.CPhaseGate(3.5444640315452953)( qr[0], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

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




UNITARY = cirq.unitary(circuit)




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

