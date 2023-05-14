
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(6.163759533339787)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(1.977559237989846)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CRZGate(2.2498881927557752)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(5.320621737498446)( qr[1] ))
circuit.append(Gates.RZGate(5.512260524440591)( qr[1] ))
circuit.append(Gates.CU1Gate(1.6723037552953224)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RZZGate(6.086884486572108)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.RYYGate(3.3705408413231095)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(5.190931186022931)( qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

