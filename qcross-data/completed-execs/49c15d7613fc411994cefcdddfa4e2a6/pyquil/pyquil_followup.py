
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_bf86c5 = circuit.declare('p_bf86c5', 'REAL')
p_12cca6 = circuit.declare('p_12cca6', 'REAL')
p_7c142a = circuit.declare('p_7c142a', 'REAL')
p_a3bcf5 = circuit.declare('p_a3bcf5', 'REAL')
p_451cf1 = circuit.declare('p_451cf1', 'REAL')

defns = get_custom_get_definitions("CCXGate", "RZGate", "CRZGate", "ZGate", "CRXGate", "XGate", "TGate")

circuit += defns

circuit.inst(Gates.RZGate(p_bf86c5, 3 ))
circuit.inst(Gates.CRZGate(p_7c142a, 6, 3 ))
circuit.inst(Gates.CRXGate(p_12cca6, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_a3bcf5, 1, 6 ))
circuit.inst(Gates.RZGate(p_451cf1, 1 ))

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
    "p_bf86c5": 6.163759533339787,
    "p_12cca6": 5.987304452123941,
    "p_7c142a": 4.2641612072511235,
    "p_a3bcf5": 4.167661441102218,
    "p_451cf1": 4.229610589867865
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

