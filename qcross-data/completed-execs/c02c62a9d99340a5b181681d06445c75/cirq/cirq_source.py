
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.RZXGate(5.294170317838349)( qr[2], qr[4] ))
circuit.append(Gates.SwapGate( qr[1], qr[5] ))
circuit.append(Gates.U3Gate(5.951221312078038, 5.377869177229497, 4.13307667574035)( qr[2] ))
circuit.append(Gates.ECRGate( qr[4], qr[1] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.YGate( qr[4] ))
circuit.append(Gates.U3Gate(3.127390581057496, 0.8951620930728853, 2.9211253533322705)( qr[4] ))
circuit.append(Gates.CPhaseGate(3.2345621726383063)( qr[3], qr[0] ))
circuit.append(Gates.CRYGate(1.5739612232900921)( qr[4], qr[0] ))
circuit.append(Gates.ECRGate( qr[1], qr[2] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.RXGate(2.1921350525840335)( qr[1] ))
circuit.append(Gates.CRYGate(4.81139250369156)( qr[0], qr[3] ))
circuit.append(Gates.CU3Gate(0.5792738051909873, 5.615330906310357, 2.660875175684596)( qr[5], qr[0] ))
circuit.append(Gates.IGate( qr[0] ))
circuit.append(Gates.U2Gate(4.245494087381378, 0.35899282563221724)( qr[0] ))
circuit.append(Gates.UGate(1.0608924835540103, 2.415674942808992, 0.8187346879786549)( qr[3] ))
circuit.append(Gates.DCXGate( qr[0], qr[1] ))
circuit.append(Gates.RXGate(5.956960136241147)( qr[3] ))
circuit.append(Gates.DCXGate( qr[4], qr[5] ))
circuit.append(Gates.U3Gate(1.5683345978951369, 1.4287408195765756, 2.3460687004856973)( qr[1] ))
circuit.append(Gates.CU1Gate(1.9757038692524151)( qr[3], qr[1] ))
circuit.append(Gates.U3Gate(0.4602821600746163, 5.414451003251248, 4.293440251468374)( qr[4] ))
circuit.append(Gates.CZGate( qr[4], qr[3] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.RYYGate(4.463598643942479)( qr[1], qr[5] ))
circuit.append(Gates.CU3Gate(3.8745722202781416, 3.2737382848299332, 3.2686683844993465)( qr[5], qr[0] ))
circuit.append(Gates.SdgGate( qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
