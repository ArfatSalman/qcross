from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_exp
from pyquil.quilbase import DefGate
import numpy

def cu1_defn():
    eith = Parameter('eith')
    cu1 = numpy.array(
                    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, quil_exp(1j * eith)]]
                )
    gate_definition = DefGate('CU1', cu1, [eith])

    CU1 = gate_definition.get_constructor()
    return gate_definition, CU1

p = Program()
ro = p.declare('ro', 'BIT', 1)
p += gate_definition
p += CU1(5.83674944466042)(0)
p += MEASURE(0, ro[0])
print(p.out())