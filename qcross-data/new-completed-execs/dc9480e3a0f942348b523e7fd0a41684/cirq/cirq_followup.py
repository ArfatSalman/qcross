
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]



circuit = cirq.Circuit()

circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.CRYGate(1.852579362704606)( qr[4], qr[7] ))
circuit.append(Gates.CYGate( qr[9], qr[0] ))
circuit.append(Gates.RXGate(5.276411432143827)( qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.U1Gate(2.825051590836995)( qr[1] ))
circuit.append(Gates.RC3XGate( qr[8], qr[9], qr[1], qr[5] ))
circuit.append(Gates.RYYGate(0.7867209387701732)( qr[7], qr[9] ))
circuit.append(Gates.UGate(4.576754367736335, 5.4109147050480955, 1.7256413064705036)( qr[7] ))
circuit.append(Gates.RC3XGate( qr[3], qr[5], qr[1], qr[4] ))
circuit.append(Gates.RVGate(5.6896213477612445, 6.047339853997451, 5.623943529608011)( qr[7] ))
circuit.append(Gates.UGate(3.0132549867885063, 6.182661801638049, 5.885160602032744)( qr[7] ))
circuit.append(Gates.HGate( qr[4] ))
circuit.append(Gates.RVGate(4.1249177878170915, 6.0745761147209345, 2.4099754200724317)( qr[0] ))
circuit.append(Gates.CYGate( qr[10], qr[2] ))
circuit.append(Gates.HGate( qr[8] ))
circuit.append(Gates.UGate(2.169150328031207, 1.7114617170345237, 2.307521863987498)( qr[2] ))
circuit.append(Gates.UGate(5.430643357287303, 0.6530454683497888, 3.836596788250059)( qr[10] ))
circuit.append(Gates.RZXGate(5.431264813579931)( qr[1], qr[3] ))
circuit.append(Gates.CUGate(2.9821700362780588, 1.3852421816440175, 4.785976176026314, 1.3657070275541772)( qr[4], qr[2] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.RCCXGate( qr[9], qr[3], qr[6] ))
circuit.append(Gates.RC3XGate( qr[10], qr[8], qr[9], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RVGate(5.050073208732572, 2.867190134610833, 1.0118283033144115)( qr[2] ))
circuit.append(Gates.RXXGate(1.2634039528117698)( qr[1], qr[6] ))
circuit.append(Gates.RVGate(0.5734726823505982, 3.854641723491838, 1.0422555828622841)( qr[7] ))
circuit.append(Gates.C3SXGate( qr[9], qr[10], qr[2], qr[8] ))
circuit.append(cirq.measure(qr[8], key='cr0'))
circuit.append(cirq.measure(qr[6], key='cr1'))
circuit.append(cirq.measure(qr[3], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[10], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[0], key='cr6'))
circuit.append(cirq.measure(qr[1], key='cr7'))
circuit.append(cirq.measure(qr[7], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))
circuit.append(cirq.measure(qr[2], key='cr10'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

