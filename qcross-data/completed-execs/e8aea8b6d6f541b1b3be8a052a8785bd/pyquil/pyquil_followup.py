
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_830596 = circuit.declare('p_830596', 'REAL')
p_e2029e = circuit.declare('p_e2029e', 'REAL')
p_fa1a24 = circuit.declare('p_fa1a24', 'REAL')
p_a95f84 = circuit.declare('p_a95f84', 'REAL')
p_b2df8c = circuit.declare('p_b2df8c', 'REAL')

defns = get_custom_get_definitions("RZXGate", "CCXGate", "CU3Gate", "RZGate", "C3SXGate", "CRZGate", "ZGate", "CUGate", "TGate", "C3XGate")

circuit += defns

circuit.inst(Gates.RZGate(p_fa1a24, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(p_a95f84, p_b2df8c, p_830596, p_e2029e, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789, 2, 5 ))
subcircuit.inst(Gates.TGate( 1 ))
subcircuit.inst(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547, 0, 3 ))
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.RZXGate(4.563562108824195)( 4, 0 ))
subcircuit.inst(Gates.C3XGate( 4, 5, 2, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_830596": 2.3864521352475245,
    "p_e2029e": 5.987304452123941,
    "p_fa1a24": 6.163759533339787,
    "p_a95f84": 0.5112149185250571,
    "p_b2df8c": 5.897054719225356
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

