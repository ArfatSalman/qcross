
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_2c5a30 = circuit.declare('p_2c5a30', 'REAL')
p_d8aa57 = circuit.declare('p_d8aa57', 'REAL')
p_90c25c = circuit.declare('p_90c25c', 'REAL')
p_b36eca = circuit.declare('p_b36eca', 'REAL')

defns = get_custom_get_definitions("XGate", "RZGate", "CUGate", "RZZGate", "CU1Gate", "iSwapGate", "CHGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(p_2c5a30)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, p_d8aa57, p_90c25c, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_b36eca, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_2c5a30": 4.066449154047175,
    "p_d8aa57": 2.3864521352475245,
    "p_90c25c": 5.987304452123941,
    "p_b36eca": 5.154187354656876
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

