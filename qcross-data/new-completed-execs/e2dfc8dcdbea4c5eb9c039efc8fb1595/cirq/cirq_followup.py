
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.TdgGate( qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.TGate( qr[0] ))
subcircuit.append(Gates.XGate( qr[3] ))
subcircuit.append(Gates.CSdgGate( qr[1], qr[2] ))
subcircuit.append(Gates.RXGate(3.585933838237832)( qr[3] ))
subcircuit.append(Gates.RZGate(4.327708900759496)( qr[2] ))
subcircuit.append(Gates.CSdgGate( qr[1], qr[2] ))
subcircuit.append(Gates.CSdgGate( qr[2], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RC3XGate( qr[3], qr[2], qr[0], qr[1] ))
circuit.append(Gates.CRXGate(3.8220531708356265)( qr[2], qr[3] ))
circuit.append(Gates.RYYGate(0.706851892491546)( qr[0], qr[3] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CCXGate( qr[2], qr[3], qr[0] ))
circuit.append(Gates.U2Gate(4.244731333359949, 5.111240623114551)( qr[1] ))
circuit.append(Gates.U1Gate(6.038142598726985)( qr[3] ))
circuit.append(Gates.RZZGate(4.711366793785529)( qr[0], qr[3] ))
circuit.append(Gates.CCZGate( qr[1], qr[2], qr[3] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.CXGate( qr[2], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.U1Gate(3.792448958077701)( qr[3] ))
circuit.append(Gates.RZZGate(0.34163860688651065)( qr[1], qr[0] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.RXXGate(0.5068226496124109)( qr[0], qr[1] ))
circuit.append(Gates.RYYGate(2.3758586345554287)( qr[2], qr[0] ))
circuit.append(Gates.RXGate(1.4237342865387943)( qr[0] ))
circuit.append(Gates.U1Gate(6.094655700711693)( qr[2] ))
circuit.append(Gates.CSGate( qr[0], qr[1] ))
circuit.append(Gates.CYGate( qr[0], qr[2] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.IGate( qr[3] ))
circuit.append(Gates.CSGate( qr[2], qr[0] ))
circuit.append(Gates.U2Gate(4.750593946827152, 1.9165638225080148)( qr[0] ))
circuit.append(Gates.RXXGate(2.141645891766187)( qr[1], qr[2] ))
circuit.append(Gates.RXGate(5.97814280452802)( qr[3] ))
circuit.append(Gates.CSXGate( qr[3], qr[1] ))
circuit.append(Gates.CSGate( qr[2], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

