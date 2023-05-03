
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_07b76a = circuit.declare('p_07b76a', 'REAL')
p_33dcc3 = circuit.declare('p_33dcc3', 'REAL')
p_a535bd = circuit.declare('p_a535bd', 'REAL')
p_ec8253 = circuit.declare('p_ec8253', 'REAL')
p_fd45fe = circuit.declare('p_fd45fe', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "ZGate", "CU1Gate", "CRZGate", "C3SXGate", "RZGate", "TGate", "SGate", "CCXGate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_ec8253, 2, 4 ))
circuit.inst(Gates.CUGate(p_a535bd, 5.897054719225356, p_07b76a, p_33dcc3, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 5 ))
circuit.inst(Gates.RZGate(p_fd45fe, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))

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
    "p_07b76a": 2.3864521352475245,
    "p_33dcc3": 5.987304452123941,
    "p_a535bd": 0.5112149185250571,
    "p_ec8253": 4.2641612072511235,
    "p_fd45fe": 4.229610589867865
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

