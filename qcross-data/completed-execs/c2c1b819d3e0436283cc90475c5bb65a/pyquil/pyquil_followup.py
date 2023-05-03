
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_59c694 = circuit.declare('p_59c694', 'REAL')
p_4da120 = circuit.declare('p_4da120', 'REAL')
p_bfc32f = circuit.declare('p_bfc32f', 'REAL')
p_080b1a = circuit.declare('p_080b1a', 'REAL')
p_6db7be = circuit.declare('p_6db7be', 'REAL')
p_d86b30 = circuit.declare('p_d86b30', 'REAL')
p_fdfc00 = circuit.declare('p_fdfc00', 'REAL')
p_63b789 = circuit.declare('p_63b789', 'REAL')

defns = get_custom_get_definitions("RZZGate", "ECRGate", "SXGate", "RYYGate", "CRXGate", "SXdgGate", "iSwapGate", "TGate", "XGate", "CRZGate", "RZGate", "CHGate", "CSXGate", "CU1Gate")

circuit += defns

circuit.inst(Gates.RZZGate(p_d86b30)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_bfc32f)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(p_59c694, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_63b789, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_080b1a, 1 ))
circuit.inst(Gates.RZGate(p_fdfc00, 1 ))
circuit.inst(Gates.CU1Gate(p_4da120, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(p_6db7be)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_59c694": 5.987304452123941,
    "p_4da120": 1.6723037552953224,
    "p_bfc32f": 1.977559237989846,
    "p_080b1a": 5.320621737498446,
    "p_6db7be": 6.086884486572108,
    "p_d86b30": 6.163759533339787,
    "p_fdfc00": 5.512260524440591,
    "p_63b789": 2.2498881927557752
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

