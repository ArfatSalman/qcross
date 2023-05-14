
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("CRZGate", "C3SXGate", "CRXGate", "RZGate", "XGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 7, 2 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 4, 2 ))
circuit.inst(Gates.C3SXGate( 7, 0, 2, 1 ))
circuit.inst(Gates.ZGate( 6 ))

circuit += MEASURE(7, qr[0])
circuit += MEASURE(4, qr[1])
circuit += MEASURE(6, qr[2])
circuit += MEASURE(1, qr[3])
circuit += MEASURE(3, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(2, qr[6])
circuit += MEASURE(0, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })
