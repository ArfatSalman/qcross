
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.RZXGate(3.813624597382902)( qr[1], qr[7] ))
circuit.append(Gates.HGate( qr[3] ))
circuit.append(Gates.U1Gate(1.7474579084583979)( qr[5] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.CZGate( qr[1], qr[2] ))
circuit.append(Gates.U1Gate(2.3042652898695457)( qr[6] ))
circuit.append(Gates.UGate(2.879770697683128, 2.335112883423633, 4.1410857855717005)( qr[0] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.U2Gate(4.529061112043725, 0.1128558241378929)( qr[3] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SXGate( qr[4] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.CXGate( qr[2], qr[3] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.U1Gate(2.0589291173378608)( qr[5] ))
circuit.append(Gates.C3SXGate( qr[6], qr[4], qr[2], qr[7] ))
circuit.append(Gates.CHGate( qr[1], qr[7] ))
circuit.append(Gates.RYYGate(0.1445200040685528)( qr[2], qr[6] ))
circuit.append(Gates.SXdgGate( qr[4] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CUGate(2.2742238751077037, 5.678583788689636, 5.945356410023023, 1.2692738094959353)( qr[5], qr[2] ))
circuit.append(Gates.YGate( qr[5] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.C3SXGate( qr[0], qr[3], qr[5], qr[7] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
