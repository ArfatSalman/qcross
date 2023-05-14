
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_b55b30 = Symbol('p_b55b30')
p_5d3d3d = Symbol('p_5d3d3d')
p_48d37c = Symbol('p_48d37c')
p_5d4f5c = Symbol('p_5d4f5c')
p_c95cea = Symbol('p_c95cea')
p_806bcc = Symbol('p_806bcc')
p_e6233a = Symbol('p_e6233a')
p_c8910e = Symbol('p_c8910e')
p_78f4ca = Symbol('p_78f4ca')
p_f29331 = Symbol('p_f29331')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_806bcc)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_b55b30)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_e6233a)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_c95cea)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_78f4ca)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_5d3d3d)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_f29331)( qr[4] ))
circuit.append(Gates.CRXGate(0.7279391018916035)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(5.03147076606842, 5.0063780207098425, p_5d4f5c, 4.940217775579305)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_c8910e, 2.1276323672732023)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(p_48d37c)( qr[3], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_b55b30": 5.987304452123941,
    "p_5d3d3d": 5.1829934776392745,
    "p_48d37c": 3.950837470808744,
    "p_5d4f5c": 3.1562533916051736,
    "p_c95cea": 4.229610589867865,
    "p_806bcc": 6.163759533339787,
    "p_e6233a": 4.167661441102218,
    "p_c8910e": 2.5163050709890156,
    "p_78f4ca": 5.94477504571567,
    "p_f29331": 3.775592041307464
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

