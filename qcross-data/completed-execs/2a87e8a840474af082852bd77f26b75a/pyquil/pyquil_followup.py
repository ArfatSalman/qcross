
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_80e8e5 = circuit.declare('p_80e8e5', 'REAL')
p_d391ad = circuit.declare('p_d391ad', 'REAL')
p_58cdd0 = circuit.declare('p_58cdd0', 'REAL')
p_899200 = circuit.declare('p_899200', 'REAL')
p_ff62da = circuit.declare('p_ff62da', 'REAL')
p_5b5ed2 = circuit.declare('p_5b5ed2', 'REAL')
p_4c1552 = circuit.declare('p_4c1552', 'REAL')
p_118d87 = circuit.declare('p_118d87', 'REAL')
p_683b64 = circuit.declare('p_683b64', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "C3SXGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_683b64, 3 ))
circuit.inst(Gates.CRZGate(p_58cdd0, 6, 3 ))
circuit.inst(Gates.CRXGate(p_5b5ed2, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_d391ad, 1, 6 ))
circuit.inst(Gates.RZGate(p_4c1552, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_899200, 1, 2 ))
circuit.inst(Gates.U2Gate(p_118d87, p_ff62da)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(p_80e8e5, 1 ))

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
    "p_80e8e5": 5.014941143947427,
    "p_d391ad": 4.167661441102218,
    "p_58cdd0": 4.2641612072511235,
    "p_899200": 2.586208953975239,
    "p_ff62da": 2.1276323672732023,
    "p_5b5ed2": 5.987304452123941,
    "p_4c1552": 4.229610589867865,
    "p_118d87": 2.5163050709890156,
    "p_683b64": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

