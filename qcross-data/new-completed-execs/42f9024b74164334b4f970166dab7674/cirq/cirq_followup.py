
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

p_f5ce15 = Symbol('p_f5ce15')
p_fa05b6 = Symbol('p_fa05b6')
p_75b77c = Symbol('p_75b77c')
p_e32c43 = Symbol('p_e32c43')
p_d9b3a9 = Symbol('p_d9b3a9')
p_415e22 = Symbol('p_415e22')
p_6c6aa2 = Symbol('p_6c6aa2')
p_66d326 = Symbol('p_66d326')
p_cf1375 = Symbol('p_cf1375')
p_9b1974 = Symbol('p_9b1974')
p_638ece = Symbol('p_638ece')
p_ee1794 = Symbol('p_ee1794')

circuit = cirq.Circuit()

circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.UGate(p_415e22, p_66d326, p_fa05b6)( qr[1] ))
circuit.append(Gates.RGate(3.9800961208659213, p_9b1974)( qr[0] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(Gates.CRXGate(p_f5ce15)( qr[1], qr[0] ))
circuit.append(Gates.CSdgGate( qr[0], qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.CU3Gate(p_6c6aa2, p_638ece, p_e32c43)( qr[0], qr[1] ))
circuit.append(Gates.CZGate( qr[1], qr[0] ))
circuit.append(Gates.RGate(p_ee1794, p_d9b3a9)( qr[1] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.UGate(p_75b77c, p_cf1375, 5.6467633400840755)( qr[1] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))



circuit = cirq.resolve_parameters(circuit, {
    "p_f5ce15": 3.0761375449158193,
    "p_fa05b6": 2.414376925356305,
    "p_75b77c": 3.820196974130503,
    "p_e32c43": 2.251031643786726,
    "p_d9b3a9": 4.7611258330830655,
    "p_415e22": 4.403788193532198,
    "p_6c6aa2": 3.359364374345002,
    "p_66d326": 5.238005217278175,
    "p_cf1375": 1.381440535002157,
    "p_9b1974": 2.54258238968427,
    "p_638ece": 4.018048446348199,
    "p_ee1794": 4.3040860238694725
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

