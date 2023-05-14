
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_b3b922 = circuit.declare('p_b3b922', 'REAL')
p_a1819b = circuit.declare('p_a1819b', 'REAL')
p_d7cdb5 = circuit.declare('p_d7cdb5', 'REAL')
p_b0de03 = circuit.declare('p_b0de03', 'REAL')
p_744464 = circuit.declare('p_744464', 'REAL')
p_1b382d = circuit.declare('p_1b382d', 'REAL')
p_c00892 = circuit.declare('p_c00892', 'REAL')

defns = get_custom_get_definitions("CZGate", "RZGate", "RZXGate", "CUGate", "ZGate", "CXGate", "CRZGate", "CU1Gate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.RZXGate(p_a1819b)( 10, 7 ))
subcircuit.inst(Gates.CXGate( 2, 6 ))
subcircuit.inst(Gates.CZGate( 7, 4 ))
subcircuit.inst(Gates.CU1Gate(p_744464, 1, 8 ))
subcircuit.inst(Gates.CUGate(p_c00892, p_b3b922, 5.631160518436971, p_1b382d, 0, 10 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(p_d7cdb5, 3 ))
circuit.inst(Gates.CRZGate(p_b0de03, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))

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
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_b3b922": 2.696266694818697,
    "p_a1819b": 3.427505621225153,
    "p_d7cdb5": 6.163759533339787,
    "p_b0de03": 4.2641612072511235,
    "p_744464": 4.501598818751339,
    "p_1b382d": 2.9151388486514547,
    "p_c00892": 4.229610589867865
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

