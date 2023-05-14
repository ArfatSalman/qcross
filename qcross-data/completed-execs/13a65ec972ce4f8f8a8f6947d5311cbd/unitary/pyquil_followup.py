
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )





defns = get_custom_get_definitions("ZGate", "RZGate", "RZZGate", "SXGate", "C3SXGate", "CRXGate", "RYYGate", "CU1Gate", "XGate", "CSXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 4, 7 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 0, 7 ))
circuit.inst(Gates.C3SXGate( 4, 3, 7, 5 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 7, 3 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 0, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 2, 4 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 7, 2 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 3, 4 ))
circuit.inst(Gates.CSXGate( 4, 1 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.RZGate(3.775592041307464, 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 8)

