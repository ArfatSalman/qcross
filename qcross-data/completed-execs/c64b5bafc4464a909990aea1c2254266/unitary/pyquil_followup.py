
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CHGate", "RCCXGate", "CRXGate", "XGate", "ECRGate", "C3SXGate", "SdgGate", "RZGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 6, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 5, 6 ))
circuit.inst(Gates.CHGate( 4, 3 ))
circuit.inst(Gates.C3SXGate( 1, 6, 5, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.ECRGate( 3, 0 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.RCCXGate( 6, 2, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

