
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.CPhaseGate(0.464603434869698)( qr[3], qr[0] ))
circuit.append(Gates.RC3XGate( qr[1], qr[2], qr[3], qr[0] ))
circuit.append(Gates.CU3Gate(4.577871395666417, 2.824995733037649, 4.570764402928323)( qr[2], qr[0] ))
circuit.append(Gates.YGate( qr[2] ))
circuit.append(Gates.RC3XGate( qr[1], qr[3], qr[0], qr[2] ))
circuit.append(Gates.SwapGate( qr[3], qr[0] ))
circuit.append(Gates.SwapGate( qr[0], qr[1] ))
circuit.append(Gates.RYGate(4.123988453145662)( qr[3] ))
circuit.append(Gates.RXGate(5.977019956470354)( qr[0] ))
circuit.append(Gates.RYGate(5.340081963621594)( qr[0] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(Gates.RZGate(0.902460456423349)( qr[2] ))
circuit.append(Gates.U1Gate(1.191082687926663)( qr[3] ))
circuit.append(Gates.RYGate(2.426038592845313)( qr[3] ))
circuit.append(Gates.CPhaseGate(1.9801508534447856)( qr[2], qr[0] ))
circuit.append(Gates.U1Gate(0.7620531016010672)( qr[3] ))
circuit.append(Gates.RZGate(1.1210417983863055)( qr[0] ))
circuit.append(Gates.C3XGate( qr[3], qr[2], qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(3.3468514586446996, 0.09605123198475385, 1.9104022337738353)( qr[2], qr[0] ))
circuit.append(Gates.RYGate(5.21436875895587)( qr[2] ))
circuit.append(Gates.RYGate(1.876889866834255)( qr[2] ))
circuit.append(Gates.U3Gate(3.580262460733749, 2.5952409532269898, 0.3968947480833723)( qr[2] ))
circuit.append(Gates.U1Gate(1.8511699871735552)( qr[0] ))
circuit.append(Gates.RYYGate(0.8500918394546497)( qr[2], qr[0] ))
circuit.append(Gates.CU3Gate(1.4776100383750288, 4.796549499287292, 5.831783083594262)( qr[3], qr[1] ))
circuit.append(Gates.C3XGate( qr[2], qr[0], qr[3], qr[1] ))
circuit.append(Gates.CU3Gate(2.6606132436968934, 0.25042616078481367, 0.47890039592537104)( qr[3], qr[0] ))
circuit.append(Gates.RXGate(5.381463645700576)( qr[0] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
