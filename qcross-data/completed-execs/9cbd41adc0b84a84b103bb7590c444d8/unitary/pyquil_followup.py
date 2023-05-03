
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"PARTIAL"']) )



p_e7b8b0 = circuit.declare('p_e7b8b0', 'REAL')

defns = get_custom_get_definitions("ECRGate", "RZZGate", "CSXGate", "SXdgGate", "iSwapGate", "XGate")

circuit += defns

circuit.inst(Gates.RZZGate(p_e7b8b0)( 0, 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.ECRGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 2)

