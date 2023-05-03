
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_f98f00 = Symbol('p_f98f00')
p_fa847a = Symbol('p_fa847a')
p_2ea8c6 = Symbol('p_2ea8c6')
p_40b755 = Symbol('p_40b755')
p_b0a2c5 = Symbol('p_b0a2c5')
p_2d39db = Symbol('p_2d39db')
p_6111e9 = Symbol('p_6111e9')
p_37d8a3 = Symbol('p_37d8a3')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_f98f00)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_2d39db)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_b0a2c5)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_2ea8c6, p_fa847a, p_6111e9, 3.865496458458116)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_40b755)( qr[3], qr[0] ))
circuit.append(Gates.UGate(5.887184334931191, p_37d8a3, 1.4112277317699358)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_f98f00": 6.163759533339787,
    "p_fa847a": 4.167661441102218,
    "p_2ea8c6": 5.708725119517347,
    "p_40b755": 3.2142159669963557,
    "p_b0a2c5": 1.0296448789776642,
    "p_2d39db": 2.0099472182748075,
    "p_6111e9": 4.623446645668956,
    "p_37d8a3": 0.07157463504881167
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

