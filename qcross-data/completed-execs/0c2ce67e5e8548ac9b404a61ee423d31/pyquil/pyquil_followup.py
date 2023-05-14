
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_8a56c7 = circuit.declare('p_8a56c7', 'REAL')
p_12f990 = circuit.declare('p_12f990', 'REAL')
p_474773 = circuit.declare('p_474773', 'REAL')

defns = get_custom_get_definitions("CRZGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_8a56c7, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 3 ))
circuit.inst(Gates.CRXGate(p_12f990, 5, 1 ))
circuit.inst(Gates.CCXGate( 7, 8, 1 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.XGate( 9 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 5, 2 ))
circuit.inst(Gates.RZGate(p_474773, 5 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.CSXGate( 6, 9 ))
circuit.inst(Gates.CCXGate( 6, 8, 7 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(5, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(6, qr[4])
circuit += MEASURE(7, qr[5])
circuit += MEASURE(2, qr[6])
circuit += MEASURE(1, qr[7])
circuit += MEASURE(9, qr[8])
circuit += MEASURE(8, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_8a56c7": 6.163759533339787,
    "p_12f990": 5.987304452123941,
    "p_474773": 4.229610589867865
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

