
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("RXXGate", "CPhaseGate", "XGate", "SXdgGate", "ECRGate", "CHGate", "RZZGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.CHGate( 0, 1 ))
subcircuit.inst(Gates.SXdgGate( 0 ))
subcircuit.inst(Gates.CPhaseGate(1.7280044377928914, 0, 1 ))
subcircuit.inst(Gates.RXXGate(0.5112149185250571)( 0, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZZGate(6.163759533339787)( 0, 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.ECRGate( 0, 1 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(0, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

