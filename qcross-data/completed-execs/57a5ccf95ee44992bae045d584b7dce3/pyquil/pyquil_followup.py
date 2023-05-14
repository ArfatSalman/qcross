
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_d5e26f = circuit.declare('p_d5e26f', 'REAL')
p_90ec67 = circuit.declare('p_90ec67', 'REAL')
p_263cbf = circuit.declare('p_263cbf', 'REAL')
p_3818c9 = circuit.declare('p_3818c9', 'REAL')
p_5671c2 = circuit.declare('p_5671c2', 'REAL')
p_3be06b = circuit.declare('p_3be06b', 'REAL')
p_1d1ce1 = circuit.declare('p_1d1ce1', 'REAL')

defns = get_custom_get_definitions("RYYGate", "CRZGate", "XGate", "CU1Gate", "ZGate", "CRXGate", "UGate", "CUGate", "ECRGate", "CHGate", "TGate", "CSXGate", "RZGate", "SGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_d5e26f, 1 ))
circuit.inst(Gates.SXdgGate( 4 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.ECRGate( 1, 4 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 1 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 2 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.RYYGate(p_3818c9)( 0, 4 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CUGate(p_263cbf, 4.167661441102218, 4.623446645668956, 3.865496458458116, 3, 2 ))
circuit.inst(Gates.RZGate(4.229610589867865, 3 ))
circuit.inst(Gates.RYYGate(p_90ec67)( 0, 4 ))
circuit.inst(Gates.CU1Gate(p_1d1ce1, 1, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, p_3be06b, p_5671c2)( 2 ))
circuit.inst(Gates.CHGate( 4, 0 ))
circuit.inst(Gates.ZGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(3, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(1, qr[3])
circuit += MEASURE(2, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_d5e26f": 6.163759533339787,
    "p_90ec67": 5.398622178940033,
    "p_263cbf": 5.708725119517347,
    "p_3818c9": 1.6723037552953224,
    "p_5671c2": 1.4112277317699358,
    "p_3be06b": 0.07157463504881167,
    "p_1d1ce1": 3.2142159669963557
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

