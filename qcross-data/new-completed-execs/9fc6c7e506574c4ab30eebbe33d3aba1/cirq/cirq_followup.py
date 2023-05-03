
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]



circuit = cirq.Circuit()

circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRYGate(2.4498821250483043)( qr[10], qr[9] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CPhaseGate(5.94833048963124)( qr[6], qr[3] ))
subcircuit.append(Gates.RCCXGate( qr[2], qr[9], qr[4] ))
subcircuit.append(Gates.CCZGate( qr[2], qr[9], qr[5] ))
subcircuit.append(Gates.SXdgGate( qr[4] ))
subcircuit.append(Gates.iSwapGate( qr[0], qr[6] ))
subcircuit.append(Gates.U1Gate(4.170850588142773)( qr[6] ))
subcircuit.append(Gates.CUGate(3.6349610195058815, 3.819623549514622, 1.4862870686636986, 3.4327806393198337)( qr[3], qr[6] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.HGate( qr[1] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.CPhaseGate(3.3516599839543195)( qr[4], qr[3] ))
circuit.append(Gates.ECRGate( qr[5], qr[8] ))
circuit.append(Gates.CU3Gate(5.423661738344168, 1.2257558063112008, 4.146906161622092)( qr[1], qr[8] ))
circuit.append(Gates.RXXGate(0.4988271119481185)( qr[7], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))
circuit.append(cirq.measure(qr[10], key='cr10'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0', 'm_cr9_0', 'm_cr10_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

