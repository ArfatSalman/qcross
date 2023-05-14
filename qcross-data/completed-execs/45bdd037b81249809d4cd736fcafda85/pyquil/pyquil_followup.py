
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_64ae37 = circuit.declare('p_64ae37', 'REAL')
p_e820f6 = circuit.declare('p_e820f6', 'REAL')
p_a4b6c0 = circuit.declare('p_a4b6c0', 'REAL')

defns = get_custom_get_definitions("RYYGate", "iSwapGate", "SXGate", "XGate", "CHGate", "CSXGate", "RZGate", "RZZGate", "CRXGate", "CRZGate", "CU1Gate", "SXdgGate", "TGate", "ECRGate")

circuit += defns

circuit.inst(Gates.RZZGate(p_64ae37)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_a4b6c0)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(p_e820f6, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(2.2498881927557752, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(5.320621737498446, 1 ))
circuit.inst(Gates.RZGate(5.512260524440591, 1 ))
circuit.inst(Gates.CU1Gate(1.6723037552953224, 0, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_64ae37": 6.163759533339787,
    "p_e820f6": 5.987304452123941,
    "p_a4b6c0": 1.977559237989846
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

