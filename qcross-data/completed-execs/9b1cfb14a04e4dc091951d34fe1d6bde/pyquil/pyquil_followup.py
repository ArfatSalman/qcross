
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)

p_897886 = circuit.declare('p_897886', 'REAL')
p_0477e2 = circuit.declare('p_0477e2', 'REAL')
p_343721 = circuit.declare('p_343721', 'REAL')
p_837a0a = circuit.declare('p_837a0a', 'REAL')
p_31e933 = circuit.declare('p_31e933', 'REAL')
p_b58743 = circuit.declare('p_b58743', 'REAL')
p_a36cb0 = circuit.declare('p_a36cb0', 'REAL')
p_966369 = circuit.declare('p_966369', 'REAL')
p_a7959d = circuit.declare('p_a7959d', 'REAL')

defns = get_custom_get_definitions("ZGate", "CHGate", "CU1Gate", "SGate", "SXGate", "C3SXGate", "CUGate", "XGate", "U2Gate", "RZGate", "CRZGate", "CSXGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_343721, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_31e933, p_897886, p_a36cb0, p_a7959d, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_837a0a, 8, 3 ))
circuit.inst(Gates.CRZGate(p_b58743, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(p_0477e2, 1, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, p_966369)( 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_897886": 5.897054719225356,
    "p_0477e2": 2.586208953975239,
    "p_343721": 6.163759533339787,
    "p_837a0a": 3.2142159669963557,
    "p_31e933": 0.5112149185250571,
    "p_b58743": 1.4112277317699358,
    "p_a36cb0": 2.3864521352475245,
    "p_966369": 2.1276323672732023,
    "p_a7959d": 5.987304452123941
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

