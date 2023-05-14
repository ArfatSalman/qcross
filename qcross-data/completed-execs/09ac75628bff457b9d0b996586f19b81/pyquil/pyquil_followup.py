
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_b2b67d = circuit.declare('p_b2b67d', 'REAL')
p_4c7bdf = circuit.declare('p_4c7bdf', 'REAL')
p_543c46 = circuit.declare('p_543c46', 'REAL')
p_86736a = circuit.declare('p_86736a', 'REAL')

defns = get_custom_get_definitions("C3SXGate", "CCXGate", "ZGate", "RZGate", "TGate", "CRZGate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(p_543c46, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_86736a, 2, 4 ))
circuit.inst(Gates.CUGate(p_b2b67d, p_4c7bdf, 2.3864521352475245, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))

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
    "p_b2b67d": 0.5112149185250571,
    "p_4c7bdf": 5.897054719225356,
    "p_543c46": 6.163759533339787,
    "p_86736a": 4.2641612072511235
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

