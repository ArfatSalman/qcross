
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_d09701 = Symbol('p_d09701')
p_8dd582 = Symbol('p_8dd582')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_d09701)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_8dd582)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.TGate( qr[2] ))
subcircuit.append(Gates.UGate(5.01836135520768, 5.190931186022931, 1.2128092629174942)( qr[3] ))
subcircuit.append(Gates.RC3XGate( qr[4], qr[0], qr[3], qr[1] ))
subcircuit.append(Gates.DCXGate( qr[2], qr[3] ))
subcircuit.append(Gates.CZGate( qr[1], qr[0] ))
subcircuit.append(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547)( qr[0], qr[1] ))
subcircuit.append(Gates.CPhaseGate(4.63837786161633)( qr[0], qr[2] ))
subcircuit.append(Gates.ECRGate( qr[3], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRZGate(1.0296448789776642)( qr[3], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_d09701": 6.163759533339787,
    "p_8dd582": 2.0099472182748075
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

