
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CHGate", "ZGate", "RZGate", "ECRGate", "SGate", "SdgGate", "C3SXGate", "CRXGate", "CU1Gate", "XGate", "RCCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 5, 3 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 5 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 4, 5, 0, 3 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.ECRGate( 2, 6 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.C3SXGate( 4, 5, 0, 6 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 1, 4 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

