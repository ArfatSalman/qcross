
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_ce7cb6 = circuit.declare('p_ce7cb6', 'REAL')
p_97c5b0 = circuit.declare('p_97c5b0', 'REAL')
p_3124eb = circuit.declare('p_3124eb', 'REAL')

defns = get_custom_get_definitions("CRZGate", "TGate", "SXGate", "ZGate", "XGate", "RZGate", "CCXGate", "CHGate", "CRXGate", "CSXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_3124eb, 4 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CRXGate(p_ce7cb6, 1, 3 ))
circuit.inst(Gates.CCXGate( 5, 9, 3 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 2 ))
circuit.inst(Gates.RZGate(p_97c5b0, 1 ))
circuit.inst(Gates.SXGate( 6 ))
circuit.inst(Gates.CSXGate( 7, 8 ))
circuit.inst(Gates.CCXGate( 7, 9, 5 ))
circuit.inst(Gates.C3SXGate( 6, 7, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 6 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 3, 1 ))
circuit.inst(Gates.CSXGate( 6, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(6, qr[2])
circuit += MEASURE(4, qr[3])
circuit += MEASURE(7, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(2, qr[6])
circuit += MEASURE(3, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_ce7cb6": 5.987304452123941,
    "p_97c5b0": 4.229610589867865,
    "p_3124eb": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

