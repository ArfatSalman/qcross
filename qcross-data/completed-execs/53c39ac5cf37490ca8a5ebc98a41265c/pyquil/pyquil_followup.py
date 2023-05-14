
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("RZZGate", "RZXGate", "RZGate", "CU3Gate", "CRZGate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.RZZGate(1.927446989780488)( 9, 4 ))
subcircuit.inst(Gates.CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789, 10, 6 ))
subcircuit.inst(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547, 0, 10 ))
subcircuit.inst(Gates.RZXGate(4.563562108824195)( 4, 8 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

