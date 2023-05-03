
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_a7ecd0 = circuit.declare('p_a7ecd0', 'REAL')

defns = get_custom_get_definitions("RYGate", "CPhaseGate", "RZGate", "CXGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.CXGate( 10, 3 ))
subcircuit.inst(Gates.RYGate(2.3864521352475245, 1 ))
subcircuit.inst(Gates.CPhaseGate(1.6161683469432118, 5, 9 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(p_a7ecd0, 3 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

