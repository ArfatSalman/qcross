
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]



circuit = cirq.Circuit()

circuit.append(Gates.CRXGate(4.905634676582973)( qr[4], qr[1] ))
circuit.append(Gates.RGate(4.591350839465064, 1.2679876620814976)( qr[5] ))
circuit.append(Gates.CZGate( qr[4], qr[10] ))
circuit.append(Gates.U3Gate(4.438175883374682, 5.014778227242978, 0.395105964485411)( qr[9] ))
circuit.append(Gates.IGate( qr[10] ))
circuit.append(Gates.CRXGate(2.8176864996575204)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[0], qr[2] ))
circuit.append(Gates.IGate( qr[4] ))
circuit.append(Gates.SGate( qr[9] ))
circuit.append(Gates.CRXGate(6.06720431582227)( qr[0], qr[8] ))
circuit.append(Gates.U2Gate(3.8396484521920486, 5.389605086705323)( qr[0] ))
circuit.append(Gates.CYGate( qr[0], qr[9] ))
circuit.append(Gates.CRXGate(0.6410834959357722)( qr[1], qr[2] ))
circuit.append(Gates.CRXGate(3.152773209785367)( qr[5], qr[2] ))
circuit.append(Gates.CSGate( qr[2], qr[3] ))
circuit.append(Gates.RC3XGate( qr[0], qr[8], qr[6], qr[4] ))
circuit.append(Gates.iSwapGate( qr[3], qr[6] ))
circuit.append(Gates.CRYGate(3.8184925395522673)( qr[7], qr[1] ))
circuit.append(Gates.RZXGate(5.0844543693921445)( qr[9], qr[0] ))
circuit.append(Gates.RCCXGate( qr[4], qr[3], qr[2] ))
circuit.append(Gates.U2Gate(0.5232088988285076, 1.5882644602699434)( qr[7] ))
circuit.append(Gates.CCZGate( qr[5], qr[2], qr[6] ))
circuit.append(Gates.IGate( qr[10] ))
circuit.append(Gates.iSwapGate( qr[6], qr[10] ))
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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

