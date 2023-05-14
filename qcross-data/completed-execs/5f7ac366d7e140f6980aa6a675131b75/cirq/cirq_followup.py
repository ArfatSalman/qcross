
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[2] ))
circuit.append(Gates.SXdgGate( qr[4] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.C3XGate(5.94477504571567)( qr[4], qr[3], qr[0], qr[1] ))
subcircuit.append(Gates.CSwapGate( qr[3], qr[1], qr[0] ))
subcircuit.append(Gates.HGate( qr[3] ))
subcircuit.append(Gates.CRXGate(5.091930552861214)( qr[4], qr[3] ))
subcircuit.append(Gates.SXGate( qr[3] ))
subcircuit.append(Gates.CRZGate(2.008796895454228)( qr[3], qr[2] ))
subcircuit.append(Gates.YGate( qr[3] ))
subcircuit.append(Gates.RCCXGate( qr[1], qr[0], qr[4] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CSXGate( qr[0], qr[3] ))
circuit.append(Gates.ECRGate( qr[2], qr[4] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[1], qr[2] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[2], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[3], qr[4] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 3.865496458458116)( qr[0], qr[1] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[0] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[3], qr[4] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[2], qr[3] ))
circuit.append(cirq.measure(qr[3], key='cr0'))
circuit.append(cirq.measure(qr[0], key='cr1'))
circuit.append(cirq.measure(qr[4], key='cr2'))
circuit.append(cirq.measure(qr[2], key='cr3'))
circuit.append(cirq.measure(qr[1], key='cr4'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

