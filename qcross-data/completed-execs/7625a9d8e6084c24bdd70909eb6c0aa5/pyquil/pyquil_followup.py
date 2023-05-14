
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



qc_1 = Program()

qr_1 = qc_1.declare("ro", "BIT", 1)



defns = get_custom_get_definitions("TGate")

qc_1 += defns

qc_1.inst(Gates.TGate( 0 ))

qc_1 += MEASURE(0, qr_1[0])




qc_1.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(qc_1, protoquil=True)





result_1 = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result_1)
RESULT_1 = counts




# Circuit 2

            



qc_2 = Program()

qr_2 = qc_2.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CUGate", "ZGate", "RZGate", "RZZGate", "TGate", "SXGate", "SdgGate", "C3SXGate", "CRXGate", "RYYGate", "CU1Gate", "U2Gate", "XGate", "CSXGate", "CRZGate")

qc_2 += defns

qc_2.inst(Gates.RZGate(6.163759533339787, 4 ))
qc_2.inst(Gates.ZGate( 5 ))
qc_2.inst(Gates.XGate( 5 ))
qc_2.inst(Gates.CRXGate(5.987304452123941, 0, 5 ))
qc_2.inst(Gates.CRZGate(1.0296448789776642, 1, 5 ))
qc_2.inst(Gates.C3SXGate( 0, 6, 5, 3 ))
qc_2.inst(Gates.ZGate( 2 ))
qc_2.inst(Gates.XGate( 1 ))
qc_2.inst(Gates.RYYGate(1.740253089260498)( 5, 6 ))
qc_2.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
qc_2.inst(Gates.RZGate(4.229610589867865, 1 ))
qc_2.inst(Gates.SXGate( 0 ))
qc_2.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
qc_2.inst(Gates.CRXGate(5.94477504571567, 5, 4 ))
qc_2.inst(Gates.RZZGate(5.1829934776392745)( 6, 0 ))
qc_2.inst(Gates.CSXGate( 0, 2 ))
qc_2.inst(Gates.ZGate( 5 ))
qc_2.inst(Gates.RZGate(3.775592041307464, 4 ))
qc_2.inst(Gates.CRXGate(0.7279391018916035, 0, 3 ))
qc_2.inst(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305, 5, 2 ))
qc_2.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
qc_2.inst(Gates.TGate( 5 ))
qc_2.inst(Gates.SdgGate( 0 ))
qc_2.inst(Gates.RZZGate(3.950837470808744)( 3, 4 ))

qc_2 += MEASURE(0, qr_2[0])
qc_2 += MEASURE(1, qr_2[1])
qc_2 += MEASURE(2, qr_2[2])
qc_2 += MEASURE(3, qr_2[3])
qc_2 += MEASURE(4, qr_2[4])
qc_2 += MEASURE(5, qr_2[5])
qc_2 += MEASURE(6, qr_2[6])




qc_2.wrap_in_numshots_loop(2771)

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


