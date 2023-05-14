
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("RZGate", "CSXGate", "CHGate", "SXdgGate", "iSwapGate", "XGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.XGate( 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 3)

