
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 6)

p_2f6fa1 = circuit.declare('p_2f6fa1', 'REAL')
p_d2b7ff = circuit.declare('p_d2b7ff', 'REAL')
p_796036 = circuit.declare('p_796036', 'REAL')
p_deb987 = circuit.declare('p_deb987', 'REAL')
p_f98523 = circuit.declare('p_f98523', 'REAL')
p_31d9e7 = circuit.declare('p_31d9e7', 'REAL')
p_7d1017 = circuit.declare('p_7d1017', 'REAL')

defns = get_custom_get_definitions("CRZGate", "iSwapGate", "C3SXGate", "RCCXGate", "RZZGate", "CU1Gate", "CUGate", "SGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "UGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_d2b7ff, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(p_2f6fa1, p_31d9e7, p_deb987, p_f98523, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.RZZGate(5.017245588344839)( 0, 1 ))
subcircuit.inst(Gates.iSwapGate( 3, 2 ))
subcircuit.inst(Gates.XGate( 0 ))
subcircuit.inst(Gates.CSXGate( 0, 1 ))
subcircuit.inst(Gates.RCCXGate( 4, 5, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 5 ))
circuit.inst(Gates.RZGate(p_796036, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, p_7d1017, 1.4112277317699358)( 5 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 0, 5 ))

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
    "p_2f6fa1": 0.5112149185250571,
    "p_d2b7ff": 6.163759533339787,
    "p_796036": 4.229610589867865,
    "p_deb987": 2.3864521352475245,
    "p_f98523": 5.987304452123941,
    "p_31d9e7": 5.897054719225356,
    "p_7d1017": 0.07157463504881167
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

