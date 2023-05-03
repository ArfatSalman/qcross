
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("SXdgGate", "RZZGate", "SXGate", "CSXGate", "ECRGate", "CHGate", "TGate", "CRZGate", "iSwapGate", "XGate", "CRXGate", "RYYGate")

circuit += defns

circuit.inst(Gates.RZZGate(6.163759533339787)( 0, 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.ECRGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RYYGate(1.977559237989846)( 1, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.CRZGate(2.2498881927557752, 1, 0 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 2)

