
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CCXGate", "XGate", "RZGate", "CRXGate", "TGate", "U2Gate", "SXdgGate", "CHGate", "CSXGate", "ZGate", "C3SXGate", "CRZGate", "SXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 6 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 4, 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 8, 3 ))
circuit.inst(Gates.CCXGate( 0, 9, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 8, 4 ))
circuit.inst(Gates.RZGate(4.229610589867865, 8 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 5, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 0 ))
circuit.inst(Gates.C3SXGate( 2, 5, 1, 9 ))
circuit.inst(Gates.CSXGate( 1, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CHGate( 3, 8 ))
circuit.inst(Gates.CSXGate( 2, 1 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 8, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXdgGate( 9 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(8, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(6, qr[3])
circuit += MEASURE(5, qr[4])
circuit += MEASURE(0, qr[5])
circuit += MEASURE(4, qr[6])
circuit += MEASURE(3, qr[7])
circuit += MEASURE(7, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

