
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.U3Gate(0.7525107922079248, 1.2447972626729948, 5.921099882361809)( qr[2] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.CU3Gate(3.5951128532694563, 0.010919193816599988, 3.645329450090628)( qr[0], qr[2] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.U2Gate(2.2781042293610834, 2.8111390321344745)( qr[1] ))
circuit.append(Gates.IGate( qr[0] ))
circuit.append(Gates.CRYGate(5.388940796049925)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(5.5431459174826, 1.3400715972886643)( qr[0] ))
circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(Gates.U2Gate(0.15471247054287984, 2.4400424648148045)( qr[1] ))
circuit.append(Gates.YGate( qr[0] ))
circuit.append(Gates.RZZGate(5.7575659278310845)( qr[0], qr[2] ))
circuit.append(Gates.U1Gate(1.4699956697302532)( qr[1] ))
circuit.append(Gates.CUGate(1.0304702852384158, 2.6685497827460365, 3.99549985610294, 5.662035192382266)( qr[1], qr[2] ))
circuit.append(Gates.CRYGate(3.4267977136464998)( qr[1], qr[2] ))
circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.TdgGate( qr[0] ))
circuit.append(Gates.RYGate(3.7754558724472616)( qr[1] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.U3Gate(6.01948050450523, 2.72714859557862, 3.399676447189968)( qr[0] ))
circuit.append(Gates.RZZGate(0.3954282502495691)( qr[0], qr[2] ))
circuit.append(Gates.U3Gate(1.9629138136015831, 3.495764555095602, 4.032386816161946)( qr[2] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CU3Gate(3.8725614355577274, 3.7233769818737543, 0.6129863346305541)( qr[0], qr[1] ))
circuit.append(Gates.U1Gate(2.410525914389015)( qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.TdgGate( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
