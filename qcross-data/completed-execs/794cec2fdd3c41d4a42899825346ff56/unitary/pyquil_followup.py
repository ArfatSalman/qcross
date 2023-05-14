
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("ZGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 5, 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 6)

