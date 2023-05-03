
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.ECRGate( qr[1], qr[7] ))
circuit.append(Gates.RC3XGate( qr[1], qr[0], qr[5], qr[6] ))
circuit.append(Gates.CPhaseGate(0.7207706407070019)( qr[4], qr[3] ))
circuit.append(Gates.DCXGate( qr[3], qr[4] ))
circuit.append(Gates.RCCXGate( qr[2], qr[1], qr[4] ))
circuit.append(Gates.SwapGate( qr[6], qr[5] ))
circuit.append(Gates.iSwapGate( qr[4], qr[7] ))
circuit.append(Gates.RXGate(4.802467793465571)( qr[0] ))
circuit.append(Gates.iSwapGate( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(3.4625444838065618)( qr[0], qr[6] ))
circuit.append(Gates.CSwapGate( qr[0], qr[3], qr[6] ))
circuit.append(Gates.RGate(5.104156300804455, 6.227137798959555)( qr[0] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.RXXGate(6.256338963756067)( qr[1], qr[5] ))
circuit.append(Gates.DCXGate( qr[7], qr[6] ))
circuit.append(Gates.RYGate(2.803631472128793)( qr[3] ))
circuit.append(Gates.RC3XGate( qr[4], qr[3], qr[1], qr[2] ))
circuit.append(Gates.CU1Gate(1.5456697172063534)( qr[7], qr[6] ))
circuit.append(Gates.RYGate(4.278284783932528)( qr[7] ))
circuit.append(Gates.RCCXGate( qr[7], qr[2], qr[0] ))
circuit.append(Gates.RGate(0.2852105385229711, 5.142516617776941)( qr[2] ))
circuit.append(Gates.RXXGate(2.2028067729502347)( qr[1], qr[6] ))
circuit.append(Gates.RXGate(1.732522506962926)( qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[1], qr[6] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.IGate( qr[3] ))
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

