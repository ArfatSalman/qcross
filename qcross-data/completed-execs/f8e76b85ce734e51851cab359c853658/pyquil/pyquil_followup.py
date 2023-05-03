
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 3)

p_cee3c3 = circuit.declare('p_cee3c3', 'REAL')
p_cfb5e0 = circuit.declare('p_cfb5e0', 'REAL')
p_749cd6 = circuit.declare('p_749cd6', 'REAL')
p_938ba1 = circuit.declare('p_938ba1', 'REAL')
p_84a600 = circuit.declare('p_84a600', 'REAL')
p_804a66 = circuit.declare('p_804a66', 'REAL')
p_6e1f78 = circuit.declare('p_6e1f78', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "ZGate", "CRZGate", "iSwapGate", "SXdgGate", "RZGate", "CSXGate", "XGate", "CHGate", "SGate", "SdgGate", "CCXGate", "RYYGate", "TGate", "ECRGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_cfb5e0, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(p_84a600, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(p_cee3c3)( 1, 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.ECRGate( 2, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RCCXGate( 1, 0, 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RCCXGate( 0, 2, 1 ))
circuit.inst(Gates.CRZGate(p_804a66, 2, 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CRZGate(p_6e1f78, 2, 1 ))
circuit.inst(Gates.RYYGate(p_749cd6)( 1, 2 ))
circuit.inst(Gates.RYYGate(p_938ba1)( 0, 2 ))

qr_102ba4 = circuit.declare("qr_102ba4", "BIT", 3)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_cee3c3": 1.6723037552953224,
    "p_cfb5e0": 6.163759533339787,
    "p_749cd6": 3.2287759437031154,
    "p_938ba1": 5.398622178940033,
    "p_84a600": 5.987304452123941,
    "p_804a66": 4.167661441102218,
    "p_6e1f78": 0.05525155902669336
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

