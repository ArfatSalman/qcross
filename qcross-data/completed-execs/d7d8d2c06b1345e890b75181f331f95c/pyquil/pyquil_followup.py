
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("RZGate", "RYGate", "ZGate", "SdgGate", "SXdgGate", "RCCXGate", "CHGate", "CPhaseGate")

circuit += defns

circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.RZGate(0.6386974670970621, 2 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.CPhaseGate(4.103056419716538, 1, 4 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.CPhaseGate(1.57456137798405, 0, 3 ))
circuit.inst(Gates.RCCXGate( 4, 5, 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 3, 1 ))
circuit.inst(Gates.RYGate(4.436548686510933, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.SXdgGate( 0 ))

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

