
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("ECRGate", "CUGate", "RZGate", "UGate", "C3XGate", "RXGate", "DCXGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.RXGate(6.033961191253911, 4 ))
subcircuit.inst(Gates.UGate(5.01836135520768, 5.190931186022931, 1.2128092629174942)( 5 ))
subcircuit.inst(Gates.DCXGate( 9, 6 ))
subcircuit.inst(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547, 0, 2 ))
subcircuit.inst(Gates.ECRGate( 2, 0 ))
subcircuit.inst(Gates.C3XGate( 8, 5, 6, 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(9, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(5, qr[4])
circuit += MEASURE(1, qr[5])
circuit += MEASURE(8, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(6, qr[8])
circuit += MEASURE(2, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

