
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("RZXGate", "iSwapGate", "C3SXGate", "RZZGate", "CU1Gate", "CUGate", "RZGate", "XGate", "CSXGate", "HGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.XGate( 1 ))
subcircuit.inst(Gates.RZXGate(1.927446989780488)( 2, 0 ))
subcircuit.inst(Gates.HGate( 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CU1Gate(5.154187354656876, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 4)

