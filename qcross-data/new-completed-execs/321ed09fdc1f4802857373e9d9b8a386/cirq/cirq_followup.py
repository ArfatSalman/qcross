
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.CRXGate(3.789039586142132)( qr[0], qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.XGate( qr[0] ))
subcircuit.append(Gates.PhaseGate(1.0991937230132693)( qr[0] ))
subcircuit.append(Gates.RZZGate(0.29263822564237946)( qr[0], qr[1] ))
subcircuit.append(Gates.CU1Gate(1.319709844326333)( qr[1], qr[0] ))
subcircuit.append(Gates.CPhaseGate(0.07651702010631041)( qr[0], qr[1] ))
subcircuit.append(Gates.CUGate(3.544831331267256, 5.290981419397922, 4.5769317827703135, 3.078979867833689)( qr[0], qr[1] ))
subcircuit.append(Gates.RGate(3.7945044816842795, 4.841616274028528)( qr[0] ))
subcircuit.append(Gates.CZGate( qr[1], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.PhaseGate(2.3969015822468824)( qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.PhaseGate(2.7534454125103585)( qr[1] ))
circuit.append(Gates.PhaseGate(4.877116605613038)( qr[0] ))
circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.PhaseGate(5.974310031718985)( qr[1] ))
circuit.append(Gates.U2Gate(3.2332547554497055, 2.6884001068559122)( qr[0] ))
circuit.append(Gates.HGate( qr[1] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.DCXGate( qr[1], qr[0] ))
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

