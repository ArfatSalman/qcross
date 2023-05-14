
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_ea6b64 = circuit.declare('p_ea6b64', 'REAL')
p_2e72b1 = circuit.declare('p_2e72b1', 'REAL')
p_ee580c = circuit.declare('p_ee580c', 'REAL')
p_6eeda0 = circuit.declare('p_6eeda0', 'REAL')
p_f65747 = circuit.declare('p_f65747', 'REAL')
p_18bd1c = circuit.declare('p_18bd1c', 'REAL')
p_ba0550 = circuit.declare('p_ba0550', 'REAL')
p_d56d65 = circuit.declare('p_d56d65', 'REAL')
p_01353d = circuit.declare('p_01353d', 'REAL')

defns = get_custom_get_definitions("CHGate", "ZGate", "CU1Gate", "UGate", "SGate", "ECRGate", "TGate", "SXdgGate", "CUGate", "XGate", "CRXGate", "RZGate", "CRZGate", "CSXGate", "RYYGate")

circuit += defns

circuit.inst(Gates.RZGate(p_ea6b64, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_18bd1c, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_f65747, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_01353d)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_ee580c, p_2e72b1, p_ba0550, 3.865496458458116, 1, 4 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 0, 2 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(p_6eeda0, 0.07157463504881167, p_d56d65)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_ea6b64": 6.163759533339787,
    "p_2e72b1": 4.167661441102218,
    "p_ee580c": 5.708725119517347,
    "p_6eeda0": 5.887184334931191,
    "p_f65747": 1.0296448789776642,
    "p_18bd1c": 2.0099472182748075,
    "p_ba0550": 4.623446645668956,
    "p_d56d65": 1.4112277317699358,
    "p_01353d": 1.6723037552953224
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        


quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

