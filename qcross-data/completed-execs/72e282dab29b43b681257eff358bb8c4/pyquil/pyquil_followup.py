
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_a3a14d = circuit.declare('p_a3a14d', 'REAL')
p_03a56d = circuit.declare('p_03a56d', 'REAL')

defns = get_custom_get_definitions("CRZGate", "RZGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_a3a14d, 6 ))
circuit.inst(Gates.CRZGate(p_03a56d, 10, 9 ))
circuit.inst(Gates.ZGate( 7 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(7, qr[1])
circuit += MEASURE(9, qr[2])
circuit += MEASURE(6, qr[3])
circuit += MEASURE(0, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(10, qr[6])
circuit += MEASURE(4, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(1, qr[9])
circuit += MEASURE(3, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_a3a14d": 6.163759533339787,
    "p_03a56d": 4.2641612072511235
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
