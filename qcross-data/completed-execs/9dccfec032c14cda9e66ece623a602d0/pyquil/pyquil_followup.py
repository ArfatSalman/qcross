
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("CPhaseGate", "CXGate", "CSXGate", "CRXGate", "DCXGate", "SXdgGate", "RZGate", "ECRGate", "ZGate", "RXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.DCXGate( 1, 4 ))
subcircuit.inst(Gates.CPhaseGate(1.6161683469432118, 1, 4 ))
subcircuit.inst(Gates.RXGate(6.033961191253911, 1 ))
subcircuit.inst(Gates.ZGate( 0 ))
subcircuit.inst(Gates.CXGate( 2, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 4, 3 ))

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

