
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_c86bb0 = circuit.declare('p_c86bb0', 'REAL')
p_646585 = circuit.declare('p_646585', 'REAL')
p_1966c3 = circuit.declare('p_1966c3', 'REAL')

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
circuit.inst(Gates.RYYGate(1.977559237989846)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(2.2498881927557752, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_646585, 1 ))
circuit.inst(Gates.RZGate(5.512260524440591, 1 ))
circuit.inst(Gates.CU1Gate(1.6723037552953224, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(p_c86bb0)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(p_1966c3)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_c86bb0": 6.086884486572108,
    "p_646585": 5.320621737498446,
    "p_1966c3": 3.3705408413231095
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

