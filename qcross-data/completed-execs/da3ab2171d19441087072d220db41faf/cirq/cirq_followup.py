
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_28ea63 = Symbol('p_28ea63')
p_651c14 = Symbol('p_651c14')
p_3602d5 = Symbol('p_3602d5')
p_72aff8 = Symbol('p_72aff8')
p_169af4 = Symbol('p_169af4')
p_0a613b = Symbol('p_0a613b')
p_9cbb9b = Symbol('p_9cbb9b')
p_5bab06 = Symbol('p_5bab06')
p_878acf = Symbol('p_878acf')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_9cbb9b)( qr[3] ))
circuit.append(Gates.CRZGate(p_28ea63)( qr[6], qr[2] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[7] ))
circuit.append(Gates.RCCXGate( qr[10], qr[6], qr[8] ))
circuit.append(Gates.RZGate(p_651c14)( qr[0] ))
circuit.append(Gates.CCXGate( qr[7], qr[10], qr[2] ))
circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.U2Gate(4.214504315296764, p_169af4)( qr[10] ))
circuit.append(Gates.CSXGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[0], qr[7] ))
circuit.append(Gates.CU1Gate(p_72aff8)( qr[9], qr[0] ))
circuit.append(Gates.RZGate(p_5bab06)( qr[6] ))
circuit.append(Gates.U2Gate(p_0a613b, p_878acf)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.RZZGate(p_3602d5)( qr[4], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
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
    "p_28ea63": 4.2641612072511235,
    "p_651c14": 4.229610589867865,
    "p_3602d5": 3.950837470808744,
    "p_72aff8": 4.028174522740928,
    "p_169af4": 4.6235667602042065,
    "p_0a613b": 2.5163050709890156,
    "p_9cbb9b": 6.163759533339787,
    "p_5bab06": 5.0063780207098425,
    "p_878acf": 2.1276323672732023
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

