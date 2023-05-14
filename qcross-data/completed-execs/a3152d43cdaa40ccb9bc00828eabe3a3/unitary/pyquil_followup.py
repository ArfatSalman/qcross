
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_668799 = circuit.declare('p_668799', 'REAL')
p_4a9618 = circuit.declare('p_4a9618', 'REAL')
p_68b975 = circuit.declare('p_68b975', 'REAL')
p_4dfb76 = circuit.declare('p_4dfb76', 'REAL')
p_c4dfaf = circuit.declare('p_c4dfaf', 'REAL')

defns = get_custom_get_definitions("ZGate", "CCXGate", "C3SXGate", "CUGate", "TGate", "RZGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_c4dfaf, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_68b975, 2, 4 ))
circuit.inst(Gates.CUGate(p_4dfb76, p_668799, 2.3864521352475245, p_4a9618, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 6)

