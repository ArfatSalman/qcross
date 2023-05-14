
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )



p_9744ba = circuit.declare('p_9744ba', 'REAL')

defns = get_custom_get_definitions("SdgGate", "CZGate", "PhaseGate", "SXdgGate", "RZGate", "CHGate", "iSwapGate")

circuit += defns

circuit.inst(Gates.RZGate(p_9744ba, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CZGate( 1, 0 ))
subcircuit.inst(Gates.PhaseGate(0.5112149185250571, 1 ))
subcircuit.inst(Gates.SdgGate( 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.iSwapGate( 2, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 3)

