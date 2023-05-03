
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_eb443b = Symbol('p_eb443b')
p_9b2473 = Symbol('p_9b2473')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_eb443b)( qr[1] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.iSwapGate( qr[2], qr[1] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[0], qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.RYYGate(p_9b2473)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_eb443b": 6.163759533339787,
    "p_9b2473": 1.6723037552953224
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

