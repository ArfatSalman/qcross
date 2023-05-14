
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_f22bb0 = circuit.declare('p_f22bb0', 'REAL')
p_c746bf = circuit.declare('p_c746bf', 'REAL')
p_bd1c3c = circuit.declare('p_bd1c3c', 'REAL')
p_2c205c = circuit.declare('p_2c205c', 'REAL')
p_132f3b = circuit.declare('p_132f3b', 'REAL')
p_72ab38 = circuit.declare('p_72ab38', 'REAL')
p_d5c708 = circuit.declare('p_d5c708', 'REAL')

defns = get_custom_get_definitions("C3SXGate", "CCXGate", "ZGate", "CHGate", "SXdgGate", "RZGate", "SXGate", "TGate", "CRZGate", "CSXGate", "U2Gate", "XGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_72ab38, 5 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 0, 5 ))
circuit.inst(Gates.CRXGate(p_d5c708, 9, 3 ))
circuit.inst(Gates.CCXGate( 6, 4, 3 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CRZGate(p_f22bb0, 9, 0 ))
circuit.inst(Gates.RZGate(p_132f3b, 9 ))
circuit.inst(Gates.SXGate( 8 ))
circuit.inst(Gates.CSXGate( 7, 2 ))
circuit.inst(Gates.CCXGate( 7, 4, 6 ))
circuit.inst(Gates.C3SXGate( 8, 7, 1, 4 ))
circuit.inst(Gates.CSXGate( 1, 8 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CHGate( 3, 9 ))
circuit.inst(Gates.CSXGate( 8, 1 ))
circuit.inst(Gates.CRZGate(p_bd1c3c, 9, 8 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, p_2c205c)( 8 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXdgGate( 4 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.RZGate(p_c746bf, 9 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(9, qr[1])
circuit += MEASURE(8, qr[2])
circuit += MEASURE(5, qr[3])
circuit += MEASURE(7, qr[4])
circuit += MEASURE(6, qr[5])
circuit += MEASURE(0, qr[6])
circuit += MEASURE(3, qr[7])
circuit += MEASURE(2, qr[8])
circuit += MEASURE(4, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_f22bb0": 4.167661441102218,
    "p_c746bf": 5.014941143947427,
    "p_bd1c3c": 2.586208953975239,
    "p_2c205c": 2.1276323672732023,
    "p_132f3b": 4.229610589867865,
    "p_72ab38": 6.163759533339787,
    "p_d5c708": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

