
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.CRXGate(4.540485128061974)( qr[2], qr[0] ))
circuit.append(Gates.CSwapGate( qr[3], qr[1], qr[2] ))
circuit.append(Gates.CSwapGate( qr[5], qr[1], qr[2] ))
circuit.append(Gates.RYYGate(4.463823258920204)( qr[1], qr[3] ))
circuit.append(Gates.CPhaseGate(3.371946193609531)( qr[6], qr[2] ))
circuit.append(Gates.RYYGate(3.3281963864143704)( qr[2], qr[0] ))
circuit.append(Gates.C3SXGate( qr[3], qr[5], qr[1], qr[6] ))
circuit.append(Gates.RYGate(4.644790991147617)( qr[0] ))
circuit.append(Gates.CPhaseGate(0.3126995978940275)( qr[2], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.RYYGate(6.048921809752355)( qr[5], qr[2] ))
circuit.append(Gates.U3Gate(3.2280333223438684, 1.6763403778979529, 1.308375256732971)( qr[4] ))
circuit.append(Gates.UGate(3.300493821011834, 2.7595037431292786, 0.0456041163048407)( qr[1] ))
circuit.append(Gates.CSwapGate( qr[2], qr[1], qr[6] ))
circuit.append(Gates.C3XGate( qr[3], qr[6], qr[4], qr[1] ))
circuit.append(Gates.UGate(4.005766554739231, 3.562181008920026, 1.1726853359197904)( qr[2] ))
circuit.append(Gates.C3XGate( qr[2], qr[5], qr[1], qr[6] ))
circuit.append(Gates.DCXGate( qr[5], qr[4] ))
circuit.append(Gates.RXXGate(1.0617494142412416)( qr[4], qr[0] ))
circuit.append(Gates.CZGate( qr[4], qr[2] ))
circuit.append(Gates.C3XGate( qr[4], qr[5], qr[1], qr[6] ))
circuit.append(Gates.CPhaseGate(3.64559874218163)( qr[0], qr[5] ))
circuit.append(Gates.RC3XGate( qr[5], qr[6], qr[1], qr[2] ))
circuit.append(Gates.TdgGate( qr[6] ))
circuit.append(Gates.RZGate(3.7376045176206487)( qr[3] ))
circuit.append(Gates.RZZGate(0.353928536272812)( qr[1], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

