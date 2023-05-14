
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CHGate", "ZGate", "RZGate", "PhaseGate", "iSwapGate", "SdgGate", "CU1Gate", "CPhaseGate", "XGate", "CSXGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))

subcircuit = Program()
subcircuit.inst(Gates.PhaseGate(0.5112149185250571, 1 ))
subcircuit.inst(Gates.SdgGate( 1 ))
subcircuit.inst(Gates.ZGate( 2 ))
subcircuit.inst(Gates.CPhaseGate(2.2498881927557752, 1, 0 ))
subcircuit.inst(Gates.CU1Gate(5.320621737498446, 1, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 3)

