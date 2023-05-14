
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("ECRGate", "C3SXGate", "CRXGate", "RZGate", "XGate", "ZGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 0, 4 ))
circuit.inst(Gates.C3SXGate( 5, 2, 6, 0 ))
circuit.inst(Gates.CHGate( 1, 5 ))
circuit.inst(Gates.C3SXGate( 2, 0, 6, 4 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ECRGate( 5, 3 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(6, qr[1])
circuit += MEASURE(0, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(1, qr[4])
circuit += MEASURE(4, qr[5])
circuit += MEASURE(5, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

