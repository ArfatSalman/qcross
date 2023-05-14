
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_d13af9 = circuit.declare('p_d13af9', 'REAL')
p_baa0bd = circuit.declare('p_baa0bd', 'REAL')
p_feab72 = circuit.declare('p_feab72', 'REAL')
p_536ad5 = circuit.declare('p_536ad5', 'REAL')

defns = get_custom_get_definitions("CUGate", "RZZGate", "iSwapGate", "RZGate", "CSXGate", "XGate")

circuit += defns

circuit.inst(Gates.RZGate(p_d13af9, 1 ))
circuit.inst(Gates.RZZGate(p_feab72)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_536ad5, 5.897054719225356, 2.3864521352475245, p_baa0bd, 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_d13af9": 6.163759533339787,
    "p_baa0bd": 5.987304452123941,
    "p_feab72": 4.066449154047175,
    "p_536ad5": 0.5112149185250571
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

