
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CCXGate", "ZGate", "RZGate", "TGate", "RZZGate", "SXGate", "SGate", "C3SXGate", "CRXGate", "CU1Gate", "UGate", "CUGate", "RCCXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.RZGate(0.5836727148908056, 1 ))
subcircuit.inst(Gates.RZGate(1.2484842640635918, 0 ))
subcircuit.inst(Gates.CRZGate(4.747288222618085, 1, 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 5 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( 5 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 5 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 1, 4 ))
circuit.inst(Gates.C3SXGate( 3, 0, 4, 2 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 2, 5 ))
circuit.inst(Gates.CRXGate(2.6687018103754414, 4, 5 ))
circuit.inst(Gates.CRZGate(5.742126321682921, 2, 0 ))
circuit.inst(Gates.TGate( 5 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 6)

