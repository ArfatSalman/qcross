
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_7ebac6 = circuit.declare('p_7ebac6', 'REAL')
p_02fa5f = circuit.declare('p_02fa5f', 'REAL')
p_68bc2a = circuit.declare('p_68bc2a', 'REAL')
p_b1a917 = circuit.declare('p_b1a917', 'REAL')
p_d2b847 = circuit.declare('p_d2b847', 'REAL')
p_98866e = circuit.declare('p_98866e', 'REAL')
p_896a7d = circuit.declare('p_896a7d', 'REAL')
p_583e59 = circuit.declare('p_583e59', 'REAL')
p_eef840 = circuit.declare('p_eef840', 'REAL')

defns = get_custom_get_definitions("CRZGate", "TGate", "RCCXGate", "ZGate", "CCXGate", "CUGate", "C3SXGate", "RZGate", "RZXGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.RZGate(p_896a7d, 2 ))
subcircuit.inst(Gates.TGate( 1 ))
subcircuit.inst(Gates.CUGate(p_98866e, p_d2b847, 5.631160518436971, p_02fa5f, 0, 3 ))
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.RZXGate(p_583e59)( 4, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_eef840, 2, 4 ))
circuit.inst(Gates.CUGate(p_68bc2a, p_b1a917, p_7ebac6, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))

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
    "p_7ebac6": 2.3864521352475245,
    "p_02fa5f": 2.9151388486514547,
    "p_68bc2a": 0.5112149185250571,
    "p_b1a917": 5.897054719225356,
    "p_d2b847": 2.696266694818697,
    "p_98866e": 4.229610589867865,
    "p_896a7d": 3.672121211148789,
    "p_583e59": 4.563562108824195,
    "p_eef840": 4.2641612072511235
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

