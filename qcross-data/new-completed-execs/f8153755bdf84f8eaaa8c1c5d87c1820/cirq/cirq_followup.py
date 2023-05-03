
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]



circuit = cirq.Circuit()

circuit.append(Gates.CRXGate(4.905634676582973)( qr[4], qr[1] ))
circuit.append(Gates.RGate(4.591350839465064, 1.2679876620814976)( qr[5] ))
circuit.append(Gates.CZGate( qr[4], qr[10] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.SGate( qr[6] ))
subcircuit.append(Gates.CPhaseGate(0.8912299955175988)( qr[10], qr[9] ))
subcircuit.append(Gates.RXXGate(6.202385428323795)( qr[9], qr[2] ))
subcircuit.append(Gates.CU3Gate(0.17275929115190944, 3.979025542935018, 1.5894459673585912)( qr[2], qr[8] ))
subcircuit.append(Gates.RZGate(5.22819431699873)( qr[3] ))
subcircuit.append(Gates.IGate( qr[4] ))
subcircuit.append(Gates.RYGate(5.90619537594574)( qr[6] ))
subcircuit.append(Gates.CU3Gate(3.688151163878286, 4.727514924286728, 4.075756946750543)( qr[7], qr[6] ))
subcircuit.append(Gates.U1Gate(5.472976168291315)( qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.U3Gate(4.438175883374682, 5.014778227242978, 0.395105964485411)( qr[9] ))
circuit.append(Gates.IGate( qr[10] ))
circuit.append(Gates.CRXGate(2.8176864996575204)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[0], qr[2] ))
circuit.append(Gates.IGate( qr[4] ))
circuit.append(Gates.SGate( qr[9] ))
circuit.append(Gates.CRXGate(6.06720431582227)( qr[0], qr[8] ))
circuit.append(Gates.U2Gate(3.8396484521920486, 5.389605086705323)( qr[0] ))
circuit.append(Gates.CYGate( qr[0], qr[9] ))
circuit.append(Gates.CRXGate(0.6410834959357722)( qr[1], qr[2] ))
circuit.append(Gates.CRXGate(3.152773209785367)( qr[5], qr[2] ))
circuit.append(Gates.CSGate( qr[2], qr[3] ))
circuit.append(Gates.RC3XGate( qr[0], qr[8], qr[6], qr[4] ))
circuit.append(Gates.iSwapGate( qr[3], qr[6] ))
circuit.append(Gates.CRYGate(3.8184925395522673)( qr[7], qr[1] ))
circuit.append(Gates.RZXGate(5.0844543693921445)( qr[9], qr[0] ))
circuit.append(Gates.RCCXGate( qr[4], qr[3], qr[2] ))
circuit.append(Gates.U2Gate(0.5232088988285076, 1.5882644602699434)( qr[7] ))
circuit.append(Gates.CCZGate( qr[5], qr[2], qr[6] ))
circuit.append(Gates.IGate( qr[10] ))
circuit.append(Gates.iSwapGate( qr[6], qr[10] ))
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

