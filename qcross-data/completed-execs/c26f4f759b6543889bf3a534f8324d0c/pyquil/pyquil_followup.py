
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



qc_1 = Program()

qr_1 = qc_1.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("ZGate")

qc_1 += defns

qc_1.inst(Gates.ZGate( 0 ))

qr_1 = qc_1.declare("qr_1", "BIT", 2)

qc_1 += MEASURE(0, qr_1[0])
qc_1 += MEASURE(1, qr_1[1])




qc_1.wrap_in_numshots_loop(7838)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_1, protoquil=True)





result_1 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_1)
RESULT_1 = counts




# Circuit 2

            



qc_2 = Program()

qr_2 = qc_2.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("RZGate", "RCCXGate", "SdgGate", "U2Gate", "CSXGate", "CCXGate", "CHGate", "CRZGate", "CU1Gate", "XGate", "ZGate")

qc_2 += defns

qc_2.inst(Gates.RZGate(6.163759533339787, 2 ))
qc_2.inst(Gates.CRZGate(4.2641612072511235, 4, 1 ))
qc_2.inst(Gates.CCXGate( 3, 7, 5 ))
qc_2.inst(Gates.ZGate( 1 ))
qc_2.inst(Gates.XGate( 5 ))
qc_2.inst(Gates.RCCXGate( 8, 4, 6 ))
qc_2.inst(Gates.RZGate(4.229610589867865, 0 ))
qc_2.inst(Gates.CCXGate( 5, 8, 1 ))
qc_2.inst(Gates.SdgGate( 5 ))
qc_2.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 8 ))
qc_2.inst(Gates.CSXGate( 2, 1 ))
qc_2.inst(Gates.CHGate( 0, 5 ))
qc_2.inst(Gates.CU1Gate(4.028174522740928, 7, 0 ))
qc_2.inst(Gates.RZGate(5.0063780207098425, 4 ))
qc_2.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 1 ))

qr_2 = qc_2.declare("qr_2", "BIT", 9)

qc_2 += MEASURE(0, qr_2[0])
qc_2 += MEASURE(1, qr_2[1])
qc_2 += MEASURE(2, qr_2[2])
qc_2 += MEASURE(3, qr_2[3])
qc_2 += MEASURE(4, qr_2[4])
qc_2 += MEASURE(5, qr_2[5])
qc_2 += MEASURE(6, qr_2[6])
qc_2 += MEASURE(7, qr_2[7])
qc_2 += MEASURE(8, qr_2[8])




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


