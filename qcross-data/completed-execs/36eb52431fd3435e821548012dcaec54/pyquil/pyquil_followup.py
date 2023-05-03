
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 4)

p_9dd91c = circuit.declare('p_9dd91c', 'REAL')
p_690702 = circuit.declare('p_690702', 'REAL')
p_8462b4 = circuit.declare('p_8462b4', 'REAL')
p_9bc049 = circuit.declare('p_9bc049', 'REAL')
p_d09863 = circuit.declare('p_d09863', 'REAL')
p_ce5af2 = circuit.declare('p_ce5af2', 'REAL')
p_e73f3b = circuit.declare('p_e73f3b', 'REAL')
p_8423e3 = circuit.declare('p_8423e3', 'REAL')

defns = get_custom_get_definitions("RYYGate", "C3SXGate", "XGate", "TGate", "SXdgGate", "SGate", "RZGate", "CSXGate", "RCCXGate", "CU1Gate", "CHGate", "iSwapGate", "RZZGate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(p_9bc049, 1 ))
circuit.inst(Gates.RZZGate(p_9dd91c)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_ce5af2, p_e73f3b, p_8423e3, p_690702, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_8462b4, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(p_d09863)( 2, 0 ))
circuit.inst(Gates.RCCXGate( 2, 3, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.SGate( 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_9dd91c": 4.066449154047175,
    "p_690702": 5.987304452123941,
    "p_8462b4": 5.154187354656876,
    "p_9bc049": 6.163759533339787,
    "p_d09863": 1.740253089260498,
    "p_ce5af2": 0.5112149185250571,
    "p_e73f3b": 5.897054719225356,
    "p_8423e3": 2.3864521352475245
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

