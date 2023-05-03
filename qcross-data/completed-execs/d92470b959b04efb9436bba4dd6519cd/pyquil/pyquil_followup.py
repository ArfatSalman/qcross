
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 8)

p_dd8db9 = circuit.declare('p_dd8db9', 'REAL')
p_fbfefd = circuit.declare('p_fbfefd', 'REAL')
p_79e2ca = circuit.declare('p_79e2ca', 'REAL')
p_d2a644 = circuit.declare('p_d2a644', 'REAL')
p_803a1f = circuit.declare('p_803a1f', 'REAL')
p_fd6f6d = circuit.declare('p_fd6f6d', 'REAL')
p_50a615 = circuit.declare('p_50a615', 'REAL')
p_bae028 = circuit.declare('p_bae028', 'REAL')
p_49f1fc = circuit.declare('p_49f1fc', 'REAL')
p_5b9a9c = circuit.declare('p_5b9a9c', 'REAL')
p_4a90e8 = circuit.declare('p_4a90e8', 'REAL')
p_28e9ae = circuit.declare('p_28e9ae', 'REAL')
p_d68182 = circuit.declare('p_d68182', 'REAL')
p_f964c1 = circuit.declare('p_f964c1', 'REAL')
p_02c08d = circuit.declare('p_02c08d', 'REAL')
p_64828e = circuit.declare('p_64828e', 'REAL')
p_1ab04f = circuit.declare('p_1ab04f', 'REAL')

defns = get_custom_get_definitions("RYYGate", "XGate", "RZZGate", "ZGate", "TGate", "CSXGate", "CU1Gate", "CRZGate", "CUGate", "C3SXGate", "SXGate", "CRXGate", "U2Gate", "RZGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_5b9a9c, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_dd8db9, 0, 6 ))
circuit.inst(Gates.CRZGate(p_d2a644, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_d68182)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_50a615, 1, 7 ))
circuit.inst(Gates.RZGate(p_fbfefd, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_4a90e8, 4, 0 ))
circuit.inst(Gates.CRXGate(p_f964c1, 6, 4 ))
circuit.inst(Gates.RZZGate(p_28e9ae)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_02c08d, 4 ))
circuit.inst(Gates.CRXGate(p_bae028, 0, 3 ))
circuit.inst(Gates.CUGate(p_1ab04f, p_79e2ca, 3.1562533916051736, p_49f1fc, 6, 2 ))
circuit.inst(Gates.U2Gate(p_64828e, p_fd6f6d)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(p_803a1f)( 3, 4 ))
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
    "p_dd8db9": 5.987304452123941,
    "p_fbfefd": 4.229610589867865,
    "p_79e2ca": 5.0063780207098425,
    "p_d2a644": 1.0296448789776642,
    "p_803a1f": 3.950837470808744,
    "p_fd6f6d": 2.1276323672732023,
    "p_50a615": 4.167661441102218,
    "p_bae028": 0.7279391018916035,
    "p_49f1fc": 4.940217775579305,
    "p_5b9a9c": 6.163759533339787,
    "p_4a90e8": 3.2142159669963557,
    "p_28e9ae": 5.1829934776392745,
    "p_d68182": 1.740253089260498,
    "p_f964c1": 5.94477504571567,
    "p_02c08d": 3.775592041307464,
    "p_64828e": 2.5163050709890156,
    "p_1ab04f": 5.03147076606842
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        


quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

