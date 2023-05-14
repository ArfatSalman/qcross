
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_66d141 = circuit.declare('p_66d141', 'REAL')
p_637123 = circuit.declare('p_637123', 'REAL')

defns = get_custom_get_definitions("CSXGate", "CHGate", "ZGate", "RZGate", "CRZGate", "SdgGate", "CU1Gate", "U2Gate", "XGate", "RCCXGate", "CCXGate")

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
circuit.inst(Gates.U2Gate(4.214504315296764, p_66d141)( 10 ))
circuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(Gates.CHGate( 0, 7 ))
circuit.inst(Gates.CU1Gate(p_637123, 9, 0 ))
circuit.inst(Gates.RZGate(5.0063780207098425, 6 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

