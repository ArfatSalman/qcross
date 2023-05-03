
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_d1553a = circuit.declare('p_d1553a', 'REAL')
p_adbb08 = circuit.declare('p_adbb08', 'REAL')
p_4a8bf2 = circuit.declare('p_4a8bf2', 'REAL')
p_78abd9 = circuit.declare('p_78abd9', 'REAL')

defns = get_custom_get_definitions("CUGate", "RZZGate", "RZGate", "CU1Gate", "CSXGate", "CHGate", "iSwapGate", "XGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_4a8bf2, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_78abd9, 5.897054719225356, p_d1553a, 5.987304452123941, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_adbb08, 3, 0 ))
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
    "p_d1553a": 2.3864521352475245,
    "p_adbb08": 5.154187354656876,
    "p_4a8bf2": 6.163759533339787,
    "p_78abd9": 0.5112149185250571
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

