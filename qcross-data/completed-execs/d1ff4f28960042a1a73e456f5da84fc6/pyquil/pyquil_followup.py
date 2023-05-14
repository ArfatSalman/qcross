
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_4b58f7 = circuit.declare('p_4b58f7', 'REAL')
p_b10c48 = circuit.declare('p_b10c48', 'REAL')
p_da461d = circuit.declare('p_da461d', 'REAL')
p_a1b5f5 = circuit.declare('p_a1b5f5', 'REAL')
p_69e8c5 = circuit.declare('p_69e8c5', 'REAL')
p_eb8e6b = circuit.declare('p_eb8e6b', 'REAL')
p_7fdc7e = circuit.declare('p_7fdc7e', 'REAL')
p_c0b116 = circuit.declare('p_c0b116', 'REAL')
p_669459 = circuit.declare('p_669459', 'REAL')
p_c6c4c2 = circuit.declare('p_c6c4c2', 'REAL')
p_eb23fe = circuit.declare('p_eb23fe', 'REAL')
p_33d287 = circuit.declare('p_33d287', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "CRXGate", "RYYGate", "ZGate", "CU1Gate", "CUGate", "SGate", "RZGate", "TGate", "XGate", "CSXGate", "ECRGate", "UGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_eb8e6b, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_c6c4c2, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_c0b116, p_eb23fe, p_a1b5f5, p_669459, 1, 4 ))
circuit.inst(Gates.RZGate(p_da461d, 1 ))
circuit.inst(Gates.RYYGate(p_7fdc7e)( 0, 2 ))
circuit.inst(Gates.CU1Gate(p_33d287, 3, 0 ))
circuit.inst(Gates.UGate(p_69e8c5, p_4b58f7, p_b10c48)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CHGate( 0, 4 ))
circuit.inst(Gates.CHGate( 0, 1 ))

qr_09ecd4 = circuit.declare("qr_09ecd4", "BIT", 6)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_4b58f7": 0.07157463504881167,
    "p_b10c48": 1.4112277317699358,
    "p_da461d": 4.229610589867865,
    "p_a1b5f5": 4.623446645668956,
    "p_69e8c5": 5.887184334931191,
    "p_eb8e6b": 2.0099472182748075,
    "p_7fdc7e": 5.398622178940033,
    "p_c0b116": 5.708725119517347,
    "p_669459": 3.865496458458116,
    "p_c6c4c2": 1.0296448789776642,
    "p_eb23fe": 4.167661441102218,
    "p_33d287": 3.2142159669963557
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

