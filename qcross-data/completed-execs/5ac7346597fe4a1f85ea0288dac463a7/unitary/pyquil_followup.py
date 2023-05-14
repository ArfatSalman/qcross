
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_946f6c = circuit.declare('p_946f6c', 'REAL')
p_ad8fd1 = circuit.declare('p_ad8fd1', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "RCCXGate", "RZZGate", "CU1Gate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(p_946f6c, 6, 2 ))
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
circuit.inst(Gates.U2Gate(p_ad8fd1, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 4, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.RZGate(4.722103101046168, 2 ))
circuit.inst(Gates.CRZGate(0.6393443962862078, 5, 3 ))
circuit.inst(Gates.CU1Gate(2.5476776328466872, 3, 8 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.RZGate(3.6614081973587154, 6 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CSXGate( 7, 0 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

