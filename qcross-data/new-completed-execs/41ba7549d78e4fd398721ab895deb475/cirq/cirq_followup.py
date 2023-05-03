
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.PhaseGate(5.010091518352677)( qr[2] ))
subcircuit.append(Gates.CSwapGate( qr[1], qr[2], qr[0] ))
subcircuit.append(Gates.CSwapGate( qr[0], qr[2], qr[1] ))
subcircuit.append(Gates.RGate(0.2790475427948373, 2.0520628548884505)( qr[2] ))
subcircuit.append(Gates.RXGate(3.7527661762502977)( qr[2] ))
subcircuit.append(Gates.SXdgGate( qr[0] ))
subcircuit.append(Gates.ZGate( qr[2] ))
subcircuit.append(Gates.RZZGate(5.975361677668773)( qr[1], qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.RZZGate(2.061149362743449)( qr[1], qr[0] ))
circuit.append(Gates.CZGate( qr[2], qr[1] ))
circuit.append(Gates.CZGate( qr[1], qr[0] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.IGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.CCZGate( qr[2], qr[1], qr[0] ))
circuit.append(Gates.CSwapGate( qr[2], qr[1], qr[0] ))
circuit.append(Gates.IGate( qr[1] ))
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

