
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_6d84ca = circuit.declare('p_6d84ca', 'REAL')
p_e64f44 = circuit.declare('p_e64f44', 'REAL')
p_ac3f49 = circuit.declare('p_ac3f49', 'REAL')

defns = get_custom_get_definitions("CRZGate", "C3SXGate", "CU1Gate", "CUGate", "SGate", "RZGate", "XGate", "CSXGate", "ZGate", "SdgGate", "SXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(p_6d84ca, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_ac3f49, 5.897054719225356, p_e64f44, 5.987304452123941, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 8, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 9)

