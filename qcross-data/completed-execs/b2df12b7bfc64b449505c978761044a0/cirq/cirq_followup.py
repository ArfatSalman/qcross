
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.CYGate( qr[9], qr[3] ))
circuit.append(Gates.CRXGate(3.006996712679364)( qr[0], qr[9] ))
circuit.append(Gates.RXXGate(6.231728094077643)( qr[0], qr[1] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CUGate(5.402681630107685, 5.7320803489582755, 1.5504227913558584, 6.117533666092848)( qr[1], qr[4] ))
circuit.append(Gates.CZGate( qr[0], qr[8] ))
circuit.append(Gates.C3XGate( qr[7], qr[5], qr[0], qr[1] ))
circuit.append(Gates.CYGate( qr[6], qr[9] ))
circuit.append(Gates.CUGate(1.9776456095905999, 2.7856733477756688, 2.3725791317893616, 4.281289624237246)( qr[4], qr[1] ))
circuit.append(Gates.C3SXGate( qr[5], qr[3], qr[8], qr[2] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.DCXGate( qr[6], qr[1] ))
circuit.append(Gates.RXGate(2.7622901582617536)( qr[2] ))
circuit.append(Gates.RCCXGate( qr[7], qr[0], qr[4] ))
circuit.append(Gates.UGate(5.093998211740766, 4.1763972388782795, 1.3446658688471513)( qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.ECRGate( qr[3], qr[9] ))
subcircuit.append(Gates.RC3XGate( qr[2], qr[4], qr[7], qr[9] ))
subcircuit.append(Gates.CU3Gate(3.1029941305253375, 2.467778988525628, 0.806315267571145)( qr[0], qr[2] ))
subcircuit.append(Gates.SXGate( qr[6] ))
subcircuit.append(Gates.SXGate( qr[8] ))
subcircuit.append(Gates.CU3Gate(2.0260479577768926, 1.6908888602654353, 4.870531090171869)( qr[3], qr[4] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CYGate( qr[5], qr[6] ))
circuit.append(Gates.UGate(3.2780013517483826, 1.092359559443437, 2.5802478164404428)( qr[0] ))
circuit.append(Gates.CUGate(5.627192099540417, 2.1947268632429866, 5.888372357253659, 1.16349884234323)( qr[3], qr[4] ))
circuit.append(Gates.CYGate( qr[0], qr[5] ))
circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.RCCXGate( qr[4], qr[0], qr[1] ))
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













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
