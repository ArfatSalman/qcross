
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_bdf701 = circuit.declare('p_bdf701', 'REAL')
p_9d6cc2 = circuit.declare('p_9d6cc2', 'REAL')
p_86ace7 = circuit.declare('p_86ace7', 'REAL')
p_8bc5a1 = circuit.declare('p_8bc5a1', 'REAL')
p_3abe65 = circuit.declare('p_3abe65', 'REAL')
p_28fe7c = circuit.declare('p_28fe7c', 'REAL')
p_ec0d90 = circuit.declare('p_ec0d90', 'REAL')

defns = get_custom_get_definitions("XGate", "CU1Gate", "RZZGate", "iSwapGate", "CUGate", "CHGate", "CSXGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_3abe65, 1 ))
circuit.inst(Gates.RZZGate(p_bdf701)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_ec0d90, p_28fe7c, p_9d6cc2, p_86ace7, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_8bc5a1, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_bdf701": 4.066449154047175,
    "p_9d6cc2": 2.3864521352475245,
    "p_86ace7": 5.987304452123941,
    "p_8bc5a1": 5.154187354656876,
    "p_3abe65": 6.163759533339787,
    "p_28fe7c": 5.897054719225356,
    "p_ec0d90": 0.5112149185250571
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

