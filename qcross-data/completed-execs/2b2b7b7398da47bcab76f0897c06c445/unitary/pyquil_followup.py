
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_1b7413 = circuit.declare('p_1b7413', 'REAL')

defns = get_custom_get_definitions("SXdgGate", "RZGate", "HGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.SXdgGate( 2 ))
subcircuit.inst(Gates.HGate( 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(p_1b7413, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 5)

