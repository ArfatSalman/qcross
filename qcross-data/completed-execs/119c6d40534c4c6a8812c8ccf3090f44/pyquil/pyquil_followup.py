
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_4891c3 = circuit.declare('p_4891c3', 'REAL')
p_4d6844 = circuit.declare('p_4d6844', 'REAL')
p_72b19d = circuit.declare('p_72b19d', 'REAL')
p_1dbd94 = circuit.declare('p_1dbd94', 'REAL')
p_ab8a7b = circuit.declare('p_ab8a7b', 'REAL')

defns = get_custom_get_definitions("C3XGate", "CPhaseGate", "CU3Gate", "SdgGate", "CHGate", "CZGate", "SGate", "IGate", "RYYGate")

circuit += defns

circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.RYYGate(2.10593478876119)( 2, 1 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CZGate( 2, 3 ))
circuit.inst(Gates.CZGate( 0, 3 ))
circuit.inst(Gates.CZGate( 1, 2 ))
circuit.inst(Gates.CU3Gate(p_72b19d, p_4891c3, p_4d6844, 2, 0 ))
circuit.inst(Gates.CHGate( 2, 3 ))
circuit.inst(Gates.CPhaseGate(p_1dbd94, 2, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.C3XGate( 3, 1, 2, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_4891c3": 3.7847055340640803,
    "p_4d6844": 5.596894918056728,
    "p_72b19d": 5.177552214723695,
    "p_1dbd94": 5.982058731459433,
    "p_ab8a7b": 0.45470685223891605
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

