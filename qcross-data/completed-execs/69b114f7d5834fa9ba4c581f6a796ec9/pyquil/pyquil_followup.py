
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_de371c = circuit.declare('p_de371c', 'REAL')
p_8a7444 = circuit.declare('p_8a7444', 'REAL')
p_4eefbf = circuit.declare('p_4eefbf', 'REAL')
p_4a7cc5 = circuit.declare('p_4a7cc5', 'REAL')
p_2f75fa = circuit.declare('p_2f75fa', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXGate", "RYYGate", "RZZGate", "CRXGate", "XGate", "C3SXGate", "CSXGate", "RZGate", "ZGate", "CU1Gate")

circuit += defns

circuit.inst(Gates.RZGate(p_de371c, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_4a7cc5, 1, 7 ))
circuit.inst(Gates.RZGate(p_2f75fa, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(p_8a7444, 6, 4 ))
circuit.inst(Gates.RZZGate(p_4eefbf)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_de371c": 6.163759533339787,
    "p_8a7444": 5.94477504571567,
    "p_4eefbf": 5.1829934776392745,
    "p_4a7cc5": 4.167661441102218,
    "p_2f75fa": 4.229610589867865
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

