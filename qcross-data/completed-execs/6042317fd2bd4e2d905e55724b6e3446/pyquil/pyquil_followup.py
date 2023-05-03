
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_ba5a58 = circuit.declare('p_ba5a58', 'REAL')
p_a56cab = circuit.declare('p_a56cab', 'REAL')
p_1e801f = circuit.declare('p_1e801f', 'REAL')

defns = get_custom_get_definitions("CCXGate", "CRZGate", "ZGate", "SXGate", "XGate", "RZGate", "TGate", "CRXGate", "CU3Gate")

circuit += defns

circuit.inst(Gates.RZGate(p_ba5a58, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.CU3Gate(p_a56cab, 0.9356897707598831, p_1e801f, 4, 7 ))
subcircuit.inst(Gates.XGate( 9 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))

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
    "p_ba5a58": 6.163759533339787,
    "p_a56cab": 2.8392254891488653,
    "p_1e801f": 3.855749700561927
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

