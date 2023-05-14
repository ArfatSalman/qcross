
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_028c2d = circuit.declare('p_028c2d', 'REAL')
p_77e236 = circuit.declare('p_77e236', 'REAL')
p_0f0077 = circuit.declare('p_0f0077', 'REAL')

defns = get_custom_get_definitions("CHGate", "CCXGate", "ZGate", "RZGate", "SGate", "iSwapGate", "SdgGate", "CRXGate", "RYYGate", "XGate", "CSXGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_028c2d, 1 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.CSXGate( 1, 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(p_0f0077, 2, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CCXGate( 1, 2, 0 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.RYYGate(p_77e236)( 1, 2 ))
circuit.inst(Gates.ZGate( 0 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(0, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_028c2d": 6.163759533339787,
    "p_77e236": 1.6723037552953224,
    "p_0f0077": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

