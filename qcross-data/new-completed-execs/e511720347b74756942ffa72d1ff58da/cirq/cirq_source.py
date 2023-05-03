
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.CYGate( qr[1], qr[3] ))
circuit.append(Gates.CSdgGate( qr[2], qr[0] ))
circuit.append(Gates.U2Gate(6.224224267022873, 0.5062108542599196)( qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.RXXGate(2.849709666292305)( qr[2], qr[0] ))
circuit.append(Gates.CUGate(1.4830756139727388, 4.336270484416077, 4.496803337305518, 0.23255854856360128)( qr[2], qr[0] ))
circuit.append(Gates.U1Gate(3.989772590171974)( qr[2] ))
circuit.append(Gates.RVGate(2.3749233592982653, 1.242766903811508, 5.902936157186667)( qr[1] ))
circuit.append(Gates.CCXGate( qr[2], qr[1], qr[3] ))
circuit.append(Gates.RGate(5.3389684124335135, 4.983335490773843)( qr[0] ))
circuit.append(Gates.CU3Gate(2.9985355066762964, 4.6584355985305175, 5.286009370798176)( qr[1], qr[2] ))
circuit.append(Gates.U1Gate(1.23766565597922)( qr[1] ))
circuit.append(Gates.CRYGate(0.7050339438266124)( qr[3], qr[0] ))
circuit.append(Gates.CU3Gate(0.26880077817102677, 4.703772321262758, 2.2003352220865064)( qr[0], qr[3] ))
circuit.append(Gates.RXXGate(1.7988659594922651)( qr[1], qr[3] ))
circuit.append(Gates.CZGate( qr[3], qr[2] ))
circuit.append(Gates.U1Gate(3.091046473463947)( qr[2] ))
circuit.append(Gates.CU3Gate(4.07826629550777, 0.6948315212195522, 3.971785158778898)( qr[1], qr[0] ))
circuit.append(Gates.RZGate(6.114994939448648)( qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.U1Gate(3.885678856232139)( qr[1] ))
circuit.append(Gates.U3Gate(1.3122881955531616, 0.33578911439943154, 4.332701855049643)( qr[1] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CSwapGate( qr[3], qr[0], qr[1] ))
circuit.append(Gates.CZGate( qr[3], qr[2] ))
circuit.append(Gates.U3Gate(0.07989271098060978, 3.2475433527931767, 3.3028156122014454)( qr[0] ))
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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

