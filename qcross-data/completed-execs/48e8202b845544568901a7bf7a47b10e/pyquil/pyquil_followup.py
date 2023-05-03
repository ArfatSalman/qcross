
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("C3XGate", "CRXGate", "RYGate", "RXGate", "CRYGate", "DCXGate")

circuit += defns

circuit.inst(Gates.CRXGate(5.2771665030277894, 2, 5 ))
circuit.inst(Gates.RYGate(2.7769187719860096, 5 ))
circuit.inst(Gates.CRYGate(2.1848751379170706, 0, 2 ))
circuit.inst(Gates.C3XGate( 0, 1, 5, 4 ))
circuit.inst(Gates.RYGate(0.43166458716598444, 0 ))
circuit.inst(Gates.DCXGate( 1, 3 ))
circuit.inst(Gates.RXGate(4.785958015357605, 0 ))
circuit.inst(Gates.CRXGate(5.271022058006445, 3, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

