
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("SXdgGate", "CCXGate", "SGate", "SdgGate", "RZGate", "CSXGate", "CHGate", "iSwapGate", "XGate", "CRXGate", "RYYGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 0 ))
circuit.inst(Gates.CHGate( 2, 1 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 0, 1, 2 ))
circuit.inst(Gates.CHGate( 2, 1 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 3)

