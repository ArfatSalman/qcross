
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("C3XGate", "CPhaseGate", "CU3Gate", "SdgGate", "CHGate", "CZGate", "SGate", "IGate", "RYYGate")

circuit += defns

circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.RYYGate(2.10593478876119)( 2, 1 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CZGate( 2, 3 ))
circuit.inst(Gates.CZGate( 0, 3 ))
circuit.inst(Gates.CZGate( 1, 2 ))
circuit.inst(Gates.CU3Gate(5.177552214723695, 3.7847055340640803, 5.596894918056728, 2, 0 ))
circuit.inst(Gates.CHGate( 2, 3 ))
circuit.inst(Gates.CPhaseGate(5.982058731459433, 2, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.C3XGate( 3, 1, 2, 0 ))

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

