
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_c22ee3 = circuit.declare('p_c22ee3', 'REAL')
p_1477d5 = circuit.declare('p_1477d5', 'REAL')
p_dd3917 = circuit.declare('p_dd3917', 'REAL')
p_d41fd7 = circuit.declare('p_d41fd7', 'REAL')
p_ef9572 = circuit.declare('p_ef9572', 'REAL')
p_1fb36c = circuit.declare('p_1fb36c', 'REAL')
p_42a4f3 = circuit.declare('p_42a4f3', 'REAL')

defns = get_custom_get_definitions("XGate", "CRZGate", "CU1Gate", "ZGate", "CRXGate", "ECRGate", "CHGate", "RCCXGate", "CSXGate", "RZGate", "C3SXGate", "SGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_1477d5, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(p_42a4f3, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_c22ee3, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_ef9572, 4, 0 ))
circuit.inst(Gates.CRXGate(p_d41fd7, 4, 6 ))
circuit.inst(Gates.CHGate( 4, 0 ))
circuit.inst(Gates.C3SXGate( 2, 0, 3, 4 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CRZGate(p_dd3917, 0, 6 ))
circuit.inst(Gates.CU1Gate(p_1fb36c, 1, 4 ))

qr_bf1373 = circuit.declare("qr_bf1373", "BIT", 1)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_c22ee3": 4.229610589867865,
    "p_1477d5": 6.163759533339787,
    "p_dd3917": 4.833923139882297,
    "p_d41fd7": 5.94477504571567,
    "p_ef9572": 3.2142159669963557,
    "p_1fb36c": 4.028174522740928,
    "p_42a4f3": 2.0099472182748075
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

