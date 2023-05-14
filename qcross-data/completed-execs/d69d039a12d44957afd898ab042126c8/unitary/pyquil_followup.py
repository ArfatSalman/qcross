
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("TGate", "C3XGate", "CHGate", "SXGate", "CRXGate", "XGate", "ECRGate", "C3SXGate", "CU3Gate", "RZGate", "U1Gate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))

subcircuit = Program()
subcircuit.inst(Gates.CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789, 2, 6 ))
subcircuit.inst(Gates.CU3Gate(3.865496458458116, 2.6636908506222836, 6.221353754875494, 5, 0 ))
subcircuit.inst(Gates.U1Gate(6.2047416485134805, 0 ))
subcircuit.inst(Gates.TGate( 6 ))
subcircuit.inst(Gates.SXGate( 4 ))
subcircuit.inst(Gates.C3XGate( 4, 6, 2, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

