
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("U3Gate", "RYGate", "RZGate", "CXGate", "YGate", "CPhaseGate", "RC3XGate", "SXdgGate", "RXGate", "RYYGate", "U1Gate", "CU3Gate", "C3XGate", "SwapGate")

circuit += defns

circuit.inst(Gates.CPhaseGate(0.464603434869698, 3, 0 ))
circuit.inst(Gates.RC3XGate( 1, 2, 3, 0 ))
circuit.inst(Gates.CU3Gate(4.577871395666417, 2.824995733037649, 4.570764402928323, 2, 0 ))
circuit.inst(Gates.YGate( 2 ))
circuit.inst(Gates.RC3XGate( 1, 3, 0, 2 ))
circuit.inst(Gates.SwapGate( 3, 0 ))
circuit.inst(Gates.SwapGate( 0, 1 ))
circuit.inst(Gates.RYGate(4.123988453145662, 3 ))
circuit.inst(Gates.RXGate(5.977019956470354, 0 ))
circuit.inst(Gates.RYGate(5.340081963621594, 0 ))
circuit.inst(Gates.CXGate( 1, 0 ))
circuit.inst(Gates.RZGate(0.902460456423349, 2 ))
circuit.inst(Gates.U1Gate(1.191082687926663, 3 ))
circuit.inst(Gates.RYGate(2.426038592845313, 3 ))
circuit.inst(Gates.CPhaseGate(1.9801508534447856, 2, 0 ))
circuit.inst(Gates.U1Gate(0.7620531016010672, 3 ))
circuit.inst(Gates.RZGate(1.1210417983863055, 0 ))
circuit.inst(Gates.C3XGate( 3, 2, 1, 0 ))
circuit.inst(Gates.CU3Gate(3.3468514586446996, 0.09605123198475385, 1.9104022337738353, 2, 0 ))
circuit.inst(Gates.RYGate(5.21436875895587, 2 ))
circuit.inst(Gates.RYGate(1.876889866834255, 2 ))
circuit.inst(Gates.U3Gate(3.580262460733749, 2.5952409532269898, 0.3968947480833723)( 2 ))
circuit.inst(Gates.U1Gate(1.8511699871735552, 0 ))
circuit.inst(Gates.RYYGate(0.8500918394546497)( 2, 0 ))
circuit.inst(Gates.CU3Gate(1.4776100383750288, 4.796549499287292, 5.831783083594262, 3, 1 ))
circuit.inst(Gates.C3XGate( 2, 0, 3, 1 ))
circuit.inst(Gates.CU3Gate(2.6606132436968934, 0.25042616078481367, 0.47890039592537104, 3, 0 ))
circuit.inst(Gates.RXGate(5.381463645700576, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

