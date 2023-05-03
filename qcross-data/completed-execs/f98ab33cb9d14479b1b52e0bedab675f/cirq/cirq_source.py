
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.CYGate( qr[3], qr[2] ))
circuit.append(Gates.RZXGate(4.992926923750951)( qr[1], qr[3] ))
circuit.append(Gates.RYYGate(1.9555057510547085)( qr[0], qr[1] ))
circuit.append(Gates.U1Gate(0.8252193008316542)( qr[1] ))
circuit.append(Gates.CSwapGate( qr[3], qr[1], qr[0] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.iSwapGate( qr[0], qr[2] ))
circuit.append(Gates.RYYGate(3.416474043372992)( qr[1], qr[3] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CRZGate(3.738048947778281)( qr[2], qr[0] ))
circuit.append(Gates.CXGate( qr[2], qr[1] ))
circuit.append(Gates.RXXGate(1.2110824459718403)( qr[0], qr[1] ))
circuit.append(Gates.CPhaseGate(0.538151089952194)( qr[0], qr[1] ))
circuit.append(Gates.CCXGate( qr[0], qr[1], qr[3] ))
circuit.append(Gates.RZGate(1.2470325800417235)( qr[3] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CUGate(0.8310820236250993, 5.196031699053289, 1.9585166986172349, 4.659181440347051)( qr[3], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
