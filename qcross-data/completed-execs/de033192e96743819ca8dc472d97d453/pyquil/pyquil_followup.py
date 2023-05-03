
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_72af2c = circuit.declare('p_72af2c', 'REAL')
p_5ed9e5 = circuit.declare('p_5ed9e5', 'REAL')
p_d7cead = circuit.declare('p_d7cead', 'REAL')
p_6a555a = circuit.declare('p_6a555a', 'REAL')
p_86b1e1 = circuit.declare('p_86b1e1', 'REAL')
p_02e598 = circuit.declare('p_02e598', 'REAL')
p_c6dce3 = circuit.declare('p_c6dce3', 'REAL')
p_7d8767 = circuit.declare('p_7d8767', 'REAL')
p_6849dc = circuit.declare('p_6849dc', 'REAL')
p_84dd61 = circuit.declare('p_84dd61', 'REAL')
p_7fd6f3 = circuit.declare('p_7fd6f3', 'REAL')
p_1a3b94 = circuit.declare('p_1a3b94', 'REAL')
p_2d35e2 = circuit.declare('p_2d35e2', 'REAL')
p_ba2c5d = circuit.declare('p_ba2c5d', 'REAL')

defns = get_custom_get_definitions("CU1Gate", "RZZGate", "CUGate", "SXGate", "TGate", "ZGate", "RZGate", "RCCXGate", "SGate", "CCXGate", "CRZGate", "C3SXGate", "UGate")

circuit += defns

circuit.inst(Gates.RZGate(p_6a555a, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_7fd6f3, 2, 4 ))
circuit.inst(Gates.CUGate(p_c6dce3, p_6849dc, p_d7cead, p_7d8767, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 5 ))
circuit.inst(Gates.RZGate(p_2d35e2, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_02e598, 3, 0 ))
circuit.inst(Gates.UGate(p_ba2c5d, p_86b1e1, p_72af2c)( 5 ))
circuit.inst(Gates.RZZGate(p_1a3b94)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(p_5ed9e5, 0, 5 ))
circuit.inst(Gates.CU1Gate(p_84dd61, 1, 4 ))

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
    "p_72af2c": 1.4112277317699358,
    "p_5ed9e5": 4.833923139882297,
    "p_d7cead": 2.3864521352475245,
    "p_6a555a": 6.163759533339787,
    "p_86b1e1": 0.07157463504881167,
    "p_02e598": 3.2142159669963557,
    "p_c6dce3": 0.5112149185250571,
    "p_7d8767": 5.987304452123941,
    "p_6849dc": 5.897054719225356,
    "p_84dd61": 4.028174522740928,
    "p_7fd6f3": 4.2641612072511235,
    "p_1a3b94": 5.1829934776392745,
    "p_2d35e2": 4.229610589867865,
    "p_ba2c5d": 5.887184334931191
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

