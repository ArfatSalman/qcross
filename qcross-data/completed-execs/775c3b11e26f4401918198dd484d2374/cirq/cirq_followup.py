
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_c99d8f = Symbol('p_c99d8f')
p_9cd4bb = Symbol('p_9cd4bb')
p_bacf18 = Symbol('p_bacf18')
p_a85ee4 = Symbol('p_a85ee4')
p_a479d9 = Symbol('p_a479d9')
p_85569c = Symbol('p_85569c')
p_8880d3 = Symbol('p_8880d3')
p_fece30 = Symbol('p_fece30')
p_dd152f = Symbol('p_dd152f')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_bacf18)( qr[1] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.U2Gate(p_85569c, p_8880d3)( qr[2] ))
subcircuit.append(Gates.IGate( qr[1] ))
subcircuit.append(Gates.RCCXGate( qr[2], qr[0], qr[1] ))
subcircuit.append(Gates.SXGate( qr[1] ))
subcircuit.append(Gates.CU3Gate(6.086884486572108, p_a479d9, p_dd152f)( qr[2], qr[0] ))
subcircuit.append(Gates.U3Gate(p_fece30, p_a85ee4, p_9cd4bb)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.iSwapGate( qr[2], qr[1] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.CRXGate(p_c99d8f)( qr[0], qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_c99d8f": 5.987304452123941,
    "p_9cd4bb": 1.2128092629174942,
    "p_bacf18": 6.163759533339787,
    "p_a85ee4": 5.190931186022931,
    "p_a479d9": 3.06538533241841,
    "p_85569c": 0.03501337194718552,
    "p_8880d3": 2.6397681660693015,
    "p_fece30": 5.01836135520768,
    "p_dd152f": 1.7532443887147882
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

