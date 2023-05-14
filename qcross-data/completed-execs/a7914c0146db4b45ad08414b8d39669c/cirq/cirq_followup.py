
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_d78b4f = Symbol('p_d78b4f')
p_670928 = Symbol('p_670928')
p_3efaaf = Symbol('p_3efaaf')
p_779c94 = Symbol('p_779c94')
p_c2a67e = Symbol('p_c2a67e')
p_9e6f86 = Symbol('p_9e6f86')
p_637ac4 = Symbol('p_637ac4')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.CRZGate(p_779c94)( qr[6], qr[2] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[7] ))
circuit.append(Gates.RCCXGate( qr[10], qr[6], qr[8] ))
circuit.append(Gates.RZGate(p_d78b4f)( qr[0] ))
circuit.append(Gates.CCXGate( qr[7], qr[10], qr[2] ))
circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( qr[10] ))
circuit.append(Gates.CSXGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[0], qr[7] ))
circuit.append(Gates.CU1Gate(p_670928)( qr[9], qr[0] ))
circuit.append(Gates.RZGate(5.0063780207098425)( qr[6] ))
circuit.append(Gates.U2Gate(p_3efaaf, p_637ac4)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.RZZGate(p_9e6f86)( qr[4], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[5] ))
circuit.append(Gates.RZGate(p_c2a67e)( qr[2] ))
circuit.append(Gates.CRZGate(0.6393443962862078)( qr[5], qr[3] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))
circuit.append(cirq.measure(qr[10], key='cr10'))



circuit = cirq.resolve_parameters(circuit, {
    "p_d78b4f": 4.229610589867865,
    "p_670928": 4.028174522740928,
    "p_3efaaf": 2.5163050709890156,
    "p_779c94": 4.2641612072511235,
    "p_c2a67e": 4.722103101046168,
    "p_9e6f86": 3.950837470808744,
    "p_637ac4": 2.1276323672732023
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

