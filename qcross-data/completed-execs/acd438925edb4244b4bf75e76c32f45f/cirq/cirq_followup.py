
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.IGate( qr[3] ))
circuit.append(Gates.XGate( qr[4] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.C3XGate( qr[4], qr[6], qr[3], qr[2] ))
circuit.append(Gates.CU1Gate(3.9840757667715256)( qr[3], qr[6] ))
circuit.append(Gates.U2Gate(1.2445320670388027, 5.484541161403915)( qr[5] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.DCXGate( qr[6], qr[3] ))
circuit.append(Gates.U3Gate(2.0075607189768796, 4.451648094855798, 0.9112643954181384)( qr[5] ))
circuit.append(Gates.CRXGate(2.3584860491406796)( qr[1], qr[6] ))
circuit.append(Gates.CU1Gate(0.1446301149031628)( qr[3], qr[1] ))
circuit.append(Gates.CUGate(0.5186416756754034, 0.37593935376934196, 5.5900874211259195, 1.3667758390177343)( qr[2], qr[3] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.UGate(5.054317038195475, 0.7695110069701433, 1.2922416810957755)( qr[1] ))
circuit.append(Gates.U2Gate(0.1149636377110738, 4.386499201930481)( qr[2] ))
circuit.append(Gates.U3Gate(4.785990021070069, 3.3831192493434576, 3.322394937884733)( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRYGate(0.6395924521893505)( qr[1], qr[0] ))
circuit.append(Gates.SwapGate( qr[0], qr[5] ))
circuit.append(Gates.SwapGate( qr[5], qr[3] ))
circuit.append(Gates.CRYGate(1.3751732052958698)( qr[4], qr[5] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CSXGate( qr[6], qr[3] ))
circuit.append(Gates.C3SXGate( qr[5], qr[2], qr[0], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
