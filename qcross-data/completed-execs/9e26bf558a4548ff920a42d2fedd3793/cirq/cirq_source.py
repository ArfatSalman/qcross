
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.CSXGate( qr[2], qr[3] ))
circuit.append(Gates.CCXGate( qr[0], qr[1], qr[4] ))
circuit.append(Gates.RYYGate(3.630000846740864)( qr[4], qr[0] ))
circuit.append(Gates.XGate( qr[4] ))
circuit.append(Gates.RC3XGate( qr[4], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(2.3801704973111244)( qr[1], qr[3] ))
circuit.append(Gates.RYYGate(2.26249791419463)( qr[3], qr[2] ))
circuit.append(Gates.IGate( qr[4] ))
circuit.append(Gates.U2Gate(0.024205049091638117, 3.6641337073605276)( qr[4] ))
circuit.append(Gates.CRYGate(0.5432436418208648)( qr[3], qr[2] ))
circuit.append(Gates.CPhaseGate(2.5556929743025827)( qr[0], qr[2] ))
circuit.append(Gates.IGate( qr[3] ))
circuit.append(Gates.CZGate( qr[3], qr[2] ))
circuit.append(Gates.CU1Gate(2.849292498056443)( qr[3], qr[0] ))
circuit.append(Gates.CSwapGate( qr[0], qr[3], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.iSwapGate( qr[4], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
