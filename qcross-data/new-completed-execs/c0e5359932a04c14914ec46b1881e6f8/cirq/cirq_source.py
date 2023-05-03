
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.DCXGate( qr[0], qr[4] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.RVGate(6.18003471835015, 5.977025954690239, 2.6287210175731346)( qr[4] ))
circuit.append(Gates.U1Gate(0.18970742217530903)( qr[3] ))
circuit.append(Gates.CPhaseGate(2.916558815706837)( qr[2], qr[1] ))
circuit.append(Gates.U2Gate(1.5787156628547458, 2.0930109781345063)( qr[2] ))
circuit.append(Gates.CRXGate(5.786879734179932)( qr[0], qr[3] ))
circuit.append(Gates.CPhaseGate(4.358574517050474)( qr[3], qr[2] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.U1Gate(2.950818625000669)( qr[0] ))
circuit.append(Gates.CPhaseGate(1.6476787886644708)( qr[2], qr[0] ))
circuit.append(Gates.ECRGate( qr[2], qr[4] ))
circuit.append(Gates.CPhaseGate(4.051497867526455)( qr[4], qr[3] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

