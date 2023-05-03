
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]



circuit = cirq.Circuit()

circuit.append(Gates.ECRGate( qr[9], qr[2] ))
circuit.append(Gates.TdgGate( qr[4] ))
circuit.append(Gates.CU1Gate(0.7405945593267375)( qr[9], qr[3] ))
circuit.append(Gates.CRYGate(4.601077991755651)( qr[7], qr[9] ))
circuit.append(Gates.CSwapGate( qr[6], qr[0], qr[9] ))
circuit.append(Gates.CPhaseGate(2.9147217589256114)( qr[6], qr[2] ))
circuit.append(Gates.PhaseGate(0.5021373390560734)( qr[9] ))
circuit.append(Gates.XGate( qr[9] ))
circuit.append(Gates.U1Gate(4.188067174285268)( qr[4] ))
circuit.append(Gates.CHGate( qr[7], qr[9] ))
circuit.append(Gates.TdgGate( qr[0] ))
circuit.append(Gates.CPhaseGate(2.629684885038655)( qr[5], qr[3] ))
circuit.append(Gates.CPhaseGate(5.383276207092515)( qr[2], qr[7] ))
circuit.append(Gates.HGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[8], qr[6] ))
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
circuit.append(cirq.measure(qr[10], key='cr10'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
