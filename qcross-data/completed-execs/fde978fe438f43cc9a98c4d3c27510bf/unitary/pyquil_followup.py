
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_531a81 = circuit.declare('p_531a81', 'REAL')

defns = get_custom_get_definitions("SXdgGate", "RZGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_531a81, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 5)

