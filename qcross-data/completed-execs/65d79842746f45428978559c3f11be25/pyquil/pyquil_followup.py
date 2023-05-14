
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_1ee909 = circuit.declare('p_1ee909', 'REAL')
p_8f01e6 = circuit.declare('p_8f01e6', 'REAL')
p_c6f972 = circuit.declare('p_c6f972', 'REAL')
p_924711 = circuit.declare('p_924711', 'REAL')
p_58a2b5 = circuit.declare('p_58a2b5', 'REAL')
p_4927d2 = circuit.declare('p_4927d2', 'REAL')
p_cc3cec = circuit.declare('p_cc3cec', 'REAL')
p_8e5127 = circuit.declare('p_8e5127', 'REAL')
p_4616e5 = circuit.declare('p_4616e5', 'REAL')
p_cc7cb0 = circuit.declare('p_cc7cb0', 'REAL')
p_1adccb = circuit.declare('p_1adccb', 'REAL')
p_683702 = circuit.declare('p_683702', 'REAL')
p_ba4e5e = circuit.declare('p_ba4e5e', 'REAL')

defns = get_custom_get_definitions("TGate", "C3SXGate", "ZGate", "SGate", "RCCXGate", "RZZGate", "CRZGate", "CCXGate", "CUGate", "UGate", "CU1Gate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_1ee909, 3 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(p_1adccb, 5, 3 ))
circuit.inst(Gates.CUGate(p_4616e5, p_924711, p_c6f972, p_ba4e5e, 5, 4 ))
circuit.inst(Gates.C3SXGate( 1, 3, 0, 5 ))
circuit.inst(Gates.CCXGate( 1, 2, 0 ))
circuit.inst(Gates.C3SXGate( 3, 4, 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.RCCXGate( 2, 4, 3 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CRZGate(p_8e5127, 1, 2 ))
circuit.inst(Gates.RZGate(p_cc3cec, 1 ))
circuit.inst(Gates.C3SXGate( 0, 5, 1, 4 ))
circuit.inst(Gates.CU1Gate(p_cc7cb0, 4, 0 ))
circuit.inst(Gates.UGate(p_8f01e6, p_4927d2, p_683702)( 2 ))
circuit.inst(Gates.RZZGate(p_58a2b5)( 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(4, qr[3])
circuit += MEASURE(3, qr[4])
circuit += MEASURE(2, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_1ee909": 6.163759533339787,
    "p_8f01e6": 5.887184334931191,
    "p_c6f972": 2.3864521352475245,
    "p_924711": 5.897054719225356,
    "p_58a2b5": 5.1829934776392745,
    "p_4927d2": 0.07157463504881167,
    "p_cc3cec": 4.229610589867865,
    "p_8e5127": 4.167661441102218,
    "p_4616e5": 0.5112149185250571,
    "p_cc7cb0": 3.2142159669963557,
    "p_1adccb": 4.2641612072511235,
    "p_683702": 1.4112277317699358,
    "p_ba4e5e": 5.987304452123941
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

