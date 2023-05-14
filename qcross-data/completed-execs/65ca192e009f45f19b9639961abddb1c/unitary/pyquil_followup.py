
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )





defns = get_custom_get_definitions("ZGate", "CHGate", "CPhaseGate", "CRZGate", "RCCXGate", "SGate", "SXGate", "C3SXGate", "ECRGate", "C3XGate", "XGate", "CRXGate", "RZGate", "RZXGate", "CYGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))

subcircuit = Program()
subcircuit.inst(Gates.CPhaseGate(4.63837786161633, 2, 0 ))
subcircuit.inst(Gates.RZXGate(4.563562108824195)( 4, 0 ))
subcircuit.inst(Gates.C3XGate( 4, 6, 2, 1 ))
subcircuit.inst(Gates.XGate( 4 ))
subcircuit.inst(Gates.CYGate( 2, 0 ))
subcircuit.inst(Gates.SXGate( 0 ))
subcircuit.inst(Gates.CRZGate(2.008796895454228, 0, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

