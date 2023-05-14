
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_80e8e5 = circuit.declare('p_80e8e5', 'REAL')
p_d391ad = circuit.declare('p_d391ad', 'REAL')
p_58cdd0 = circuit.declare('p_58cdd0', 'REAL')
p_899200 = circuit.declare('p_899200', 'REAL')
p_ff62da = circuit.declare('p_ff62da', 'REAL')
p_5b5ed2 = circuit.declare('p_5b5ed2', 'REAL')
p_4c1552 = circuit.declare('p_4c1552', 'REAL')
p_118d87 = circuit.declare('p_118d87', 'REAL')
p_683b64 = circuit.declare('p_683b64', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "C3SXGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_683b64, 3 ))
circuit.inst(Gates.CRZGate(p_58cdd0, 6, 3 ))
circuit.inst(Gates.CRXGate(p_5b5ed2, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_d391ad, 1, 6 ))
circuit.inst(Gates.RZGate(p_4c1552, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_899200, 1, 2 ))
circuit.inst(Gates.U2Gate(p_118d87, p_ff62da)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(p_80e8e5, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

