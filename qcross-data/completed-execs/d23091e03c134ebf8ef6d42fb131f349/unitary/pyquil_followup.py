
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("SGate", "C4XGate", "HGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.SGate( 4 ))
subcircuit.inst(Gates.C4XGate( 1, 7, 4, 3, 6 ))
subcircuit.inst(Gates.HGate( 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())




from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 8)

