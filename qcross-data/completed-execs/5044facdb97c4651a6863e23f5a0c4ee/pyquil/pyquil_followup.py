
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_8dcae8 = circuit.declare('p_8dcae8', 'REAL')
p_aa831e = circuit.declare('p_aa831e', 'REAL')
p_84ca0c = circuit.declare('p_84ca0c', 'REAL')

defns = get_custom_get_definitions("U2Gate", "CSXGate", "CRXGate", "CRZGate", "XGate", "SXdgGate", "ZGate", "SXGate", "CHGate", "TGate", "RZGate", "C3SXGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(p_8dcae8, 6, 3 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_84ca0c, 1, 2 ))
circuit.inst(Gates.U2Gate(p_aa831e, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(5.014941143947427, 1 ))

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
    "p_8dcae8": 4.2641612072511235,
    "p_aa831e": 2.5163050709890156,
    "p_84ca0c": 2.586208953975239
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

