
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CUGate(2.0087468885271504, 5.883811190278971, 5.864947219205212, 5.7446598664897115)( qr[1], qr[0] ))
circuit.append(Gates.RXGate(5.794504209717704)( qr[1] ))
circuit.append(Gates.RZZGate(2.1663122372864825)( qr[1], qr[0] ))
circuit.append(Gates.DCXGate( qr[1], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.U2Gate(3.615801062466814, 0.8936944779843444)( qr[1] ))
circuit.append(Gates.RYGate(2.2562188139100248)( qr[1] ))
circuit.append(Gates.RYYGate(6.060522892419086)( qr[1], qr[0] ))
circuit.append(Gates.SwapGate( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SwapGate( qr[0], qr[1] ))
circuit.append(Gates.U3Gate(3.8927238245726374, 2.0377807006749333, 4.064217417062462)( qr[0] ))
circuit.append(Gates.RZGate(2.414915889738904)( qr[1] ))
circuit.append(Gates.CRYGate(2.594321777907923)( qr[1], qr[0] ))
circuit.append(Gates.RXGate(2.3571868764276998)( qr[1] ))
circuit.append(Gates.RZZGate(0.3644709100093532)( qr[0], qr[1] ))
circuit.append(Gates.RXGate(2.5276999718154167)( qr[1] ))
circuit.append(Gates.CZGate( qr[1], qr[0] ))
circuit.append(Gates.RZZGate(3.41477281916325)( qr[1], qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(Gates.U3Gate(5.170631856240322, 2.9463190555168968, 2.269493738638121)( qr[0] ))
circuit.append(Gates.U3Gate(2.481557449187282, 3.06771330185138, 2.2732733996544363)( qr[1] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.CUGate(0.8725199162352276, 2.0033484721527364, 1.6015864357317902, 4.9684596562340495)( qr[1], qr[0] ))
circuit.append(Gates.RYGate(5.8249335523617525)( qr[0] ))
circuit.append(Gates.RZGate(4.757508594558637)( qr[0] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.SwapGate( qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(3.137732232950496, 2.9454453048301827, 2.754468708884141)( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
