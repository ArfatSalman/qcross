
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("RVGate", "CSdgGate", "SdgGate", "PhaseGate", "CRYGate", "iSwapGate", "CUGate", "U1Gate", "CRZGate")

circuit += defns

circuit.inst(Gates.CRYGate(4.682220755041814, 0, 1 ))
circuit.inst(Gates.CUGate(5.960866266876448, 5.945098421875394, 4.418481228600101, 3.972623244718876, 1, 0 ))
circuit.inst(Gates.PhaseGate(2.031442273399285, 0 ))
circuit.inst(Gates.U1Gate(1.1449128292629545, 1 ))
circuit.inst(Gates.CRYGate(1.8638911468677428, 0, 1 ))
circuit.inst(Gates.CSdgGate( 0, 1 ))
circuit.inst(Gates.RVGate(3.2561786456517483, 4.027853623334148, 0.7501118686992972)( 1 ))
circuit.inst(Gates.PhaseGate(3.1265936864110326, 0 ))
circuit.inst(Gates.PhaseGate(2.7301494704572584, 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRZGate(2.967811594681098, 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

