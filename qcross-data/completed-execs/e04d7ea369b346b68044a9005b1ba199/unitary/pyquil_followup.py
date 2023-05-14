
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_1d63ec = circuit.declare('p_1d63ec', 'REAL')

defns = get_custom_get_definitions("CHGate", "CCXGate", "ZGate", "RZGate", "XGate", "TGate", "SXGate", "SGate", "RCCXGate", "SdgGate", "iSwapGate", "C3SXGate", "CRXGate", "CU1Gate", "U2Gate", "CUGate", "CSXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, p_1d63ec, 2.3864521352475245, 5.987304452123941, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 8, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 1, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.CCXGate( 0, 6, 1 ))
circuit.inst(Gates.RCCXGate( 4, 0, 1 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZGate(5.014941143947427, 1 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 1, 8 ))
circuit.inst(Gates.iSwapGate( 2, 6 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 9)

