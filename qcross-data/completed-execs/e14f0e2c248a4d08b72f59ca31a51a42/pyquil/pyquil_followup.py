
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_51dc20 = circuit.declare('p_51dc20', 'REAL')
p_f1ce6e = circuit.declare('p_f1ce6e', 'REAL')
p_f92e4f = circuit.declare('p_f92e4f', 'REAL')

defns = get_custom_get_definitions("TGate", "CRXGate", "CCXGate", "ZGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_f1ce6e, 3 ))
circuit.inst(Gates.CRZGate(p_51dc20, 6, 3 ))
circuit.inst(Gates.CRXGate(p_f92e4f, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_51dc20": 4.2641612072511235,
    "p_f1ce6e": 6.163759533339787,
    "p_f92e4f": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

