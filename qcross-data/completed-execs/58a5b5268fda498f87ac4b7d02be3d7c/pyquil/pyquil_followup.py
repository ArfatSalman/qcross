
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



qc_1 = Program()

qr_1 = qc_1.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CRZGate", "RZGate", "CCXGate", "TGate", "CRXGate")

qc_1 += defns

qc_1.inst(Gates.RZGate(6.163759533339787, 1 ))
qc_1.inst(Gates.CRZGate(4.2641612072511235, 3, 1 ))
qc_1.inst(Gates.CRXGate(5.987304452123941, 0, 4 ))
qc_1.inst(Gates.CCXGate( 2, 5, 4 ))
qc_1.inst(Gates.TGate( 5 ))
qc_1.inst(Gates.CRZGate(4.167661441102218, 0, 3 ))
qc_1.inst(Gates.RZGate(4.229610589867865, 0 ))

qc_1 += MEASURE(0, qr_1[0])
qc_1 += MEASURE(1, qr_1[1])
qc_1 += MEASURE(2, qr_1[2])
qc_1 += MEASURE(3, qr_1[3])
qc_1 += MEASURE(4, qr_1[4])
qc_1 += MEASURE(5, qr_1[5])
qc_1 += MEASURE(6, qr_1[6])




qc_1.wrap_in_numshots_loop(5542)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_1, protoquil=True)



result_1 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_1)
RESULT_1 = counts




# Circuit 2

            



qc_2 = Program()

qr_2 = qc_2.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("SXGate", "ZGate", "CSXGate", "XGate")

qc_2 += defns

qc_2.inst(Gates.ZGate( 2 ))
qc_2.inst(Gates.XGate( 0 ))
qc_2.inst(Gates.SXGate( 2 ))
qc_2.inst(Gates.CSXGate( 1, 0 ))

qc_2 += MEASURE(0, qr_2[0])
qc_2 += MEASURE(1, qr_2[1])
qc_2 += MEASURE(2, qr_2[2])




qc_2.wrap_in_numshots_loop(5542)

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


