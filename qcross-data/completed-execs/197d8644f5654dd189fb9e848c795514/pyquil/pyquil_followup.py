
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



qc_1 = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr_1 = qc_1.declare("ro", "BIT", 1)



defns = get_custom_get_definitions("ZGate", "SXdgGate", "TGate")

qc_1 += defns

qc_1.inst(Gates.ZGate( 0 ))
qc_1.inst(Gates.TGate( 0 ))
qc_1.inst(Gates.SXdgGate( 0 ))

qc_1 += MEASURE(0, qr_1[0])




qc_1.wrap_in_numshots_loop(7838)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_1, protoquil=True)





result_1 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_1)
RESULT_1 = counts




# Circuit 2

            



qc_2 = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr_2 = qc_2.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "RCCXGate", "RZZGate", "CU1Gate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CHGate", "CCXGate")

qc_2 += defns

qc_2.inst(Gates.RZGate(6.163759533339787, 2 ))
qc_2.inst(Gates.CRZGate(4.2641612072511235, 5, 1 ))
qc_2.inst(Gates.CCXGate( 4, 8, 6 ))
qc_2.inst(Gates.ZGate( 1 ))
qc_2.inst(Gates.XGate( 6 ))
qc_2.inst(Gates.RCCXGate( 9, 5, 7 ))
qc_2.inst(Gates.RZGate(4.229610589867865, 0 ))
qc_2.inst(Gates.CCXGate( 6, 9, 1 ))
qc_2.inst(Gates.SdgGate( 6 ))
qc_2.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 9 ))
qc_2.inst(Gates.CSXGate( 2, 1 ))
qc_2.inst(Gates.CHGate( 0, 6 ))
qc_2.inst(Gates.CU1Gate(4.028174522740928, 8, 0 ))
qc_2.inst(Gates.RZGate(5.0063780207098425, 5 ))
qc_2.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 1 ))
qc_2.inst(Gates.TGate( 0 ))
qc_2.inst(Gates.RZZGate(3.950837470808744)( 3, 0 ))
qc_2.inst(Gates.TGate( 0 ))
qc_2.inst(Gates.SXdgGate( 4 ))
qc_2.inst(Gates.RZGate(4.722103101046168, 1 ))
qc_2.inst(Gates.CRZGate(0.6393443962862078, 4, 2 ))
qc_2.inst(Gates.CU1Gate(2.5476776328466872, 2, 7 ))

qc_2 += MEASURE(0, qr_2[0])
qc_2 += MEASURE(1, qr_2[1])
qc_2 += MEASURE(2, qr_2[2])
qc_2 += MEASURE(3, qr_2[3])
qc_2 += MEASURE(4, qr_2[4])
qc_2 += MEASURE(5, qr_2[5])
qc_2 += MEASURE(6, qr_2[6])
qc_2 += MEASURE(7, qr_2[7])
qc_2 += MEASURE(8, qr_2[8])
qc_2 += MEASURE(9, qr_2[9])




qc_2.wrap_in_numshots_loop(7838)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_2, protoquil=True)





result_2 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_2)
RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from utils import display_results
    for i in RESULT:
        display_results( {"result": i })


