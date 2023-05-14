
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_b6dd52 = circuit.declare('p_b6dd52', 'REAL')
p_02ac66 = circuit.declare('p_02ac66', 'REAL')
p_f623a3 = circuit.declare('p_f623a3', 'REAL')
p_57e546 = circuit.declare('p_57e546', 'REAL')
p_e01555 = circuit.declare('p_e01555', 'REAL')
p_3851a3 = circuit.declare('p_3851a3', 'REAL')
p_736182 = circuit.declare('p_736182', 'REAL')
p_8b193d = circuit.declare('p_8b193d', 'REAL')
p_0d1cd9 = circuit.declare('p_0d1cd9', 'REAL')
p_5da4d4 = circuit.declare('p_5da4d4', 'REAL')
p_414184 = circuit.declare('p_414184', 'REAL')
p_2096e5 = circuit.declare('p_2096e5', 'REAL')
p_b24006 = circuit.declare('p_b24006', 'REAL')
p_304e0e = circuit.declare('p_304e0e', 'REAL')
p_d9a218 = circuit.declare('p_d9a218', 'REAL')
p_8522da = circuit.declare('p_8522da', 'REAL')

defns = get_custom_get_definitions("TGate", "CRZGate", "UGate", "SXGate", "CUGate", "CCXGate", "RCCXGate", "RZZGate", "CRXGate", "C3SXGate", "RZGate", "ZGate", "CU1Gate", "SGate")

circuit += defns

circuit.inst(Gates.RZGate(p_3851a3, 2 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(p_2096e5, 1, 2 ))
circuit.inst(Gates.CUGate(p_f623a3, 5.897054719225356, p_57e546, p_b24006, 1, 4 ))
circuit.inst(Gates.C3SXGate( 3, 2, 0, 1 ))
circuit.inst(Gates.CCXGate( 3, 5, 0 ))
circuit.inst(Gates.C3SXGate( 2, 4, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.RCCXGate( 5, 4, 2 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(p_d9a218, 3, 5 ))
circuit.inst(Gates.RZGate(p_8b193d, 3 ))
circuit.inst(Gates.C3SXGate( 0, 1, 3, 4 ))
circuit.inst(Gates.CU1Gate(p_e01555, 4, 0 ))
circuit.inst(Gates.UGate(p_736182, p_5da4d4, p_304e0e)( 5 ))
circuit.inst(Gates.RZZGate(p_02ac66)( 0, 5 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CRZGate(p_414184, 0, 5 ))
circuit.inst(Gates.CU1Gate(p_b6dd52, 3, 2 ))
circuit.inst(Gates.C3SXGate( 4, 0, 2, 1 ))
circuit.inst(Gates.CRZGate(p_8522da, 1, 5 ))
circuit.inst(Gates.CRXGate(p_0d1cd9, 2, 5 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(3, qr[1])
circuit += MEASURE(1, qr[2])
circuit += MEASURE(4, qr[3])
circuit += MEASURE(2, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_b6dd52": 4.028174522740928,
    "p_02ac66": 5.1829934776392745,
    "p_f623a3": 0.5112149185250571,
    "p_57e546": 2.3864521352475245,
    "p_e01555": 3.2142159669963557,
    "p_3851a3": 6.163759533339787,
    "p_736182": 5.887184334931191,
    "p_8b193d": 4.229610589867865,
    "p_0d1cd9": 2.6687018103754414,
    "p_5da4d4": 0.07157463504881167,
    "p_414184": 4.833923139882297,
    "p_2096e5": 4.2641612072511235,
    "p_b24006": 5.987304452123941,
    "p_304e0e": 1.4112277317699358,
    "p_d9a218": 4.167661441102218,
    "p_8522da": 2.586208953975239
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

