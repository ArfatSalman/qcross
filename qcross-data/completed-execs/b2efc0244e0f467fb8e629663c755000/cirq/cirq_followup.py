
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
circuit.append(Gates.C3SXGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[0], qr[2], qr[3] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.SXdgGate( qr[3] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[3], qr[2] ))
circuit.append(Gates.RCCXGate( qr[3], qr[1], qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.CRZGate(2.9790366726895714)( qr[2], qr[0] ))
circuit.append(Gates.C3SXGate( qr[0], qr[3], qr[2], qr[1] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[3], qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[2], qr[1] ))
circuit.append(Gates.iSwapGate( qr[0], qr[2] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[3], qr[2] ))
circuit.append(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
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
