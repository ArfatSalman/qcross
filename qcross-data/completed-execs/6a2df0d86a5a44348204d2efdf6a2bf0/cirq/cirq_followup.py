
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

p_311c30 = Symbol('p_311c30')
p_ef6cfa = Symbol('p_ef6cfa')
p_5c92ee = Symbol('p_5c92ee')
p_f8cd13 = Symbol('p_f8cd13')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_311c30)( qr[1] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.CRXGate(p_5c92ee)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[5], qr[4], qr[6], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[5] ))
circuit.append(Gates.C3SXGate( qr[4], qr[2], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[5], qr[0] ))
circuit.append(Gates.SdgGate( qr[5] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[6] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[6] ))
circuit.append(Gates.C3SXGate( qr[4], qr[2], qr[6], qr[0] ))
circuit.append(Gates.CU1Gate(p_f8cd13)( qr[1], qr[4] ))
circuit.append(Gates.CRXGate(p_ef6cfa)( qr[1], qr[5] ))
circuit.append(cirq.measure(qr[4], key='cr0'))
circuit.append(cirq.measure(qr[6], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[0], key='cr3'))
circuit.append(cirq.measure(qr[1], key='cr4'))
circuit.append(cirq.measure(qr[3], key='cr5'))
circuit.append(cirq.measure(qr[5], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_311c30": 6.163759533339787,
    "p_ef6cfa": 5.94477504571567,
    "p_5c92ee": 2.0099472182748075,
    "p_f8cd13": 3.2142159669963557
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

