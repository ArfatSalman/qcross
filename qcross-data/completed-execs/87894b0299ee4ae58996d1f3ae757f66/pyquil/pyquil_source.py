
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("RYGate", "CUGate", "C3XGate", "TGate", "CYGate", "U2Gate", "ZGate", "CU1Gate", "CSwapGate", "CRYGate")

circuit += defns

circuit.inst(Gates.CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054, 5, 3 ))
circuit.inst(Gates.U2Gate(0.49960530614896387, 3.4965748481666385)( 0 ))
circuit.inst(Gates.RYGate(1.6125723299807893, 0 ))
circuit.inst(Gates.C3XGate( 9, 1, 5, 2 ))
circuit.inst(Gates.RYGate(5.620914585085149, 9 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CSwapGate( 4, 2, 9 ))
circuit.inst(Gates.CRYGate(1.9836175804480751, 6, 9 ))
circuit.inst(Gates.CU1Gate(4.388257530988808, 3, 6 ))
circuit.inst(Gates.CYGate( 5, 9 ))
circuit.inst(Gates.RYGate(4.206888046259435, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

