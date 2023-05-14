
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("CRZGate", "U2Gate", "RCCXGate", "RZGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 6 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 5, 8 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CCXGate( 7, 0, 2 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.RCCXGate( 4, 5, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 9 ))
circuit.inst(Gates.CCXGate( 2, 4, 8 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 4 ))
circuit.inst(Gates.CSXGate( 6, 8 ))

circuit += MEASURE(9, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(8, qr[2])
circuit += MEASURE(6, qr[3])
circuit += MEASURE(10, qr[4])
circuit += MEASURE(7, qr[5])
circuit += MEASURE(5, qr[6])
circuit += MEASURE(2, qr[7])
circuit += MEASURE(3, qr[8])
circuit += MEASURE(0, qr[9])
circuit += MEASURE(4, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })
