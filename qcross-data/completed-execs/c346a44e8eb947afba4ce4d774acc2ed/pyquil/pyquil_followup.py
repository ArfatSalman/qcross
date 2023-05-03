
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_dcc7c3 = circuit.declare('p_dcc7c3', 'REAL')
p_883ff5 = circuit.declare('p_883ff5', 'REAL')
p_cbd7c7 = circuit.declare('p_cbd7c7', 'REAL')
p_ac7c01 = circuit.declare('p_ac7c01', 'REAL')
p_a8d127 = circuit.declare('p_a8d127', 'REAL')
p_464996 = circuit.declare('p_464996', 'REAL')
p_cdc516 = circuit.declare('p_cdc516', 'REAL')
p_f56c05 = circuit.declare('p_f56c05', 'REAL')
p_93f2a9 = circuit.declare('p_93f2a9', 'REAL')
p_1c4575 = circuit.declare('p_1c4575', 'REAL')

defns = get_custom_get_definitions("C3SXGate", "RYYGate", "SXGate", "CRXGate", "CU1Gate", "CSXGate", "ZGate", "XGate", "RZZGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_883ff5, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_a8d127, 0, 6 ))
circuit.inst(Gates.CRZGate(p_f56c05, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_1c4575)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_cdc516, 1, 7 ))
circuit.inst(Gates.RZGate(p_93f2a9, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_cbd7c7, 4, 0 ))
circuit.inst(Gates.CRXGate(p_464996, 6, 4 ))
circuit.inst(Gates.RZZGate(p_dcc7c3)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_ac7c01, 4 ))

qr_96a3f9 = circuit.declare("qr_96a3f9", "BIT", 6)

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
    "p_dcc7c3": 5.1829934776392745,
    "p_883ff5": 6.163759533339787,
    "p_cbd7c7": 3.2142159669963557,
    "p_ac7c01": 3.775592041307464,
    "p_a8d127": 5.987304452123941,
    "p_464996": 5.94477504571567,
    "p_cdc516": 4.167661441102218,
    "p_f56c05": 1.0296448789776642,
    "p_93f2a9": 4.229610589867865,
    "p_1c4575": 1.740253089260498
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

