from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilatom import Parameter, quil_sin, quil_cos, quil_exp
from pyquil.quilbase import DefGate
import numpy

theta = Parameter('theta')
phi = Parameter('phi')
lam = Parameter('lam')

u3_matrix = numpy.array(
            [
                [quil_cos(theta/2), -quil_exp(1j * lam) * quil_sin(theta/2)],
                [quil_exp(1j * phi) * quil_sin(theta/2), quil_exp(1j * (phi + lam)) * quil_cos(theta/2)],
            ]
        )
gate_definition = DefGate('U3', u3_matrix, [theta, phi, lam])
U3 = gate_definition.get_constructor()


p = Program()
ro = p.declare('ro', 'BIT', 1)
p += gate_definition
p += U3(6.159830616557135,5.814130909921563,1.581219984490172)(0)
p += MEASURE(0, ro[0])
p.wrap_in_numshots_loop(1000)

qc = get_qc('1q-qvm')  # You can make any 'nq-qvm' this way for any reasonable 'n'
executable = qc.compile(p)
result = qc.run(executable)
bitstrings = result.readout_data.get('ro')
print(bitstrings)