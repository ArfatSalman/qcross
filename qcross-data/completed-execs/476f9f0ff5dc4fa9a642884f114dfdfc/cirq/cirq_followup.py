
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.HGate( qr[1] ))
circuit.append(Gates.U3Gate(0.2435863694263356, 4.952605016068409, 1.0462631235631594)( qr[0] ))
circuit.append(Gates.CRZGate(3.8430137210716477)( qr[0], qr[3] ))
circuit.append(Gates.RCCXGate( qr[1], qr[2], qr[0] ))
circuit.append(Gates.RYYGate(1.9038331447854693)( qr[0], qr[3] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.RC3XGate( qr[0], qr[2], qr[3], qr[1] ))
circuit.append(Gates.DCXGate( qr[3], qr[0] ))
circuit.append(Gates.U2Gate(2.315671616264609, 3.642280082030703)( qr[1] ))
circuit.append(Gates.DCXGate( qr[1], qr[3] ))
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
