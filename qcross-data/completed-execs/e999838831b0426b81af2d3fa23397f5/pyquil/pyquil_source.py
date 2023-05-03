
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("U3Gate", "DCXGate", "RYGate", "RZGate", "CPhaseGate", "HGate", "RYYGate", "U1Gate")

circuit += defns

circuit.inst(Gates.U3Gate(4.655749679598676, 2.7381706999194857, 2.740795817289426)( 0 ))
circuit.inst(Gates.RYYGate(5.171156764260811)( 2, 1 ))
circuit.inst(Gates.DCXGate( 2, 0 ))
circuit.inst(Gates.U1Gate(4.660569462447812, 1 ))
circuit.inst(Gates.CPhaseGate(5.442036812415247, 1, 0 ))
circuit.inst(Gates.RYGate(3.1620892961233205, 2 ))
circuit.inst(Gates.RZGate(2.816396898940768, 2 ))
circuit.inst(Gates.HGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

