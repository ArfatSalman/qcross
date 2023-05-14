
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("RZGate", "CRXGate", "CSXGate", "U2Gate", "CCXGate", "CHGate", "SXGate", "SXdgGate", "ECRGate", "TGate", "CRZGate", "C3SXGate", "XGate", "ZGate", "UGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 6 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 5, 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 9, 1 ))
circuit.inst(Gates.CCXGate( 2, 0, 1 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.XGate( 4 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 9, 5 ))
circuit.inst(Gates.RZGate(4.229610589867865, 9 ))
circuit.inst(Gates.SXGate( 3 ))
circuit.inst(Gates.CSXGate( 7, 4 ))
circuit.inst(Gates.CCXGate( 7, 0, 2 ))
circuit.inst(Gates.C3SXGate( 3, 7, 8, 0 ))
circuit.inst(Gates.CSXGate( 8, 3 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.CHGate( 1, 9 ))
circuit.inst(Gates.CSXGate( 3, 8 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 9, 3 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 3 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RZGate(5.014941143947427, 9 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 1, 9 ))
circuit.inst(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( 3 ))
circuit.inst(Gates.ECRGate( 7, 4 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

