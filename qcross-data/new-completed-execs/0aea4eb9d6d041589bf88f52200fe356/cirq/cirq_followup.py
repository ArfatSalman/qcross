
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.RYYGate(0.040332757463886044)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.RZXGate(2.0199977459798464)( qr[0], qr[1] ))
circuit.append(Gates.RXXGate(3.927829733740478)( qr[1], qr[0] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.CRZGate(5.451741496819523)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RXXGate(2.6277753952279403)( qr[0], qr[1] ))
circuit.append(Gates.iSwapGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CRZGate(3.555542082325973)( qr[0], qr[1] ))
circuit.append(Gates.RYYGate(5.488061464125162)( qr[0], qr[1] ))
circuit.append(Gates.RXGate(3.657037356032689)( qr[0] ))
circuit.append(Gates.RXGate(4.976946713501052)( qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CRYGate(3.142547021000323)( qr[0], qr[1] ))
subcircuit.append(Gates.SGate( qr[0] ))
subcircuit.append(Gates.U1Gate(1.1029693994010046)( qr[1] ))
subcircuit.append(Gates.CZGate( qr[1], qr[0] ))
subcircuit.append(Gates.SGate( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.RGate(5.88245539296814, 5.313337512106651)( qr[1] ))
circuit.append(Gates.RXGate(3.1801000664195067)( qr[1] ))
circuit.append(Gates.RYYGate(2.60217238429383)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
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

