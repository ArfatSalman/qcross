
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 8)

p_dcc42c = circuit.declare('p_dcc42c', 'REAL')
p_e95c81 = circuit.declare('p_e95c81', 'REAL')
p_aa5610 = circuit.declare('p_aa5610', 'REAL')
p_68ba36 = circuit.declare('p_68ba36', 'REAL')
p_a73b08 = circuit.declare('p_a73b08', 'REAL')
p_22c7ba = circuit.declare('p_22c7ba', 'REAL')
p_033778 = circuit.declare('p_033778', 'REAL')
p_69de3c = circuit.declare('p_69de3c', 'REAL')
p_79b734 = circuit.declare('p_79b734', 'REAL')

defns = get_custom_get_definitions("CU1Gate", "SdgGate", "CRZGate", "RYYGate", "CSXGate", "CUGate", "RZZGate", "U2Gate", "ZGate", "SXGate", "XGate", "RZGate", "SXdgGate", "TGate", "CRXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_a73b08, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(p_e95c81, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_033778)( 6, 7 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 7 ))
circuit.inst(Gates.RZGate(p_22c7ba, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 6, 4 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_aa5610, 4 ))
circuit.inst(Gates.CRXGate(p_79b734, 0, 3 ))
circuit.inst(Gates.CUGate(5.03147076606842, p_68ba36, 3.1562533916051736, p_69de3c, 6, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 3, 4 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RYYGate(p_dcc42c)( 4, 2 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 5 ))
circuit.inst(Gates.SXdgGate( 7 ))

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
    "p_dcc42c": 1.9669252191306448,
    "p_e95c81": 1.0296448789776642,
    "p_aa5610": 3.775592041307464,
    "p_68ba36": 5.0063780207098425,
    "p_a73b08": 6.163759533339787,
    "p_22c7ba": 4.229610589867865,
    "p_033778": 1.740253089260498,
    "p_69de3c": 4.940217775579305,
    "p_79b734": 0.7279391018916035
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

