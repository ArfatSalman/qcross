
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("RC3XGate", "C4XGate", "SdgGate", "U2Gate", "CUGate")

circuit += defns

circuit.inst(Gates.CUGate(4.8953107059252625, 2.6758072220615388, 3.2748083473946528, 6.236176216437301, 4, 3 ))
circuit.inst(Gates.SdgGate( 4 ))
circuit.inst(Gates.RC3XGate( 4, 2, 1, 3 ))
circuit.inst(Gates.CUGate(3.8548770506419117, 4.254344154816252, 1.4586583527810086, 0.6558022908747309, 1, 4 ))
circuit.inst(Gates.U2Gate(4.508908477229367, 4.339644176014044)( 5 ))
circuit.inst(Gates.C4XGate( 5, 2, 4, 1, 0 ))
circuit.inst(Gates.CUGate(2.0612495225167686, 0.9108049053481971, 1.7408688031064241, 2.2294210493888307, 2, 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

