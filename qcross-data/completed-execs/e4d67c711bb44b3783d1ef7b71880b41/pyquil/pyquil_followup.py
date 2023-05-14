
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_3be9dd = circuit.declare('p_3be9dd', 'REAL')
p_7c0930 = circuit.declare('p_7c0930', 'REAL')
p_1ba891 = circuit.declare('p_1ba891', 'REAL')
p_c8dca5 = circuit.declare('p_c8dca5', 'REAL')
p_abdae9 = circuit.declare('p_abdae9', 'REAL')
p_fd3e2d = circuit.declare('p_fd3e2d', 'REAL')
p_177252 = circuit.declare('p_177252', 'REAL')

defns = get_custom_get_definitions("XGate", "RZGate", "CUGate", "RZZGate", "CU1Gate", "iSwapGate", "CHGate", "CSXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_1ba891, 1 ))
circuit.inst(Gates.RZZGate(p_fd3e2d)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_c8dca5, p_177252, p_3be9dd, p_abdae9, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_7c0930, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_3be9dd": 2.3864521352475245,
    "p_7c0930": 5.154187354656876,
    "p_1ba891": 6.163759533339787,
    "p_c8dca5": 0.5112149185250571,
    "p_abdae9": 5.987304452123941,
    "p_fd3e2d": 4.066449154047175,
    "p_177252": 5.897054719225356
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

