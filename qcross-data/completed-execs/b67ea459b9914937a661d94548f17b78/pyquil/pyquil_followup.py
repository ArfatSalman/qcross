
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("SdgGate", "CCXGate", "TdgGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.SdgGate( 0 ))
subcircuit.inst(Gates.TdgGate( 0 ))
subcircuit.inst(Gates.CCXGate( 2, 3, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())


qr_a24f97 = circuit.declare("qr_a24f97", "BIT", 7)

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

