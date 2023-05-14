
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_023a7d = circuit.declare('p_023a7d', 'REAL')
p_21ba07 = circuit.declare('p_21ba07', 'REAL')
p_4a69b2 = circuit.declare('p_4a69b2', 'REAL')
p_b96fd4 = circuit.declare('p_b96fd4', 'REAL')
p_1c6cdf = circuit.declare('p_1c6cdf', 'REAL')
p_7d7c65 = circuit.declare('p_7d7c65', 'REAL')
p_66e932 = circuit.declare('p_66e932', 'REAL')
p_8b6baf = circuit.declare('p_8b6baf', 'REAL')
p_9ec620 = circuit.declare('p_9ec620', 'REAL')
p_628297 = circuit.declare('p_628297', 'REAL')
p_4c04c2 = circuit.declare('p_4c04c2', 'REAL')
p_f3b666 = circuit.declare('p_f3b666', 'REAL')
p_edb705 = circuit.declare('p_edb705', 'REAL')
p_1a21da = circuit.declare('p_1a21da', 'REAL')
p_52c99c = circuit.declare('p_52c99c', 'REAL')
p_7fc368 = circuit.declare('p_7fc368', 'REAL')
p_ad4dbb = circuit.declare('p_ad4dbb', 'REAL')
p_d7b9ee = circuit.declare('p_d7b9ee', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "C3SXGate", "RCCXGate", "CRXGate", "RZZGate", "CU3Gate", "RYYGate", "CU1Gate", "CUGate", "RZGate", "TGate", "XGate", "CSXGate", "RXGate", "ZGate", "SdgGate", "SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_7fc368, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_1a21da, 0, 6 ))
circuit.inst(Gates.CRZGate(p_52c99c, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_d7b9ee)( 6, 7 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 7 ))
circuit.inst(Gates.RZGate(p_1c6cdf, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_7d7c65, 4, 0 ))
circuit.inst(Gates.CRXGate(p_4a69b2, 6, 4 ))
circuit.inst(Gates.RZZGate(p_f3b666)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_66e932, 4 ))
circuit.inst(Gates.CRXGate(p_edb705, 0, 3 ))
circuit.inst(Gates.CUGate(p_21ba07, p_628297, p_8b6baf, p_023a7d, 6, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CU3Gate(5.583322729510212, 4.773422973876057, 0.8960434543694032, 4, 3 ))
subcircuit.inst(Gates.RCCXGate( 1, 6, 7 ))
subcircuit.inst(Gates.RXGate(1.723121374211541, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.U2Gate(p_b96fd4, p_ad4dbb)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(p_9ec620)( 3, 4 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RYYGate(p_4c04c2)( 4, 2 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 5 ))

qr_b7d75d = circuit.declare("qr_b7d75d", "BIT", 4)

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
    "p_023a7d": 4.940217775579305,
    "p_21ba07": 5.03147076606842,
    "p_4a69b2": 5.94477504571567,
    "p_b96fd4": 2.5163050709890156,
    "p_1c6cdf": 4.229610589867865,
    "p_7d7c65": 3.2142159669963557,
    "p_66e932": 3.775592041307464,
    "p_8b6baf": 3.1562533916051736,
    "p_9ec620": 3.950837470808744,
    "p_628297": 5.0063780207098425,
    "p_4c04c2": 1.9669252191306448,
    "p_f3b666": 5.1829934776392745,
    "p_edb705": 0.7279391018916035,
    "p_1a21da": 5.987304452123941,
    "p_52c99c": 1.0296448789776642,
    "p_7fc368": 6.163759533339787,
    "p_ad4dbb": 2.1276323672732023,
    "p_d7b9ee": 1.740253089260498
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

