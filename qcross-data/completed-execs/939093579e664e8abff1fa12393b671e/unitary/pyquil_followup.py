
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("XGate", "RZGate", "ZGate", "CSXGate", "RCCXGate", "CRXGate", "DCXGate", "TGate", "CCXGate", "CYGate", "SXGate", "RXXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.CYGate( 2, 4 ))
subcircuit.inst(Gates.SXGate( 0 ))
subcircuit.inst(Gates.CRZGate(2.008796895454228, 0, 5 ))
subcircuit.inst(Gates.RCCXGate( 9, 1, 8 ))
subcircuit.inst(Gates.RXXGate(5.25962645863375)( 4, 6 ))
subcircuit.inst(Gates.DCXGate( 2, 7 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

