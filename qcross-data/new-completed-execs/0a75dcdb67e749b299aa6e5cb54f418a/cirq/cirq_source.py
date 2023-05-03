
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.CYGate( qr[0], qr[3] ))
circuit.append(Gates.RC3XGate( qr[3], qr[0], qr[2], qr[1] ))
circuit.append(Gates.CUGate(0.9157606983245934, 5.397500370041537, 3.7108393874093117, 3.651689382779405)( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[1], qr[3] ))
circuit.append(Gates.CSdgGate( qr[1], qr[3] ))
circuit.append(Gates.DCXGate( qr[3], qr[0] ))
circuit.append(Gates.RZXGate(1.7115424816079432)( qr[0], qr[3] ))
circuit.append(Gates.RZXGate(1.6486589761943145)( qr[2], qr[0] ))
circuit.append(Gates.C3XGate( qr[0], qr[2], qr[3], qr[1] ))
circuit.append(Gates.RYYGate(4.794877298046951)( qr[0], qr[1] ))
circuit.append(Gates.RZXGate(3.4346411253220106)( qr[3], qr[1] ))
circuit.append(Gates.RYYGate(6.102373854375312)( qr[3], qr[2] ))
circuit.append(Gates.CU3Gate(2.6976815284019784, 0.9310317943034069, 1.8906179385735775)( qr[3], qr[0] ))
circuit.append(Gates.IGate( qr[0] ))
circuit.append(Gates.UGate(5.176714778665683, 0.30607591346008556, 0.8506581770011129)( qr[3] ))
circuit.append(Gates.C3XGate( qr[2], qr[1], qr[3], qr[0] ))
circuit.append(Gates.UGate(2.478741058575176, 4.422282188870415, 4.889199801305671)( qr[1] ))
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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

