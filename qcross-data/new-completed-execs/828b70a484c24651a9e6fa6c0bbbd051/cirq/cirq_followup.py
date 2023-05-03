
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.RYYGate(0.1584650651944304)( qr[1], qr[2] ))
circuit.append(Gates.YGate( qr[2] ))
circuit.append(Gates.RXGate(1.9643059251773882)( qr[6] ))
circuit.append(Gates.CRXGate(2.2091452154672204)( qr[0], qr[6] ))
circuit.append(Gates.CUGate(5.28444061678252, 2.26438130892656, 4.508815818648728, 5.843141721322287)( qr[4], qr[0] ))
circuit.append(Gates.RXGate(2.316480646141322)( qr[1] ))
circuit.append(Gates.RZXGate(1.7530034337193163)( qr[0], qr[4] ))
circuit.append(Gates.CU1Gate(2.75818719037007)( qr[4], qr[1] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.CSwapGate( qr[0], qr[4], qr[5] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.CU3Gate(0.29341892717166834, 6.249908353941511, 2.9247183841853848)( qr[4], qr[3] ))
circuit.append(Gates.RYGate(3.70789888536151)( qr[5] ))
circuit.append(Gates.CYGate( qr[5], qr[0] ))
circuit.append(Gates.CZGate( qr[3], qr[6] ))
circuit.append(Gates.CSGate( qr[3], qr[0] ))
circuit.append(Gates.CSwapGate( qr[2], qr[5], qr[4] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.CRXGate(2.360789071411234)( qr[3], qr[4] ))
circuit.append(Gates.CZGate( qr[1], qr[0] ))
circuit.append(Gates.RXGate(2.191505539211396)( qr[3] ))
circuit.append(Gates.RYYGate(0.39681210536068023)( qr[1], qr[4] ))
circuit.append(Gates.CYGate( qr[4], qr[5] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.YGate( qr[0] ))
circuit.append(Gates.CU3Gate(5.928213929259535, 1.0062255952575803, 2.115561623846294)( qr[5], qr[2] ))
circuit.append(Gates.CYGate( qr[1], qr[6] ))
circuit.append(Gates.CZGate( qr[3], qr[0] ))
circuit.append(Gates.ECRGate( qr[2], qr[4] ))
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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

