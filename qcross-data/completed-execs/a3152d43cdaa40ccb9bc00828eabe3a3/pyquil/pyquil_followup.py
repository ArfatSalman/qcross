
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_668799 = circuit.declare('p_668799', 'REAL')
p_4a9618 = circuit.declare('p_4a9618', 'REAL')
p_68b975 = circuit.declare('p_68b975', 'REAL')
p_4dfb76 = circuit.declare('p_4dfb76', 'REAL')
p_c4dfaf = circuit.declare('p_c4dfaf', 'REAL')

defns = get_custom_get_definitions("ZGate", "CCXGate", "C3SXGate", "CUGate", "TGate", "RZGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_c4dfaf, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_68b975, 2, 4 ))
circuit.inst(Gates.CUGate(p_4dfb76, p_668799, 2.3864521352475245, p_4a9618, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))

qr_70c8ce = circuit.declare("qr_70c8ce", "BIT", 3)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_668799": 5.897054719225356,
    "p_4a9618": 5.987304452123941,
    "p_68b975": 4.2641612072511235,
    "p_4dfb76": 0.5112149185250571,
    "p_c4dfaf": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

