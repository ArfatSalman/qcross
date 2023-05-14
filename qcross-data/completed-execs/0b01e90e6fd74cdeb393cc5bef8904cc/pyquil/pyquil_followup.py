
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_53e66c = circuit.declare('p_53e66c', 'REAL')
p_6b5eeb = circuit.declare('p_6b5eeb', 'REAL')
p_c550ed = circuit.declare('p_c550ed', 'REAL')
p_1bf9a6 = circuit.declare('p_1bf9a6', 'REAL')
p_71ceaf = circuit.declare('p_71ceaf', 'REAL')
p_3b8ed5 = circuit.declare('p_3b8ed5', 'REAL')
p_34c784 = circuit.declare('p_34c784', 'REAL')
p_dc073a = circuit.declare('p_dc073a', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "iSwapGate", "RZZGate", "CRXGate", "RYYGate", "CU1Gate", "TGate", "RZGate", "XGate", "CSXGate", "ECRGate", "SXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZZGate(6.163759533339787)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_53e66c)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(p_34c784, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_dc073a, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_6b5eeb, 1 ))
circuit.inst(Gates.RZGate(p_c550ed, 1 ))
circuit.inst(Gates.CU1Gate(p_71ceaf, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(p_3b8ed5)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(p_1bf9a6)( 0, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_53e66c": 1.977559237989846,
    "p_6b5eeb": 5.320621737498446,
    "p_c550ed": 5.512260524440591,
    "p_1bf9a6": 3.3705408413231095,
    "p_71ceaf": 1.6723037552953224,
    "p_3b8ed5": 6.086884486572108,
    "p_34c784": 5.987304452123941,
    "p_dc073a": 2.2498881927557752
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

