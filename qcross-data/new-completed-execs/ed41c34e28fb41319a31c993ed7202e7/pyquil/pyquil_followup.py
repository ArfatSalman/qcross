
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("CSGate", "CU3Gate", "CXGate", "CSdgGate", "CRYGate", "U2Gate", "CCZGate", "CUGate", "CSXGate", "CYGate", "CRZGate")

circuit += defns

circuit.inst(Gates.CCZGate( 2, 1, 0 ))
circuit.inst(Gates.CU3Gate(2.6781418933705265, 5.033873892484971, 0.8205539045157343, 0, 2 ))
circuit.inst(Gates.CSGate( 2, 0 ))
circuit.inst(Gates.CSdgGate( 2, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.CYGate( 1, 2 ))
subcircuit.inst(Gates.CRZGate(2.0238721057673663, 0, 2 ))
subcircuit.inst(Gates.U2Gate(4.584479443719739, 1.724423394919128)( 0 ))
subcircuit.inst(Gates.CSXGate( 1, 0 ))
subcircuit.inst(Gates.CRYGate(0.8712775153371473, 0, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRYGate(1.4158427363998418, 0, 1 ))
circuit.inst(Gates.CU3Gate(3.033025708292916, 4.882023158927633, 2.498989202347216, 0, 1 ))
circuit.inst(Gates.CSGate( 1, 0 ))
circuit.inst(Gates.U2Gate(1.2920361589137734, 0.11522677196421838)( 2 ))
circuit.inst(Gates.CUGate(0.5771195062234611, 6.03105941204732, 5.250698623145584, 4.055221339124102, 1, 2 ))
circuit.inst(Gates.CU3Gate(1.40128081782857, 0.22745116565007226, 1.0942942714535664, 2, 1 ))
circuit.inst(Gates.CU3Gate(5.272901276657899, 4.665266516802061, 4.874107923353778, 0, 2 ))
circuit.inst(Gates.CXGate( 1, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

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

