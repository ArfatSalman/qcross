
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_8c8820 = Symbol('p_8c8820')
p_946556 = Symbol('p_946556')
p_693dd5 = Symbol('p_693dd5')
p_b9f99b = Symbol('p_b9f99b')
p_d01756 = Symbol('p_d01756')
p_df5015 = Symbol('p_df5015')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_8c8820)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(p_b9f99b)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_693dd5, 4.167661441102218, 4.623446645668956, 3.865496458458116)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.RYYGate(p_946556)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(5.887184334931191, p_df5015, p_d01756)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_8c8820": 6.163759533339787,
    "p_946556": 5.398622178940033,
    "p_693dd5": 5.708725119517347,
    "p_b9f99b": 1.6723037552953224,
    "p_d01756": 1.4112277317699358,
    "p_df5015": 0.07157463504881167
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

