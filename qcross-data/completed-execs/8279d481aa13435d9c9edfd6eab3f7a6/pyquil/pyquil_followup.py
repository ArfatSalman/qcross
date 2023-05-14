
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



qc_1 = Program()

qr_1 = qc_1.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("C3SXGate", "CUGate", "SGate", "RZGate", "XGate")

qc_1 += defns

qc_1.inst(Gates.RZGate(6.163759533339787, 4 ))
qc_1.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 2 ))
qc_1.inst(Gates.C3SXGate( 0, 4, 3, 1 ))
qc_1.inst(Gates.XGate( 1 ))
qc_1.inst(Gates.SGate( 0 ))
qc_1.inst(Gates.SGate( 4 ))

qc_1 += MEASURE(0, qr_1[0])
qc_1 += MEASURE(1, qr_1[1])
qc_1 += MEASURE(2, qr_1[2])
qc_1 += MEASURE(3, qr_1[3])
qc_1 += MEASURE(4, qr_1[4])
qc_1 += MEASURE(5, qr_1[5])




qc_1.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_1, protoquil=True)





result_1 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_1)
RESULT_1 = counts




# Circuit 2

            



qc_2 = Program()

qr_2 = qc_2.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("ZGate", "SdgGate", "CSXGate")

qc_2 += defns

qc_2.inst(Gates.CSXGate( 1, 2 ))
qc_2.inst(Gates.SdgGate( 0 ))
qc_2.inst(Gates.ZGate( 1 ))

qc_2 += MEASURE(0, qr_2[0])
qc_2 += MEASURE(1, qr_2[1])
qc_2 += MEASURE(2, qr_2[2])




qc_2.wrap_in_numshots_loop(3919)

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


