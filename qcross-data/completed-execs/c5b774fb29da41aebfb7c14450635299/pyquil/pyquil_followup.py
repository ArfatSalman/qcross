
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_52c643 = circuit.declare('p_52c643', 'REAL')
p_827e55 = circuit.declare('p_827e55', 'REAL')
p_8ff258 = circuit.declare('p_8ff258', 'REAL')
p_7054b2 = circuit.declare('p_7054b2', 'REAL')
p_e129ef = circuit.declare('p_e129ef', 'REAL')
p_11ec22 = circuit.declare('p_11ec22', 'REAL')
p_d24d8a = circuit.declare('p_d24d8a', 'REAL')

defns = get_custom_get_definitions("XGate", "CU1Gate", "RZZGate", "iSwapGate", "CUGate", "CHGate", "CSXGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_e129ef, 1 ))
circuit.inst(Gates.RZZGate(p_52c643)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_11ec22, p_d24d8a, p_827e55, p_8ff258, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_7054b2, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_52c643": 4.066449154047175,
    "p_827e55": 2.3864521352475245,
    "p_8ff258": 5.987304452123941,
    "p_7054b2": 5.154187354656876,
    "p_e129ef": 6.163759533339787,
    "p_11ec22": 0.5112149185250571,
    "p_d24d8a": 5.897054719225356
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

