
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.YGate( qr[8] ))
circuit.append(Gates.CU3Gate(1.137265035582176, 1.9191341652886187, 2.035659400824786)( qr[2], qr[5] ))
circuit.append(Gates.ECRGate( qr[4], qr[1] ))
circuit.append(Gates.HGate( qr[8] ))
circuit.append(Gates.CRZGate(5.5072773697390085)( qr[5], qr[0] ))
circuit.append(Gates.RXGate(4.368068524516866)( qr[9] ))
circuit.append(Gates.CZGate( qr[6], qr[1] ))
circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.CRYGate(4.03209544447551)( qr[1], qr[4] ))
circuit.append(Gates.SwapGate( qr[9], qr[2] ))
circuit.append(Gates.YGate( qr[9] ))
circuit.append(Gates.SwapGate( qr[0], qr[8] ))
circuit.append(Gates.SXdgGate( qr[3] ))
circuit.append(Gates.ECRGate( qr[3], qr[7] ))
circuit.append(Gates.DCXGate( qr[9], qr[1] ))
circuit.append(Gates.CCXGate( qr[8], qr[2], qr[3] ))
circuit.append(Gates.YGate( qr[7] ))
circuit.append(Gates.C3SXGate( qr[7], qr[3], qr[5], qr[1] ))
circuit.append(Gates.U3Gate(1.6951114914418934, 5.599301713249363, 3.1864266503972143)( qr[4] ))
circuit.append(Gates.RXGate(5.528457770513217)( qr[7] ))
circuit.append(Gates.C3SXGate( qr[2], qr[6], qr[1], qr[7] ))
circuit.append(Gates.CSwapGate( qr[9], qr[3], qr[1] ))
circuit.append(Gates.RZZGate(3.5190638597992265)( qr[8], qr[5] ))
circuit.append(Gates.SXdgGate( qr[6] ))
circuit.append(Gates.HGate( qr[6] ))
circuit.append(Gates.RZXGate(3.656646631785722)( qr[0], qr[9] ))
circuit.append(Gates.HGate( qr[3] ))
circuit.append(Gates.XGate( qr[7] ))
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













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

