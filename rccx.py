from pyquil import Program
from pyquil.gates import *
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_exp
from pyquil.quilbase import DefGate
import numpy

def rccx_gate():

    rccx = numpy.array(
                [
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, -1j],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, -1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1j, 0, 0, 0, 0],
                ]
            )

    gate_definition = DefGate('RCCX', rccx)

    RCCX = gate_definition.get_constructor()
    return gate_definition, RCCX

p = Program()
ro = p.declare('ro', 'BIT', 7)
p += gate_definition
p += RCCX(2,3,0)
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])
p += MEASURE(2, ro[2])
p += MEASURE(3, ro[3])
p += MEASURE(4, ro[4])
p += MEASURE(5, ro[5])
p += MEASURE(6, ro[6])
print(p.out())