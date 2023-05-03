
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_7a4196 = circuit.declare('p_7a4196', 'REAL')
p_6c0341 = circuit.declare('p_6c0341', 'REAL')
p_36ff61 = circuit.declare('p_36ff61', 'REAL')
p_0404e8 = circuit.declare('p_0404e8', 'REAL')
p_669081 = circuit.declare('p_669081', 'REAL')
p_92c9c5 = circuit.declare('p_92c9c5', 'REAL')
p_c06d9c = circuit.declare('p_c06d9c', 'REAL')

defns = get_custom_get_definitions("CSXGate", "CRXGate", "XGate", "SXdgGate", "RYYGate", "CRZGate", "CU1Gate", "iSwapGate", "RZZGate", "SXGate", "CHGate", "TGate", "RZGate", "ECRGate")

circuit += defns

circuit.inst(Gates.RZZGate(p_c06d9c)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_0404e8)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(p_7a4196, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_669081, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_92c9c5, 1 ))
circuit.inst(Gates.RZGate(p_6c0341, 1 ))
circuit.inst(Gates.CU1Gate(1.6723037552953224, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(p_36ff61)( 0, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_7a4196": 5.987304452123941,
    "p_6c0341": 5.512260524440591,
    "p_36ff61": 6.086884486572108,
    "p_0404e8": 1.977559237989846,
    "p_669081": 2.2498881927557752,
    "p_92c9c5": 5.320621737498446,
    "p_c06d9c": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

