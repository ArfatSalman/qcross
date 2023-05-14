
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CRXGate", "CRZGate", "TGate", "CCXGate", "XGate", "RZGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

