
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("SXdgGate", "XGate", "RZGate", "ZGate", "RCCXGate", "CSXGate", "CHGate", "RZZGate", "UGate", "SdgGate", "TGate", "CCXGate", "CU1Gate", "CRZGate", "U2Gate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 10 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 1 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CCXGate( 0, 7, 4 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 4 ))
circuit.inst(Gates.RCCXGate( 9, 6, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 2 ))
circuit.inst(Gates.CCXGate( 4, 9, 1 ))
circuit.inst(Gates.SdgGate( 4 ))
circuit.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 9 ))
circuit.inst(Gates.CSXGate( 10, 1 ))
circuit.inst(Gates.CHGate( 2, 4 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 7, 2 ))
circuit.inst(Gates.RZGate(5.0063780207098425, 6 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 1 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 8, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RZGate(4.722103101046168, 1 ))
circuit.inst(Gates.CRZGate(0.6393443962862078, 0, 10 ))
circuit.inst(Gates.CU1Gate(2.5476776328466872, 10, 3 ))
circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.RZGate(3.6614081973587154, 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CSXGate( 4, 2 ))
circuit.inst(Gates.CU1Gate(3.631024984774394, 9, 4 ))
circuit.inst(Gates.UGate(3.4183332103477166, 1.1450785027645094, 1.308491043619365)( 6 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

