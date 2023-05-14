
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("RZGate", "YGate", "RYYGate", "U1Gate", "RZZGate", "RXGate", "IGate", "RXXGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.IGate( 1 ))
subcircuit.inst(Gates.RYYGate(2.3864521352475245)( 0, 3 ))
subcircuit.inst(Gates.RXGate(3.8629766967365606, 0 ))
subcircuit.inst(Gates.U1Gate(2.6397681660693015, 3 ))
subcircuit.inst(Gates.YGate( 1 ))
subcircuit.inst(Gates.RXXGate(6.033961191253911)( 1, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

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

