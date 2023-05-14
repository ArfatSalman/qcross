
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_d542f8 = circuit.declare('p_d542f8', 'REAL')

defns = get_custom_get_definitions("RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_d542f8, 3 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

