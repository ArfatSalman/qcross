
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 4)

p_549fef = circuit.declare('p_549fef', 'REAL')
p_6e5194 = circuit.declare('p_6e5194', 'REAL')
p_afd57c = circuit.declare('p_afd57c', 'REAL')
p_78f5ff = circuit.declare('p_78f5ff', 'REAL')
p_2d015c = circuit.declare('p_2d015c', 'REAL')

defns = get_custom_get_definitions("iSwapGate", "RZZGate", "CU1Gate", "CUGate", "RZGate", "XGate", "CSXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_549fef, p_78f5ff, p_2d015c, p_6e5194, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_afd57c, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_549fef": 0.5112149185250571,
    "p_6e5194": 5.987304452123941,
    "p_afd57c": 5.154187354656876,
    "p_78f5ff": 5.897054719225356,
    "p_2d015c": 2.3864521352475245
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

