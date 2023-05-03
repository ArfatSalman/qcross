
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_c17d7a = circuit.declare('p_c17d7a', 'REAL')
p_b8f691 = circuit.declare('p_b8f691', 'REAL')
p_abc7bc = circuit.declare('p_abc7bc', 'REAL')
p_61eb28 = circuit.declare('p_61eb28', 'REAL')
p_efb1d9 = circuit.declare('p_efb1d9', 'REAL')

defns = get_custom_get_definitions("SXGate", "RZGate", "CSXGate", "CHGate", "TGate", "CRZGate", "CCXGate", "XGate", "ZGate", "CRXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_abc7bc, 3 ))
circuit.inst(Gates.CRZGate(p_c17d7a, 6, 3 ))
circuit.inst(Gates.CRXGate(p_efb1d9, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_61eb28, 1, 6 ))
circuit.inst(Gates.RZGate(p_b8f691, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))

qr_02ac22 = circuit.declare("qr_02ac22", "BIT", 9)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_c17d7a": 4.2641612072511235,
    "p_b8f691": 4.229610589867865,
    "p_abc7bc": 6.163759533339787,
    "p_61eb28": 4.167661441102218,
    "p_efb1d9": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

