
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.RGate(1.3462943863788401, 2.0625679674283215)( qr[2] ))
circuit.append(Gates.RYGate(3.7263733381135333)( qr[4] ))
circuit.append(Gates.CRZGate(3.624574776344154)( qr[7], qr[3] ))
circuit.append(Gates.CUGate(2.7575077791457248, 2.0665317573057798, 5.876304122002991, 5.455724865836178)( qr[3], qr[0] ))
circuit.append(Gates.RZZGate(6.059622421697095)( qr[2], qr[6] ))
circuit.append(Gates.C4XGate( qr[0], qr[4], qr[1], qr[5], qr[6] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[2], qr[4] ))
circuit.append(Gates.SXdgGate( qr[6] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.CRZGate(3.472333959218345)( qr[7], qr[3] ))
circuit.append(Gates.CRYGate(2.364247849527231)( qr[7], qr[1] ))
circuit.append(Gates.CRZGate(0.8522442036798011)( qr[6], qr[4] ))
circuit.append(Gates.RGate(0.44671874703610037, 4.595620654661833)( qr[3] ))
circuit.append(Gates.SXGate( qr[3] ))
circuit.append(Gates.DCXGate( qr[1], qr[5] ))
circuit.append(Gates.CUGate(2.010079880074799, 3.570167881942785, 3.7199764092307213, 0.8777762419082662)( qr[6], qr[4] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.CRXGate(5.895791450120457)( qr[0], qr[5] ))
circuit.append(Gates.CU3Gate(2.3777076314685166, 0.2787777190001789, 6.013755670278601)( qr[5], qr[6] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

