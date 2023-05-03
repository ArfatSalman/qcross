
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.SGate( qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CCZGate( qr[4], qr[1], qr[0] ))
subcircuit.append(Gates.RZZGate(1.494768934171475)( qr[3], qr[0] ))
subcircuit.append(Gates.RGate(0.2569619900931398, 2.6199756460968913)( qr[4] ))
subcircuit.append(Gates.TdgGate( qr[3] ))
subcircuit.append(Gates.SXdgGate( qr[1] ))
subcircuit.append(Gates.PhaseGate(4.75198563922302)( qr[0] ))
subcircuit.append(Gates.RC3XGate( qr[1], qr[3], qr[4], qr[2] ))
subcircuit.append(Gates.SGate( qr[3] ))
subcircuit.append(Gates.CHGate( qr[1], qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CSdgGate( qr[0], qr[2] ))
circuit.append(Gates.RXGate(5.16336000498251)( qr[2] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRXGate(3.8747797547682863)( qr[0], qr[1] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(Gates.SwapGate( qr[3], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[3] ))
circuit.append(Gates.CSdgGate( qr[3], qr[2] ))
circuit.append(Gates.DCXGate( qr[2], qr[3] ))
circuit.append(Gates.CPhaseGate(1.6310047821220433)( qr[3], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))




UNITARY = cirq.unitary(circuit)




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

