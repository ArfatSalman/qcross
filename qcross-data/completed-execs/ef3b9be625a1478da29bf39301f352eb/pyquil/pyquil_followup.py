
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_86f185 = circuit.declare('p_86f185', 'REAL')
p_6b43a3 = circuit.declare('p_6b43a3', 'REAL')
p_7d2faf = circuit.declare('p_7d2faf', 'REAL')
p_85477f = circuit.declare('p_85477f', 'REAL')
p_f407a3 = circuit.declare('p_f407a3', 'REAL')
p_eb055e = circuit.declare('p_eb055e', 'REAL')
p_e75067 = circuit.declare('p_e75067', 'REAL')
p_93dcc8 = circuit.declare('p_93dcc8', 'REAL')
p_0d2e3c = circuit.declare('p_0d2e3c', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "TGate", "ZGate", "RYYGate", "RZGate", "XGate", "SGate", "CUGate", "ECRGate", "CHGate", "CRXGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_86f185, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_7d2faf, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_0d2e3c, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_85477f)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_f407a3, p_e75067, p_93dcc8, p_eb055e, 1, 4 ))
circuit.inst(Gates.RZGate(p_6b43a3, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_86f185": 6.163759533339787,
    "p_6b43a3": 4.229610589867865,
    "p_7d2faf": 2.0099472182748075,
    "p_85477f": 1.6723037552953224,
    "p_f407a3": 5.708725119517347,
    "p_eb055e": 3.865496458458116,
    "p_e75067": 4.167661441102218,
    "p_93dcc8": 4.623446645668956,
    "p_0d2e3c": 1.0296448789776642
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

