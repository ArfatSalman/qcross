
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)

p_9a487a = circuit.declare('p_9a487a', 'REAL')
p_958665 = circuit.declare('p_958665', 'REAL')
p_15dc74 = circuit.declare('p_15dc74', 'REAL')
p_ca2ee7 = circuit.declare('p_ca2ee7', 'REAL')
p_13526e = circuit.declare('p_13526e', 'REAL')
p_13b576 = circuit.declare('p_13b576', 'REAL')
p_74b502 = circuit.declare('p_74b502', 'REAL')
p_9d695e = circuit.declare('p_9d695e', 'REAL')
p_1c2d80 = circuit.declare('p_1c2d80', 'REAL')
p_fc122e = circuit.declare('p_fc122e', 'REAL')

defns = get_custom_get_definitions("CYGate", "IGate", "RCCXGate", "CU3Gate", "RZZGate", "U2Gate", "TdgGate", "RYGate", "C4XGate", "PhaseGate", "U1Gate", "C3SXGate", "SGate")

circuit += defns

circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.C4XGate( 4, 7, 8, 0, 6 ))
circuit.inst(Gates.TdgGate( 4 ))
circuit.inst(Gates.PhaseGate(p_13b576, 5 ))
circuit.inst(Gates.C4XGate( 3, 0, 5, 8, 2 ))
circuit.inst(Gates.RYGate(p_13526e, 0 ))
circuit.inst(Gates.TdgGate( 3 ))
circuit.inst(Gates.U2Gate(p_1c2d80, p_ca2ee7)( 6 ))
circuit.inst(Gates.CU3Gate(p_9a487a, 6.100759745363555, p_958665, 0, 4 ))
circuit.inst(Gates.C3SXGate( 7, 0, 1, 8 ))
circuit.inst(Gates.RYGate(p_fc122e, 0 ))
circuit.inst(Gates.PhaseGate(p_74b502, 3 ))
circuit.inst(Gates.RZZGate(p_15dc74)( 0, 6 ))
circuit.inst(Gates.CYGate( 1, 2 ))
circuit.inst(Gates.CYGate( 4, 2 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.RCCXGate( 8, 5, 7 ))
circuit.inst(Gates.C4XGate( 0, 4, 5, 2, 6 ))
circuit.inst(Gates.U1Gate(0.1283649697684065, 8 ))
circuit.inst(Gates.U1Gate(p_9d695e, 2 ))

qr_a58c70 = circuit.declare("qr_a58c70", "BIT", 10)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_9a487a": 1.0200536425931515,
    "p_958665": 3.891803045839442,
    "p_15dc74": 5.548043373759139,
    "p_ca2ee7": 4.861997899593006,
    "p_13526e": 5.6536210846521495,
    "p_13b576": 3.583928898313607,
    "p_74b502": 0.6916556361503159,
    "p_9d695e": 5.195347791320497,
    "p_1c2d80": 5.070978145808224,
    "p_fc122e": 3.345954529034082
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

