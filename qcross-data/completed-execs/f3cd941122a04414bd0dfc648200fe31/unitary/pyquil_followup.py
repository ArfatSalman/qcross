
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("RZXGate", "CRXGate", "XGate", "SXdgGate", "CUGate", "RZGate", "DCXGate", "ZGate", "RZZGate", "CZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))

subcircuit = Program()
subcircuit.inst(Gates.RZXGate(0.6833824466861163)( 0, 6 ))
subcircuit.inst(Gates.SXdgGate( 0 ))
subcircuit.inst(Gates.CZGate( 4, 3 ))
subcircuit.inst(Gates.ZGate( 4 ))
subcircuit.inst(Gates.RZZGate(1.927446989780488)( 6, 7 ))
subcircuit.inst(Gates.CRXGate(4.736752714049485, 4, 0 ))
subcircuit.inst(Gates.DCXGate( 1, 6 ))
subcircuit.inst(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547, 0, 6 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 8)

