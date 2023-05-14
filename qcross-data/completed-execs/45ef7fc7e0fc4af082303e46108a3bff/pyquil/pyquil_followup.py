
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_628a76 = circuit.declare('p_628a76', 'REAL')
p_7b2ce0 = circuit.declare('p_7b2ce0', 'REAL')
p_1b05b2 = circuit.declare('p_1b05b2', 'REAL')
p_cb0ae5 = circuit.declare('p_cb0ae5', 'REAL')
p_af3d09 = circuit.declare('p_af3d09', 'REAL')

defns = get_custom_get_definitions("RZGate", "CUGate", "CRXGate", "CSXGate", "RYYGate", "SXdgGate", "CHGate", "ZGate", "TGate", "CRZGate", "SGate", "XGate", "ECRGate")

circuit += defns

circuit.inst(Gates.RZGate(p_cb0ae5, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_628a76, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_af3d09, 4.167661441102218, p_7b2ce0, p_1b05b2, 1, 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_628a76": 2.0099472182748075,
    "p_7b2ce0": 4.623446645668956,
    "p_1b05b2": 3.865496458458116,
    "p_cb0ae5": 6.163759533339787,
    "p_af3d09": 5.708725119517347
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

