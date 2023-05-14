
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 5)

p_236385 = circuit.declare('p_236385', 'REAL')
p_500aa6 = circuit.declare('p_500aa6', 'REAL')
p_8f916e = circuit.declare('p_8f916e', 'REAL')
p_8aac37 = circuit.declare('p_8aac37', 'REAL')
p_9f7fb1 = circuit.declare('p_9f7fb1', 'REAL')
p_3176a0 = circuit.declare('p_3176a0', 'REAL')

defns = get_custom_get_definitions("SGate", "CUGate", "ECRGate", "CRXGate", "RYYGate", "ZGate", "CU1Gate", "CHGate", "RZGate", "XGate", "UGate", "CSXGate", "SXdgGate", "CRZGate", "TGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_3176a0, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(5.708725119517347, 4.167661441102218, p_8aac37, 3.865496458458116, 1, 4 ))
circuit.inst(Gates.RZGate(p_8f916e, 1 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 0, 2 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(p_9f7fb1, p_236385, p_500aa6)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CHGate( 0, 4 ))
circuit.inst(Gates.CHGate( 0, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_236385": 0.07157463504881167,
    "p_500aa6": 1.4112277317699358,
    "p_8f916e": 4.229610589867865,
    "p_8aac37": 4.623446645668956,
    "p_9f7fb1": 5.887184334931191,
    "p_3176a0": 2.0099472182748075
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

