
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("RCCXGate", "ZGate", "C3SXGate", "XGate", "RZGate", "SdgGate", "ECRGate", "SGate", "CHGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 3, 6 ))
circuit.inst(Gates.C3SXGate( 1, 5, 4, 3 ))
circuit.inst(Gates.CHGate( 2, 1 ))
circuit.inst(Gates.C3SXGate( 5, 3, 4, 6 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.RCCXGate( 3, 6, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.RZGate(4.229610589867865, 4 ))
circuit.inst(Gates.C3SXGate( 5, 3, 4, 0 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

