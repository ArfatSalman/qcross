
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_8a56c7 = circuit.declare('p_8a56c7', 'REAL')
p_12f990 = circuit.declare('p_12f990', 'REAL')
p_474773 = circuit.declare('p_474773', 'REAL')

defns = get_custom_get_definitions("CRZGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_8a56c7, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 3 ))
circuit.inst(Gates.CRXGate(p_12f990, 5, 1 ))
circuit.inst(Gates.CCXGate( 7, 8, 1 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.XGate( 9 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 5, 2 ))
circuit.inst(Gates.RZGate(p_474773, 5 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.CSXGate( 6, 9 ))
circuit.inst(Gates.CCXGate( 6, 8, 7 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

