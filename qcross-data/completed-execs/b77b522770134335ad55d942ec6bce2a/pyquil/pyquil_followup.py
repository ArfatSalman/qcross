
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 3)

p_d5d30f = circuit.declare('p_d5d30f', 'REAL')
p_483362 = circuit.declare('p_483362', 'REAL')
p_c08e15 = circuit.declare('p_c08e15', 'REAL')
p_304ede = circuit.declare('p_304ede', 'REAL')
p_3c2ca3 = circuit.declare('p_3c2ca3', 'REAL')

defns = get_custom_get_definitions("XGate", "RYYGate", "CRZGate", "ZGate", "CRXGate", "iSwapGate", "CCXGate", "ECRGate", "CHGate", "TGate", "RCCXGate", "CSXGate", "RZGate", "SGate", "SXdgGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_304ede, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(p_d5d30f, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(p_483362)( 1, 0 ))
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
circuit.inst(Gates.CRZGate(p_c08e15, 2, 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CRZGate(p_3c2ca3, 2, 1 ))

qr_a899a5 = circuit.declare("qr_a899a5", "BIT", 3)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_d5d30f": 5.987304452123941,
    "p_483362": 1.6723037552953224,
    "p_c08e15": 4.167661441102218,
    "p_304ede": 6.163759533339787,
    "p_3c2ca3": 0.05525155902669336
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

