
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



circuit = cirq.Circuit()

circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.C4XGate( qr[4], qr[7], qr[8], qr[0], qr[6] ))
circuit.append(Gates.TdgGate( qr[4] ))
circuit.append(Gates.PhaseGate(3.583928898313607)( qr[5] ))
circuit.append(Gates.C4XGate( qr[3], qr[0], qr[5], qr[8], qr[2] ))
circuit.append(Gates.RYGate(5.6536210846521495)( qr[0] ))
circuit.append(Gates.TdgGate( qr[3] ))
circuit.append(Gates.U2Gate(5.070978145808224, 4.861997899593006)( qr[6] ))
circuit.append(Gates.CU3Gate(1.0200536425931515, 6.100759745363555, 3.891803045839442)( qr[0], qr[4] ))
circuit.append(Gates.C3SXGate( qr[7], qr[0], qr[1], qr[8] ))
circuit.append(Gates.RYGate(3.345954529034082)( qr[0] ))
circuit.append(Gates.PhaseGate(0.6916556361503159)( qr[3] ))
circuit.append(Gates.RZZGate(5.548043373759139)( qr[0], qr[6] ))
circuit.append(Gates.CYGate( qr[1], qr[2] ))
circuit.append(Gates.CYGate( qr[4], qr[2] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.RCCXGate( qr[8], qr[5], qr[7] ))
circuit.append(Gates.C4XGate( qr[0], qr[4], qr[5], qr[2], qr[6] ))
circuit.append(Gates.U1Gate(0.1283649697684065)( qr[8] ))
circuit.append(Gates.U1Gate(5.195347791320497)( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

