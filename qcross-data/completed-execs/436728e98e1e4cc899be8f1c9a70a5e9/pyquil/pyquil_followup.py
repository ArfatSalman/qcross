
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_f36ce2 = circuit.declare('p_f36ce2', 'REAL')
p_3c5b38 = circuit.declare('p_3c5b38', 'REAL')
p_2be356 = circuit.declare('p_2be356', 'REAL')
p_a02e63 = circuit.declare('p_a02e63', 'REAL')
p_230af2 = circuit.declare('p_230af2', 'REAL')
p_e694fd = circuit.declare('p_e694fd', 'REAL')
p_6036fe = circuit.declare('p_6036fe', 'REAL')
p_feb03e = circuit.declare('p_feb03e', 'REAL')
p_8056eb = circuit.declare('p_8056eb', 'REAL')
p_02880f = circuit.declare('p_02880f', 'REAL')
p_2ba9cb = circuit.declare('p_2ba9cb', 'REAL')
p_383aef = circuit.declare('p_383aef', 'REAL')
p_22cd76 = circuit.declare('p_22cd76', 'REAL')
p_13a733 = circuit.declare('p_13a733', 'REAL')
p_4c6189 = circuit.declare('p_4c6189', 'REAL')
p_4e6bd3 = circuit.declare('p_4e6bd3', 'REAL')
p_872d56 = circuit.declare('p_872d56', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXGate", "TGate", "U2Gate", "ZGate", "XGate", "RZGate", "CUGate", "RZZGate", "SdgGate", "CU1Gate", "RYYGate", "CRXGate", "CSXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_02880f, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_f36ce2, 0, 6 ))
circuit.inst(Gates.CRZGate(p_a02e63, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_22cd76)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_6036fe, 1, 7 ))
circuit.inst(Gates.RZGate(p_3c5b38, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_2ba9cb, 4, 0 ))
circuit.inst(Gates.CRXGate(p_13a733, 6, 4 ))
circuit.inst(Gates.RZZGate(p_383aef)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_4c6189, 4 ))
circuit.inst(Gates.CRXGate(p_feb03e, 0, 3 ))
circuit.inst(Gates.CUGate(p_872d56, p_2be356, 3.1562533916051736, p_8056eb, 6, 2 ))
circuit.inst(Gates.U2Gate(p_4e6bd3, p_e694fd)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(p_230af2)( 3, 4 ))
circuit.inst(Gates.TGate( 5 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_f36ce2": 5.987304452123941,
    "p_3c5b38": 4.229610589867865,
    "p_2be356": 5.0063780207098425,
    "p_a02e63": 1.0296448789776642,
    "p_230af2": 3.950837470808744,
    "p_e694fd": 2.1276323672732023,
    "p_6036fe": 4.167661441102218,
    "p_feb03e": 0.7279391018916035,
    "p_8056eb": 4.940217775579305,
    "p_02880f": 6.163759533339787,
    "p_2ba9cb": 3.2142159669963557,
    "p_383aef": 5.1829934776392745,
    "p_22cd76": 1.740253089260498,
    "p_13a733": 5.94477504571567,
    "p_4c6189": 3.775592041307464,
    "p_4e6bd3": 2.5163050709890156,
    "p_872d56": 5.03147076606842
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

