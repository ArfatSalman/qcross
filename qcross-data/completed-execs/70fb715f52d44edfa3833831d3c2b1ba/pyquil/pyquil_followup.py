
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("C3SXGate", "SXGate", "SXdgGate", "RZGate", "ZGate", "CUGate", "UGate", "U2Gate", "RZZGate", "TGate", "CU1Gate", "SdgGate", "XGate", "CRZGate", "RYYGate", "CRXGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 7, 2 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 2 ))
circuit.inst(Gates.C3SXGate( 7, 0, 2, 6 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 2, 0 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 0 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 7 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 7 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 2, 4 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 0, 7 ))
circuit.inst(Gates.CSXGate( 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.RZGate(3.775592041307464, 4 ))
circuit.inst(Gates.CRXGate(0.7279391018916035, 7, 6 ))
circuit.inst(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305, 2, 5 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 5 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 6, 4 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.RYYGate(1.9669252191306448)( 4, 5 ))
circuit.inst(Gates.C3SXGate( 1, 6, 5, 3 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( 5 ))

circuit += MEASURE(7, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(6, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(2, qr[6])
circuit += MEASURE(0, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

