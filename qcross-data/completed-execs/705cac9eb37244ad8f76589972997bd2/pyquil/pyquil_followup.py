
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_f98f00 = circuit.declare('p_f98f00', 'REAL')
p_fa847a = circuit.declare('p_fa847a', 'REAL')
p_2ea8c6 = circuit.declare('p_2ea8c6', 'REAL')
p_40b755 = circuit.declare('p_40b755', 'REAL')
p_b0a2c5 = circuit.declare('p_b0a2c5', 'REAL')
p_2d39db = circuit.declare('p_2d39db', 'REAL')
p_6111e9 = circuit.declare('p_6111e9', 'REAL')
p_37d8a3 = circuit.declare('p_37d8a3', 'REAL')

defns = get_custom_get_definitions("SGate", "CU1Gate", "CSXGate", "CRZGate", "CRXGate", "TGate", "ECRGate", "RYYGate", "ZGate", "XGate", "CUGate", "UGate", "CHGate", "SXdgGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_f98f00, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_2d39db, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_b0a2c5, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_2ea8c6, p_fa847a, p_6111e9, 3.865496458458116, 1, 4 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 0, 2 ))
circuit.inst(Gates.CU1Gate(p_40b755, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, p_37d8a3, 1.4112277317699358)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_f98f00": 6.163759533339787,
    "p_fa847a": 4.167661441102218,
    "p_2ea8c6": 5.708725119517347,
    "p_40b755": 3.2142159669963557,
    "p_b0a2c5": 1.0296448789776642,
    "p_2d39db": 2.0099472182748075,
    "p_6111e9": 4.623446645668956,
    "p_37d8a3": 0.07157463504881167
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

