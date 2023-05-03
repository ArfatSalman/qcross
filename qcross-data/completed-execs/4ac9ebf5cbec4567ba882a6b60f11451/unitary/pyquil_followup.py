
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CRZGate", "ZGate", "XGate", "RZGate", "CRXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 7, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 6, 3 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 7 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 8)

