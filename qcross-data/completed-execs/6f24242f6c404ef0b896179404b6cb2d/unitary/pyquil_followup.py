
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("RCCXGate", "U2Gate", "ZGate", "CU1Gate", "RZZGate", "CRZGate", "XGate", "RZGate", "SdgGate", "CSXGate", "TGate", "CHGate", "SXdgGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.RCCXGate( 10, 6, 8 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.CCXGate( 7, 10, 2 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 10 ))
circuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(Gates.CHGate( 0, 7 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 9, 0 ))
circuit.inst(Gates.RZGate(5.0063780207098425, 6 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 4, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.RZGate(4.722103101046168, 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

