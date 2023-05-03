
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 8)

p_143887 = circuit.declare('p_143887', 'REAL')
p_72a534 = circuit.declare('p_72a534', 'REAL')
p_082ec3 = circuit.declare('p_082ec3', 'REAL')
p_fd33bb = circuit.declare('p_fd33bb', 'REAL')
p_c40958 = circuit.declare('p_c40958', 'REAL')
p_106180 = circuit.declare('p_106180', 'REAL')
p_083e1c = circuit.declare('p_083e1c', 'REAL')
p_36e2fe = circuit.declare('p_36e2fe', 'REAL')
p_f20bd4 = circuit.declare('p_f20bd4', 'REAL')
p_ec90c9 = circuit.declare('p_ec90c9', 'REAL')
p_2bbfa0 = circuit.declare('p_2bbfa0', 'REAL')
p_bb3cbe = circuit.declare('p_bb3cbe', 'REAL')
p_8baad8 = circuit.declare('p_8baad8', 'REAL')
p_057fbf = circuit.declare('p_057fbf', 'REAL')
p_0927f4 = circuit.declare('p_0927f4', 'REAL')
p_b8acf2 = circuit.declare('p_b8acf2', 'REAL')
p_1e860b = circuit.declare('p_1e860b', 'REAL')

defns = get_custom_get_definitions("U2Gate", "ZGate", "CU1Gate", "RZZGate", "CRZGate", "XGate", "RZGate", "C3SXGate", "CSXGate", "TGate", "RYYGate", "SXGate", "CUGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_72a534, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_36e2fe, 0, 6 ))
circuit.inst(Gates.CRZGate(p_bb3cbe, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_057fbf)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_0927f4, 1, 7 ))
circuit.inst(Gates.RZGate(p_b8acf2, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_143887, 4, 0 ))
circuit.inst(Gates.CRXGate(p_ec90c9, 6, 4 ))
circuit.inst(Gates.RZZGate(p_fd33bb)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_082ec3, 4 ))
circuit.inst(Gates.CRXGate(p_106180, 0, 3 ))
circuit.inst(Gates.CUGate(p_8baad8, p_2bbfa0, p_c40958, p_1e860b, 6, 2 ))
circuit.inst(Gates.U2Gate(p_f20bd4, p_083e1c)( 2 ))
circuit.inst(Gates.TGate( 6 ))

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
    "p_143887": 3.2142159669963557,
    "p_72a534": 6.163759533339787,
    "p_082ec3": 3.775592041307464,
    "p_fd33bb": 5.1829934776392745,
    "p_c40958": 3.1562533916051736,
    "p_106180": 0.7279391018916035,
    "p_083e1c": 2.1276323672732023,
    "p_36e2fe": 5.987304452123941,
    "p_f20bd4": 2.5163050709890156,
    "p_ec90c9": 5.94477504571567,
    "p_2bbfa0": 5.0063780207098425,
    "p_bb3cbe": 1.0296448789776642,
    "p_8baad8": 5.03147076606842,
    "p_057fbf": 1.740253089260498,
    "p_0927f4": 4.167661441102218,
    "p_b8acf2": 4.229610589867865,
    "p_1e860b": 4.940217775579305
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

