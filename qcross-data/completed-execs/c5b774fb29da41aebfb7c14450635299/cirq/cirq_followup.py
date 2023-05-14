
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_52c643 = Symbol('p_52c643')
p_827e55 = Symbol('p_827e55')
p_8ff258 = Symbol('p_8ff258')
p_7054b2 = Symbol('p_7054b2')
p_e129ef = Symbol('p_e129ef')
p_11ec22 = Symbol('p_11ec22')
p_d24d8a = Symbol('p_d24d8a')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_e129ef)( qr[1] ))
circuit.append(Gates.RZZGate(p_52c643)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_11ec22, p_d24d8a, p_827e55, p_8ff258)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_7054b2)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_52c643": 4.066449154047175,
    "p_827e55": 2.3864521352475245,
    "p_8ff258": 5.987304452123941,
    "p_7054b2": 5.154187354656876,
    "p_e129ef": 6.163759533339787,
    "p_11ec22": 0.5112149185250571,
    "p_d24d8a": 5.897054719225356
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

