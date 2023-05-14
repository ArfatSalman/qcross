
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_6142d5 = circuit.declare('p_6142d5', 'REAL')
p_2be59c = circuit.declare('p_2be59c', 'REAL')
p_668fde = circuit.declare('p_668fde', 'REAL')
p_3b7aea = circuit.declare('p_3b7aea', 'REAL')
p_ef3ee6 = circuit.declare('p_ef3ee6', 'REAL')
p_75d3b5 = circuit.declare('p_75d3b5', 'REAL')

defns = get_custom_get_definitions("TGate", "CRZGate", "CSXGate", "SXGate", "XGate", "CRXGate", "CU1Gate", "SXdgGate", "ECRGate", "RZGate", "CHGate", "RYYGate", "RZZGate", "iSwapGate")

circuit += defns

circuit.inst(Gates.RZZGate(6.163759533339787)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_3b7aea)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_75d3b5, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_6142d5, 1 ))
circuit.inst(Gates.RZGate(5.512260524440591, 1 ))
circuit.inst(Gates.CU1Gate(1.6723037552953224, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(p_ef3ee6)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(p_2be59c)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_668fde, 1 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 2)

