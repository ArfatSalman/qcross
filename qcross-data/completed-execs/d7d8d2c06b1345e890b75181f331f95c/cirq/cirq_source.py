
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.SXdgGate( qr[5] ))
circuit.append(Gates.RZGate(0.6386974670970621)( qr[2] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.CPhaseGate(4.103056419716538)( qr[1], qr[4] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.CPhaseGate(1.57456137798405)( qr[0], qr[3] ))
circuit.append(Gates.RCCXGate( qr[4], qr[5], qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[1] ))
circuit.append(Gates.RYGate(4.436548686510933)( qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[5] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
