
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



qc_1 = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr_1 = qc_1.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("CRZGate", "ZGate", "RCCXGate")

qc_1 += defns

qc_1.inst(Gates.CRZGate(4.2641612072511235, 3, 1 ))
qc_1.inst(Gates.ZGate( 1 ))
qc_1.inst(Gates.RCCXGate( 2, 3, 0 ))

qc_1 += MEASURE(0, qr_1[0])
qc_1 += MEASURE(1, qr_1[1])
qc_1 += MEASURE(2, qr_1[2])
qc_1 += MEASURE(3, qr_1[3])
qc_1 += MEASURE(4, qr_1[4])
qc_1 += MEASURE(5, qr_1[5])




qc_1.wrap_in_numshots_loop(7838)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_1, protoquil=True)





result_1 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_1)
RESULT_1 = counts




# Circuit 2

            



qc_2 = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr_2 = qc_2.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("RZGate", "ZGate", "XGate", "CCXGate")

qc_2 += defns

qc_2.inst(Gates.RZGate(6.163759533339787, 0 ))
qc_2.inst(Gates.ZGate( 1 ))
qc_2.inst(Gates.CCXGate( 3, 2, 4 ))
qc_2.inst(Gates.XGate( 4 ))

qc_2 += MEASURE(0, qr_2[0])
qc_2 += MEASURE(1, qr_2[1])
qc_2 += MEASURE(2, qr_2[2])
qc_2 += MEASURE(3, qr_2[3])
qc_2 += MEASURE(4, qr_2[4])




qc_2.wrap_in_numshots_loop(7838)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_2, protoquil=True)





result_2 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_2)
RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from utils import display_results
    for i in RESULT:
        display_results( {"result": i })


