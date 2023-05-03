
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CCXGate", "SdgGate", "C3XGate", "CHGate", "RC3XGate", "RZGate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(1.011876271526295, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CUGate(4.470339697850853, 2.3870542496998692, 0.050955830933431714, 0.06883225750858235, 0, 4 ))
circuit.inst(Gates.C3XGate( 6, 4, 5, 1 ))
circuit.inst(Gates.RC3XGate( 4, 6, 5, 2 ))
circuit.inst(Gates.SdgGate( 5 ))
circuit.inst(Gates.CCXGate( 0, 5, 6 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(4, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(0, qr[4])
circuit += MEASURE(6, qr[5])
circuit += MEASURE(2, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

