
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_445472 = circuit.declare('p_445472', 'REAL')
p_893583 = circuit.declare('p_893583', 'REAL')
p_99b2af = circuit.declare('p_99b2af', 'REAL')

defns = get_custom_get_definitions("RYYGate", "iSwapGate", "SXGate", "XGate", "CHGate", "CSXGate", "RZGate", "SGate", "RZZGate", "CRXGate", "CRZGate", "CU1Gate", "SXdgGate", "TGate", "ECRGate")

circuit += defns

circuit.inst(Gates.RZZGate(p_445472)( 0, 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.ECRGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RYYGate(1.977559237989846)( 1, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CRXGate(p_893583, 1, 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.CRZGate(2.2498881927557752, 1, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.RZGate(5.320621737498446, 0 ))
circuit.inst(Gates.RZGate(5.512260524440591, 0 ))
circuit.inst(Gates.CU1Gate(p_99b2af, 1, 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RZZGate(6.086884486572108)( 1, 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.RYYGate(3.3705408413231095)( 1, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.RZGate(5.190931186022931, 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RYYGate(5.167261531657622)( 0, 1 ))
circuit.inst(Gates.SGate( 1 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(0, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_445472": 6.163759533339787,
    "p_893583": 5.987304452123941,
    "p_99b2af": 1.6723037552953224
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })
