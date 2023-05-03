
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RCCXGate( qr[1], qr[2], qr[0] ))
subcircuit.append(Gates.SXGate( qr[0] ))
subcircuit.append(Gates.CU3Gate(6.086884486572108, 3.06538533241841, 1.7532443887147882)( qr[1], qr[2] ))
subcircuit.append(Gates.U3Gate(5.01836135520768, 5.190931186022931, 1.2128092629174942)( qr[0] ))
subcircuit.append(Gates.CYGate( qr[2], qr[0] ))
subcircuit.append(Gates.RYGate(6.1292830756636185)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[2], qr[1] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.CCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[0], key='cr1'))
circuit.append(cirq.measure(qr[1], key='cr2'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

