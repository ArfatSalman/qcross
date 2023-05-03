
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CU1Gate", "iSwapGate", "CSXGate", "RZZGate", "CHGate", "XGate", "RZGate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 0 ))
circuit.inst(Gates.iSwapGate( 2, 0 ))
circuit.inst(Gates.CSXGate( 3, 1 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 1, 2 ))
circuit.inst(Gates.CU1Gate(5.154187354656876, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.CHGate( 3, 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 4)

