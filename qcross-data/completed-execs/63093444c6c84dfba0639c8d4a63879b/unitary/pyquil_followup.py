
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("ZGate", "CHGate", "CU1Gate", "RCCXGate", "CCXGate", "TGate", "XGate", "U2Gate", "RZGate", "CRZGate", "CSXGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 5 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 1 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CCXGate( 4, 9, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.RCCXGate( 3, 6, 10 ))
circuit.inst(Gates.RZGate(4.229610589867865, 8 ))
circuit.inst(Gates.CCXGate( 2, 3, 1 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 3 ))
circuit.inst(Gates.CSXGate( 5, 1 ))
circuit.inst(Gates.CHGate( 8, 2 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 9, 8 ))
circuit.inst(Gates.RZGate(5.0063780207098425, 6 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 1 ))
circuit.inst(Gates.TGate( 8 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

