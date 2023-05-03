
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_435387 = circuit.declare('p_435387', 'REAL')
p_ad6c48 = circuit.declare('p_ad6c48', 'REAL')
p_7baf10 = circuit.declare('p_7baf10', 'REAL')
p_3c5bca = circuit.declare('p_3c5bca', 'REAL')

defns = get_custom_get_definitions("CUGate", "iSwapGate", "RZGate", "XGate", "RZZGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_435387, 1 ))
circuit.inst(Gates.RZZGate(p_7baf10)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_3c5bca, 5.897054719225356, 2.3864521352475245, p_ad6c48, 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_435387": 6.163759533339787,
    "p_ad6c48": 5.987304452123941,
    "p_7baf10": 4.066449154047175,
    "p_3c5bca": 0.5112149185250571
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

