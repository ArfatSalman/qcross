
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("XGate", "RZGate", "ZGate", "CSXGate", "CRXGate", "C3SXGate", "RYYGate", "RZZGate", "SdgGate", "TGate", "CU1Gate", "SXGate", "CUGate", "CRZGate", "U2Gate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 3, 2 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 6, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 2, 5 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 2, 1 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 6, 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 6 ))
circuit.inst(Gates.SXGate( 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 3 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 2, 4 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 1, 3 ))
circuit.inst(Gates.CSXGate( 3, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.RZGate(3.775592041307464, 4 ))
circuit.inst(Gates.CRXGate(0.7279391018916035, 3, 5 ))
circuit.inst(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305, 2, 7 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 7 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 5, 4 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RYYGate(1.9669252191306448)( 4, 7 ))
circuit.inst(Gates.C3SXGate( 6, 5, 7, 0 ))

circuit += MEASURE(3, qr[0])
circuit += MEASURE(6, qr[1])
circuit += MEASURE(7, qr[2])
circuit += MEASURE(5, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(0, qr[5])
circuit += MEASURE(2, qr[6])
circuit += MEASURE(1, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })
