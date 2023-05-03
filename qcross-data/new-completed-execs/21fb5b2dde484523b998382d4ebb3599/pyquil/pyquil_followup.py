
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("SXdgGate", "CRYGate", "IGate", "iSwapGate", "U3Gate", "RZXGate", "CYGate", "YGate", "CCXGate", "SwapGate")

circuit += defns

circuit.inst(Gates.YGate( 0 ))

subcircuit = Program()
subcircuit.inst(Gates.RZXGate(3.16172626234211)( 8, 7 ))
subcircuit.inst(Gates.IGate( 2 ))
subcircuit.inst(Gates.RZXGate(2.6189671924535145)( 1, 6 ))
subcircuit.inst(Gates.CCXGate( 6, 8, 5 ))
subcircuit.inst(Gates.U3Gate(2.1917712015201105, 6.242718257689912, 4.756709623150395)( 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.SwapGate( 5, 8 ))
circuit.inst(Gates.CRYGate(0.4514529683521159, 3, 4 ))
circuit.inst(Gates.iSwapGate( 2, 8 ))
circuit.inst(Gates.CYGate( 4, 3 ))
circuit.inst(Gates.SXdgGate( 7 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

