
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_8fbc55 = circuit.declare('p_8fbc55', 'REAL')
p_57585f = circuit.declare('p_57585f', 'REAL')
p_285ae7 = circuit.declare('p_285ae7', 'REAL')
p_0602a6 = circuit.declare('p_0602a6', 'REAL')
p_0a2147 = circuit.declare('p_0a2147', 'REAL')
p_bb1901 = circuit.declare('p_bb1901', 'REAL')
p_82597a = circuit.declare('p_82597a', 'REAL')
p_34e682 = circuit.declare('p_34e682', 'REAL')

defns = get_custom_get_definitions("CRZGate", "C3SXGate", "RCCXGate", "CU1Gate", "CUGate", "SGate", "RZGate", "TGate", "ZGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_34e682, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_0602a6, 2, 4 ))
circuit.inst(Gates.CUGate(p_285ae7, p_bb1901, p_8fbc55, p_57585f, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(p_82597a, 1, 5 ))
circuit.inst(Gates.RZGate(p_0a2147, 1 ))
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
    "p_8fbc55": 2.3864521352475245,
    "p_57585f": 5.987304452123941,
    "p_285ae7": 0.5112149185250571,
    "p_0602a6": 4.2641612072511235,
    "p_0a2147": 4.229610589867865,
    "p_bb1901": 5.897054719225356,
    "p_82597a": 4.167661441102218,
    "p_34e682": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

