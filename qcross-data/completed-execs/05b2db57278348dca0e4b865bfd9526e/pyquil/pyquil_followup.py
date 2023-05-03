
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CCXGate", "CRZGate", "CSXGate", "ZGate", "SXGate", "XGate", "RZGate", "CHGate", "TGate", "CRXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 9 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 7, 9 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 8 ))
circuit.inst(Gates.CCXGate( 4, 5, 8 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 0, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.SXGate( 6 ))
circuit.inst(Gates.CSXGate( 3, 1 ))
circuit.inst(Gates.CCXGate( 3, 5, 4 ))
circuit.inst(Gates.C3SXGate( 6, 3, 2, 5 ))
circuit.inst(Gates.CSXGate( 2, 6 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CHGate( 8, 0 ))
circuit.inst(Gates.CSXGate( 6, 2 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 0, 6 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(6, qr[2])
circuit += MEASURE(9, qr[3])
circuit += MEASURE(3, qr[4])
circuit += MEASURE(4, qr[5])
circuit += MEASURE(7, qr[6])
circuit += MEASURE(8, qr[7])
circuit += MEASURE(1, qr[8])
circuit += MEASURE(5, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

