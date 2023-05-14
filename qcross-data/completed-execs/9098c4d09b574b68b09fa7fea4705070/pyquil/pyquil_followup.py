
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_eed10c = circuit.declare('p_eed10c', 'REAL')
p_55f179 = circuit.declare('p_55f179', 'REAL')
p_3b8fbf = circuit.declare('p_3b8fbf', 'REAL')
p_0989aa = circuit.declare('p_0989aa', 'REAL')
p_d3bd13 = circuit.declare('p_d3bd13', 'REAL')
p_c0fb12 = circuit.declare('p_c0fb12', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "C3SXGate", "CUGate", "CCXGate", "RZGate", "ZGate", "SGate", "TGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_3b8fbf, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_0989aa, 2, 4 ))
circuit.inst(Gates.CUGate(p_eed10c, p_c0fb12, p_d3bd13, p_55f179, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))

qr_d7d03d = circuit.declare("qr_d7d03d", "BIT", 9)

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
    "p_eed10c": 0.5112149185250571,
    "p_55f179": 5.987304452123941,
    "p_3b8fbf": 6.163759533339787,
    "p_0989aa": 4.2641612072511235,
    "p_d3bd13": 2.3864521352475245,
    "p_c0fb12": 5.897054719225356
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

