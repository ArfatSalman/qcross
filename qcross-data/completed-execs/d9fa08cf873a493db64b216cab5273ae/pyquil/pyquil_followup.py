
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_a95533 = circuit.declare('p_a95533', 'REAL')
p_ec403b = circuit.declare('p_ec403b', 'REAL')
p_4c0f0f = circuit.declare('p_4c0f0f', 'REAL')
p_6100f8 = circuit.declare('p_6100f8', 'REAL')
p_07e86a = circuit.declare('p_07e86a', 'REAL')
p_55c5f0 = circuit.declare('p_55c5f0', 'REAL')

defns = get_custom_get_definitions("SXGate", "C3SXGate", "SXdgGate", "RZGate", "ZGate", "TGate", "CHGate", "U2Gate", "XGate", "CRZGate", "CCXGate", "CRXGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_4c0f0f, 3 ))
circuit.inst(Gates.CRZGate(p_6100f8, 6, 3 ))
circuit.inst(Gates.CRXGate(p_55c5f0, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_07e86a, 1, 6 ))
circuit.inst(Gates.RZGate(p_ec403b, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_a95533, 1, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))

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
    "p_a95533": 2.586208953975239,
    "p_ec403b": 4.229610589867865,
    "p_4c0f0f": 6.163759533339787,
    "p_6100f8": 4.2641612072511235,
    "p_07e86a": 4.167661441102218,
    "p_55c5f0": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

