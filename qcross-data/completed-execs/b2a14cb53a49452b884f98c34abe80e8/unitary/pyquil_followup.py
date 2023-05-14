
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()



p_ec106f = circuit.declare('p_ec106f', 'REAL')
p_5f113d = circuit.declare('p_5f113d', 'REAL')
p_cf8439 = circuit.declare('p_cf8439', 'REAL')
p_7e38fe = circuit.declare('p_7e38fe', 'REAL')
p_50c455 = circuit.declare('p_50c455', 'REAL')
p_e13c2b = circuit.declare('p_e13c2b', 'REAL')

defns = get_custom_get_definitions("UGate", "IGate", "U3Gate", "RZGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_ec106f, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.U3Gate(p_7e38fe, p_5f113d, 0.4903361071050254)( 1 ))
subcircuit.inst(Gates.IGate( 2 ))
subcircuit.inst(Gates.UGate(p_e13c2b, p_50c455, p_cf8439)( 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 2 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)

