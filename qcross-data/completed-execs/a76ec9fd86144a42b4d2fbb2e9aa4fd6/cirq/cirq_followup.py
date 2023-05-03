
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054)( qr[2], qr[1] ))
circuit.append(Gates.CUGate(1.1871631023192395, 3.1208310247400375, 4.6969093516914615, 0.17758444859871442)( qr[2], qr[0] ))
circuit.append(Gates.CRYGate(0.6970696680696589)( qr[0], qr[1] ))
circuit.append(Gates.CSwapGate( qr[0], qr[3], qr[1] ))
circuit.append(Gates.RYGate(1.6125723299807893)( qr[1] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.RC3XGate( qr[0], qr[1], qr[2], qr[3] ))
circuit.append(Gates.C3XGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.CRYGate(4.258547097390385)( qr[3], qr[1] ))
circuit.append(Gates.RYGate(5.620914585085149)( qr[3] ))
circuit.append(Gates.PhaseGate(2.3677386437434818)( qr[3] ))
circuit.append(Gates.RYGate(1.8882312521616809)( qr[1] ))
circuit.append(Gates.RYGate(3.4959547081113205)( qr[3] ))
circuit.append(Gates.RYGate(5.99120670299654)( qr[3] ))
circuit.append(Gates.iSwapGate( qr[1], qr[2] ))
circuit.append(Gates.CUGate(5.709276284014425, 1.1243723913896708, 5.481400346001526, 3.157375188814291)( qr[0], qr[1] ))
circuit.append(Gates.PhaseGate(4.139653233556392)( qr[3] ))
circuit.append(Gates.CRYGate(1.9836175804480751)( qr[3], qr[2] ))
circuit.append(Gates.CSwapGate( qr[3], qr[0], qr[2] ))
circuit.append(Gates.U2Gate(2.0386602682603954, 6.248470925834253)( qr[3] ))
circuit.append(Gates.C3XGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.CUGate(2.945697832726557, 3.322311684185455, 2.468007457013939, 1.7221796439586554)( qr[3], qr[0] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.RC3XGate( qr[1], qr[3], qr[0], qr[2] ))
circuit.append(Gates.RYGate(0.8391711967546518)( qr[3] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.CXGate( qr[2], qr[0] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.CXGate( qr[2], qr[0] ))
circuit.append(Gates.CXGate( qr[1], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.CXGate( qr[1], qr[2] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.CXGate( qr[1], qr[2] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.C3XGate( qr[1], qr[0], qr[3], qr[2] ))
circuit.append(Gates.RXXGate(3.9517064865019407)( qr[3], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

