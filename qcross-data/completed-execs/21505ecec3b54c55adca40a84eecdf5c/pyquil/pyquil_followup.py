
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_e377c8 = circuit.declare('p_e377c8', 'REAL')
p_9593ea = circuit.declare('p_9593ea', 'REAL')
p_751f8c = circuit.declare('p_751f8c', 'REAL')
p_7227de = circuit.declare('p_7227de', 'REAL')

defns = get_custom_get_definitions("ZGate", "RZGate", "C3SXGate", "CRXGate", "RYYGate", "XGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_751f8c, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_9593ea, 0, 6 ))
circuit.inst(Gates.CRZGate(p_e377c8, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_7227de)( 6, 7 ))

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
    "p_e377c8": 1.0296448789776642,
    "p_9593ea": 5.987304452123941,
    "p_751f8c": 6.163759533339787,
    "p_7227de": 1.740253089260498
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

