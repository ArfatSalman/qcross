
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("CRZGate", "U2Gate", "RCCXGate", "CU1Gate", "RZGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 0 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 4, 2 ))
circuit.inst(Gates.ZGate( 10 ))
circuit.inst(Gates.CCXGate( 3, 1, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.RCCXGate( 5, 4, 9 ))
circuit.inst(Gates.RZGate(4.229610589867865, 6 ))
circuit.inst(Gates.CCXGate( 8, 5, 2 ))
circuit.inst(Gates.SdgGate( 8 ))
circuit.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 5 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.CHGate( 6, 8 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 1, 6 ))
circuit.inst(Gates.RZGate(5.0063780207098425, 4 ))

circuit += MEASURE(6, qr[0])
circuit += MEASURE(10, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(0, qr[3])
circuit += MEASURE(7, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(4, qr[6])
circuit += MEASURE(8, qr[7])
circuit += MEASURE(9, qr[8])
circuit += MEASURE(1, qr[9])
circuit += MEASURE(5, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

