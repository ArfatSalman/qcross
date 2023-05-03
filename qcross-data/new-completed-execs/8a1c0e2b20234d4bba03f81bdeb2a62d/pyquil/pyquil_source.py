
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("CPhaseGate", "PhaseGate", "CHGate", "U1Gate", "UGate")

circuit += defns

circuit.inst(Gates.CPhaseGate(1.7910282654595102, 1, 2 ))
circuit.inst(Gates.U1Gate(5.072633818750175, 2 ))
circuit.inst(Gates.UGate(3.8090985869250003, 1.2201500361327853, 4.276690396183425)( 2 ))
circuit.inst(Gates.PhaseGate(2.482034489972267, 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))

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

