
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.RXGate(0.6650027350645848)( qr[5] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.CYGate( qr[0], qr[4] ))
circuit.append(Gates.RVGate(4.207878413680952, 0.3009231473653096, 1.580343691421699)( qr[4] ))
circuit.append(Gates.CPhaseGate(3.9206722628490542)( qr[5], qr[2] ))
circuit.append(Gates.CPhaseGate(3.397598873029434)( qr[2], qr[3] ))
circuit.append(Gates.IGate( qr[4] ))
circuit.append(Gates.U2Gate(4.855299131904333, 3.1272609413923482)( qr[3] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.RXXGate(0.7249247820191558)( qr[3], qr[4] ))
circuit.append(Gates.TdgGate( qr[5] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CXGate( qr[4], qr[1] ))
circuit.append(Gates.IGate( qr[5] ))
circuit.append(Gates.RC3XGate( qr[5], qr[2], qr[4], qr[3] ))
circuit.append(Gates.RC3XGate( qr[5], qr[2], qr[4], qr[0] ))
circuit.append(Gates.RXXGate(2.6498953828086473)( qr[2], qr[4] ))
circuit.append(Gates.CYGate( qr[5], qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.iSwapGate( qr[0], qr[2] ))
circuit.append(Gates.HGate( qr[4] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.SwapGate( qr[1], qr[0] ))
subcircuit.append(Gates.CYGate( qr[0], qr[5] ))
subcircuit.append(Gates.CCZGate( qr[4], qr[3], qr[5] ))
subcircuit.append(Gates.DCXGate( qr[0], qr[2] ))
subcircuit.append(Gates.RXGate(5.981830878165426)( qr[2] ))
subcircuit.append(Gates.U3Gate(2.693422775984842, 0.5067499290735414, 2.096989391777038)( qr[5] ))
subcircuit.append(Gates.SwapGate( qr[0], qr[3] ))
subcircuit.append(Gates.CU3Gate(2.0053149876729552, 5.072178584377088, 2.2962625668816754)( qr[1], qr[3] ))
subcircuit.append(Gates.RXXGate(4.1874527696058825)( qr[0], qr[4] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.ECRGate( qr[0], qr[5] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

