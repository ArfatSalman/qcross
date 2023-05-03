
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.CRYGate(5.084522291571211)( qr[1], qr[0] ))
circuit.append(Gates.CRYGate(0.5214443205823275)( qr[0], qr[1] ))
circuit.append(Gates.UGate(5.249389156861369, 5.506136172902856, 5.236656888622806)( qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.CU3Gate(1.3702172143092286, 1.9059592606091926, 5.782626030792982)( qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(3.371102520538735, 2.998573490180536, 1.776109337694477)( qr[1], qr[0] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.UGate(4.284938125077518, 1.0148536455132817, 2.487168338274746)( qr[0] ))
circuit.append(Gates.RYGate(3.900848522710214)( qr[0] ))
circuit.append(Gates.RZGate(2.334985126003777)( qr[1] ))
circuit.append(Gates.RYGate(1.7484204274088997)( qr[0] ))
circuit.append(Gates.TdgGate( qr[0] ))
circuit.append(Gates.CU3Gate(4.742430815090222, 1.8154225091000729, 3.693501832396555)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RZGate(5.556271444847221)( qr[1] ))
circuit.append(Gates.CRZGate(1.6719873041871378)( qr[1], qr[0] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.U2Gate(3.6951879813098216, 4.977624965840704)( qr[1] ))
circuit.append(Gates.CU3Gate(5.4144948963161035, 6.127785368788657, 2.137798063823039)( qr[1], qr[0] ))
circuit.append(Gates.U2Gate(4.611032125076666, 2.7074003913270643)( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.U2Gate(6.108789748804481, 2.1969367629951018)( qr[0] ))
circuit.append(Gates.RYGate(2.811127302481191)( qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
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
