
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )



p_a2a414 = circuit.declare('p_a2a414', 'REAL')
p_560035 = circuit.declare('p_560035', 'REAL')
p_47c65c = circuit.declare('p_47c65c', 'REAL')
p_0a6c0e = circuit.declare('p_0a6c0e', 'REAL')
p_fa3e46 = circuit.declare('p_fa3e46', 'REAL')
p_26dfb8 = circuit.declare('p_26dfb8', 'REAL')

defns = get_custom_get_definitions("ZGate", "RZGate", "XGate", "SXGate", "SGate", "SdgGate", "C3SXGate", "CU1Gate", "CUGate", "CSXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_0a6c0e, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_a2a414, p_560035, p_26dfb8, p_47c65c, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_fa3e46, 8, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 9)

