
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_ec106f = Symbol('p_ec106f')
p_5f113d = Symbol('p_5f113d')
p_cf8439 = Symbol('p_cf8439')
p_7e38fe = Symbol('p_7e38fe')
p_50c455 = Symbol('p_50c455')
p_e13c2b = Symbol('p_e13c2b')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_ec106f)( qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.U3Gate(p_7e38fe, p_5f113d, 0.4903361071050254)( qr[1] ))
subcircuit.append(Gates.IGate( qr[2] ))
subcircuit.append(Gates.UGate(p_e13c2b, p_50c455, p_cf8439)( qr[4] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRZGate(4.2641612072511235)( qr[6], qr[2] ))
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
    "p_ec106f": 6.163759533339787,
    "p_5f113d": 5.154187354656876,
    "p_cf8439": 1.2128092629174942,
    "p_7e38fe": 4.094867647151279,
    "p_50c455": 5.190931186022931,
    "p_e13c2b": 5.01836135520768
}, recursive=True)
        

UNITARY = cirq.unitary(circuit)








simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

