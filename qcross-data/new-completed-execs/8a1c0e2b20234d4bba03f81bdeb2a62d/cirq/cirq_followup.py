
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_435d0d = Symbol('p_435d0d')
p_3c07ca = Symbol('p_3c07ca')
p_ccc6de = Symbol('p_ccc6de')
p_f9d2fd = Symbol('p_f9d2fd')
p_6b41c3 = Symbol('p_6b41c3')
p_8c914c = Symbol('p_8c914c')

circuit = cirq.Circuit()

circuit.append(Gates.CPhaseGate(p_6b41c3)( qr[1], qr[2] ))
circuit.append(Gates.U1Gate(p_3c07ca)( qr[2] ))
circuit.append(Gates.UGate(p_f9d2fd, p_435d0d, p_ccc6de)( qr[2] ))
circuit.append(Gates.PhaseGate(p_8c914c)( qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_435d0d": 1.2201500361327853,
    "p_3c07ca": 5.072633818750175,
    "p_ccc6de": 4.276690396183425,
    "p_f9d2fd": 3.8090985869250003,
    "p_6b41c3": 1.7910282654595102,
    "p_8c914c": 2.482034489972267
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

