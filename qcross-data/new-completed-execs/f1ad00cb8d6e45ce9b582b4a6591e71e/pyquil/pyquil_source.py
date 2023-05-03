
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("CPhaseGate", "CU1Gate", "UGate", "SXGate", "TdgGate", "CRYGate", "CCZGate")

circuit += defns

circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.CRYGate(0.8476513988624245, 4, 0 ))
circuit.inst(Gates.CU1Gate(1.5710197357755318, 3, 2 ))
circuit.inst(Gates.TdgGate( 2 ))
circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.CCZGate( 2, 1, 3 ))
circuit.inst(Gates.UGate(0.708502006099043, 2.97765669736744, 5.6444063351584415)( 2 ))
circuit.inst(Gates.CPhaseGate(5.597667172921795, 3, 4 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CRYGate(0.3177314062860099, 4, 1 ))
circuit.inst(Gates.CU1Gate(1.9730677082046415, 4, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

