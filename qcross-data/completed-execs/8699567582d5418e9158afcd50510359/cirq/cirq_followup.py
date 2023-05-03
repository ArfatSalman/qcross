
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.CYGate( qr[0], qr[6] ))
circuit.append(Gates.U1Gate(3.321288277959951)( qr[2] ))
circuit.append(Gates.YGate( qr[3] ))
circuit.append(Gates.ECRGate( qr[5], qr[1] ))
circuit.append(Gates.RZGate(3.0238378046938514)( qr[6] ))
circuit.append(Gates.iSwapGate( qr[3], qr[6] ))
circuit.append(Gates.ECRGate( qr[4], qr[3] ))
circuit.append(Gates.RCCXGate( qr[2], qr[5], qr[3] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.PhaseGate(0.2289483555541983)( qr[3] ))
circuit.append(Gates.CYGate( qr[5], qr[7] ))
circuit.append(Gates.PhaseGate(4.268329737032283)( qr[4] ))
circuit.append(Gates.CSwapGate( qr[2], qr[3], qr[7] ))
circuit.append(Gates.UGate(0.7278978053151748, 5.145064315568138, 1.7503156588884659)( qr[2] ))
circuit.append(Gates.C4XGate( qr[4], qr[1], qr[2], qr[6], qr[8] ))
circuit.append(Gates.RZZGate(6.262915463363716)( qr[9], qr[7] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.ECRGate( qr[2], qr[7] ))
circuit.append(Gates.RZZGate(2.0261195842682675)( qr[7], qr[5] ))
circuit.append(Gates.U1Gate(0.5870983336064636)( qr[0] ))
circuit.append(Gates.RZZGate(4.586260430147017)( qr[7], qr[9] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.C3XGate( qr[6], qr[3], qr[8], qr[4] ))
circuit.append(Gates.C4XGate( qr[0], qr[7], qr[5], qr[6], qr[4] ))
circuit.append(Gates.CSXGate( qr[9], qr[4] ))
circuit.append(Gates.C4XGate( qr[0], qr[8], qr[9], qr[5], qr[2] ))
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













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
