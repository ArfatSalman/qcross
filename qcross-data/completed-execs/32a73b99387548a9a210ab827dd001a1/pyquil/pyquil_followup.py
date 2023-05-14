
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_fc0ce7 = circuit.declare('p_fc0ce7', 'REAL')
p_532c13 = circuit.declare('p_532c13', 'REAL')
p_96cba0 = circuit.declare('p_96cba0', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "C3SXGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 0 ))
circuit.inst(Gates.CRZGate(p_fc0ce7, 7, 0 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 5, 9 ))
circuit.inst(Gates.CCXGate( 3, 4, 9 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 5, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 5 ))
circuit.inst(Gates.SXGate( 8 ))
circuit.inst(Gates.CSXGate( 1, 6 ))
circuit.inst(Gates.CCXGate( 1, 4, 3 ))
circuit.inst(Gates.C3SXGate( 8, 1, 2, 4 ))
circuit.inst(Gates.CSXGate( 2, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CHGate( 9, 5 ))
circuit.inst(Gates.CSXGate( 8, 2 ))
circuit.inst(Gates.CRZGate(p_96cba0, 5, 8 ))
circuit.inst(Gates.U2Gate(p_532c13, 2.1276323672732023)( 8 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 4 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.RZGate(5.014941143947427, 5 ))

qr_0b8718 = circuit.declare("qr_0b8718", "BIT", 8)

circuit += MEASURE(2, qr[0])
circuit += MEASURE(5, qr[1])
circuit += MEASURE(8, qr[2])
circuit += MEASURE(0, qr[3])
circuit += MEASURE(1, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(7, qr[6])
circuit += MEASURE(9, qr[7])
circuit += MEASURE(6, qr[8])
circuit += MEASURE(4, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_fc0ce7": 4.2641612072511235,
    "p_532c13": 2.5163050709890156,
    "p_96cba0": 2.586208953975239
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

