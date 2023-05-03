
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.RYYGate(1.7892872835005398)( qr[0], qr[5] ))
circuit.append(Gates.PhaseGate(3.7964394792576885)( qr[6] ))
circuit.append(Gates.RYGate(3.6138974545836176)( qr[2] ))
circuit.append(Gates.CU1Gate(4.877167017151953)( qr[4], qr[1] ))
circuit.append(Gates.CCXGate( qr[4], qr[3], qr[2] ))
circuit.append(Gates.ECRGate( qr[0], qr[6] ))
circuit.append(Gates.CSwapGate( qr[0], qr[6], qr[4] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.SwapGate( qr[3], qr[5] ))
circuit.append(Gates.CSwapGate( qr[3], qr[6], qr[1] ))
circuit.append(Gates.RC3XGate( qr[6], qr[1], qr[4], qr[0] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.UGate(5.066050249739578, 3.676251393433825, 2.5510590709018732)( qr[2] ))
circuit.append(Gates.U2Gate(4.9702527118009066, 3.5114983819004046)( qr[4] ))
circuit.append(Gates.CSGate( qr[2], qr[5] ))
circuit.append(Gates.U2Gate(1.6924855892819173, 6.035455549292343)( qr[6] ))
circuit.append(Gates.RYYGate(3.0928548495797905)( qr[1], qr[5] ))
circuit.append(Gates.RC3XGate( qr[3], qr[1], qr[4], qr[5] ))
circuit.append(Gates.UGate(0.8822742453157227, 3.4849606070943584, 4.713462039096519)( qr[3] ))
circuit.append(Gates.CUGate(5.814210499839879, 2.2396990253899713, 5.986977817617511, 6.091448724065051)( qr[3], qr[5] ))
circuit.append(Gates.U2Gate(4.95448520957096, 2.4524844691285543)( qr[6] ))
circuit.append(Gates.RC3XGate( qr[1], qr[3], qr[2], qr[0] ))
circuit.append(Gates.RXGate(5.129266867572668)( qr[0] ))
circuit.append(Gates.CRYGate(2.998268232293747)( qr[6], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

