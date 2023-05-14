
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_4534a2 = circuit.declare('p_4534a2', 'REAL')
p_c28457 = circuit.declare('p_c28457', 'REAL')
p_88080a = circuit.declare('p_88080a', 'REAL')
p_089fca = circuit.declare('p_089fca', 'REAL')
p_0aa97a = circuit.declare('p_0aa97a', 'REAL')
p_f1630e = circuit.declare('p_f1630e', 'REAL')
p_a25c71 = circuit.declare('p_a25c71', 'REAL')
p_63f494 = circuit.declare('p_63f494', 'REAL')
p_4537df = circuit.declare('p_4537df', 'REAL')
p_cab727 = circuit.declare('p_cab727', 'REAL')

defns = get_custom_get_definitions("DCXGate", "RZXGate", "ECRGate", "RZGate", "UGate", "CRZGate", "ZGate", "CUGate", "C3XGate")

circuit += defns

circuit.inst(Gates.RZGate(p_88080a, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.RZXGate(p_cab727)( 0, 6 ))
subcircuit.inst(Gates.UGate(p_4534a2, p_0aa97a, p_c28457)( 5 ))
subcircuit.inst(Gates.ZGate( 2 ))
subcircuit.inst(Gates.UGate(p_63f494, 5.190931186022931, p_4537df)( 4 ))
subcircuit.inst(Gates.DCXGate( 1, 8 ))
subcircuit.inst(Gates.CUGate(p_f1630e, p_a25c71, 5.631160518436971, 2.9151388486514547, 0, 9 ))
subcircuit.inst(Gates.ECRGate( 9, 0 ))
subcircuit.inst(Gates.C3XGate( 6, 4, 8, 9 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))

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
    "p_4534a2": 2.6397681660693015,
    "p_c28457": 3.427505621225153,
    "p_88080a": 6.163759533339787,
    "p_089fca": 5.94477504571567,
    "p_0aa97a": 5.320621737498446,
    "p_f1630e": 4.229610589867865,
    "p_a25c71": 2.696266694818697,
    "p_63f494": 5.01836135520768,
    "p_4537df": 1.2128092629174942,
    "p_cab727": 0.6833824466861163
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

