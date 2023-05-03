
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("XGate", "RZGate", "ZGate", "RCCXGate", "SGate", "CSXGate", "CHGate", "CRXGate", "C3SXGate", "ECRGate", "SdgGate", "CU1Gate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 1, 3 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 1 ))
circuit.inst(Gates.CHGate( 5, 2 ))
circuit.inst(Gates.C3SXGate( 4, 1, 0, 3 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.ECRGate( 2, 6 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RCCXGate( 1, 3, 4 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.C3SXGate( 4, 1, 0, 6 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 5, 4 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 5, 2 ))
circuit.inst(Gates.CHGate( 5, 4 ))
circuit.inst(Gates.C3SXGate( 1, 4, 6, 5 ))
circuit.inst(Gates.CSXGate( 4, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

