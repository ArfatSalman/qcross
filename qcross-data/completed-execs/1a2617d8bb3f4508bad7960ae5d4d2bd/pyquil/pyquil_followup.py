
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 2)

p_c44195 = circuit.declare('p_c44195', 'REAL')
p_79c15b = circuit.declare('p_79c15b', 'REAL')
p_d72302 = circuit.declare('p_d72302', 'REAL')
p_f05a11 = circuit.declare('p_f05a11', 'REAL')
p_381d88 = circuit.declare('p_381d88', 'REAL')
p_3f6521 = circuit.declare('p_3f6521', 'REAL')
p_24e500 = circuit.declare('p_24e500', 'REAL')

defns = get_custom_get_definitions("SXGate", "TGate", "SGate", "ZGate", "RYYGate", "RZZGate", "CHGate", "CRZGate", "SXdgGate", "XGate", "RZGate", "CSXGate", "CU1Gate", "iSwapGate", "ECRGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZZGate(6.163759533339787)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_79c15b)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_24e500, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_381d88, 1 ))
circuit.inst(Gates.RZGate(5.512260524440591, 1 ))
circuit.inst(Gates.CU1Gate(p_3f6521, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(6.086884486572108)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(p_c44195)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_f05a11, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_d72302)( 1, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_c44195": 3.3705408413231095,
    "p_79c15b": 1.977559237989846,
    "p_d72302": 5.167261531657622,
    "p_f05a11": 5.190931186022931,
    "p_381d88": 5.320621737498446,
    "p_3f6521": 1.6723037552953224,
    "p_24e500": 2.2498881927557752
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

