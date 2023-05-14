
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )



p_b96123 = circuit.declare('p_b96123', 'REAL')
p_016d54 = circuit.declare('p_016d54', 'REAL')
p_99427e = circuit.declare('p_99427e', 'REAL')
p_93d5ac = circuit.declare('p_93d5ac', 'REAL')
p_7691c4 = circuit.declare('p_7691c4', 'REAL')
p_7ec4f4 = circuit.declare('p_7ec4f4', 'REAL')

defns = get_custom_get_definitions("SdgGate", "RCCXGate", "RYYGate", "C3SXGate", "CRZGate", "CSXGate", "CRXGate", "XGate", "CU1Gate", "HGate", "SXdgGate", "RZGate", "ECRGate", "SGate", "ZGate", "CHGate", "SwapGate", "RZZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.HGate( 0 ))
subcircuit.inst(Gates.RZZGate(p_99427e)( 0, 5 ))
subcircuit.inst(Gates.CRZGate(p_016d54, 0, 5 ))
subcircuit.inst(Gates.CSXGate( 4, 0 ))
subcircuit.inst(Gates.SwapGate( 1, 4 ))
subcircuit.inst(Gates.RYYGate(0.5501056885328758)( 2, 0 ))
subcircuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(p_93d5ac, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_b96123, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_7691c4, 4, 0 ))
circuit.inst(Gates.CRXGate(p_7ec4f4, 4, 6 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 7)

