
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[0] ))
circuit.append(Gates.RZZGate(4.066449154047175)( qr[3], qr[1] ))
circuit.append(Gates.iSwapGate( qr[3], qr[1] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941)( qr[2], qr[3] ))
circuit.append(Gates.CU1Gate(5.154187354656876)( qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CU3Gate(4.501598818751339, 3.831363380793745, 0.29379897242098046)( qr[2], qr[3] ))
subcircuit.append(Gates.HGate( qr[0] ))
subcircuit.append(Gates.CU1Gate(4.229610589867865)( qr[0], qr[1] ))
subcircuit.append(Gates.ECRGate( qr[0], qr[1] ))
subcircuit.append(Gates.U2Gate(6.171674001528992, 4.948673314014118)( qr[2] ))
subcircuit.append(Gates.SGate( qr[0] ))
subcircuit.append(Gates.CXGate( qr[2], qr[1] ))
subcircuit.append(Gates.RXXGate(3.855749700561927)( qr[0], qr[1] ))
subcircuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.C3SXGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[0], qr[2], qr[3] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.SXdgGate( qr[3] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[3], qr[2] ))
circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[0], key='cr1'))
circuit.append(cirq.measure(qr[3], key='cr2'))
circuit.append(cirq.measure(qr[1], key='cr3'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

