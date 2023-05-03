
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



circuit = cirq.Circuit()

circuit.append(Gates.RYYGate(4.230538610152256)( qr[3], qr[8] ))
circuit.append(Gates.CRXGate(3.3203084344733997)( qr[2], qr[3] ))
circuit.append(Gates.CRXGate(4.622916213622228)( qr[6], qr[8] ))
circuit.append(Gates.C3SXGate( qr[8], qr[2], qr[6], qr[1] ))
circuit.append(Gates.CRZGate(2.3252143484585774)( qr[4], qr[8] ))
circuit.append(Gates.CU3Gate(3.9779731506025207, 1.8692602791557653, 3.52092355767973)( qr[0], qr[7] ))
circuit.append(Gates.CSdgGate( qr[5], qr[7] ))
circuit.append(Gates.C3SXGate( qr[6], qr[1], qr[8], qr[4] ))
circuit.append(Gates.CYGate( qr[8], qr[5] ))
circuit.append(Gates.CU1Gate(6.092983263138358)( qr[6], qr[8] ))
circuit.append(Gates.DCXGate( qr[2], qr[1] ))
circuit.append(Gates.CRZGate(0.2732434042738512)( qr[2], qr[8] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CYGate( qr[3], qr[4] ))
circuit.append(Gates.CSdgGate( qr[5], qr[2] ))
circuit.append(Gates.CYGate( qr[0], qr[5] ))
circuit.append(Gates.CUGate(1.3294053085361235, 1.6134324891544933, 1.3668738903035305, 2.2614780495462785)( qr[1], qr[6] ))
circuit.append(Gates.CHGate( qr[6], qr[8] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.RC3XGate( qr[1], qr[7], qr[0], qr[8] ))
circuit.append(Gates.RVGate(4.325005000959295, 1.4884924689724215, 2.122323708296557)( qr[6] ))
circuit.append(Gates.CUGate(4.129509958864599, 2.661313282317246, 3.471286270687046, 3.3400786207701714)( qr[2], qr[5] ))
circuit.append(Gates.CUGate(5.55653769076178, 4.605056011495016, 0.9700427538550028, 1.9703735803987805)( qr[8], qr[0] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[5], qr[2] ))
circuit.append(Gates.CCZGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.CSdgGate( qr[3], qr[8] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

