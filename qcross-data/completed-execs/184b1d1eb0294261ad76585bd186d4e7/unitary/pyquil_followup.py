
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CRZGate", "C3SXGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 3 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 5, 1 ))
circuit.inst(Gates.CCXGate( 7, 8, 1 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.XGate( 9 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 5, 2 ))
circuit.inst(Gates.RZGate(4.229610589867865, 5 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.CSXGate( 6, 9 ))
circuit.inst(Gates.CCXGate( 6, 8, 7 ))
circuit.inst(Gates.C3SXGate( 4, 6, 0, 8 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

