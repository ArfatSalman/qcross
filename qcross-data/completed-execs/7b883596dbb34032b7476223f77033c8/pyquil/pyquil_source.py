
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("ECRGate", "CSwapGate", "CPhaseGate", "PhaseGate", "SGate", "RXGate", "SXdgGate", "SwapGate")

circuit += defns

circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CSwapGate( 7, 6, 3 ))
circuit.inst(Gates.ECRGate( 3, 1 ))
circuit.inst(Gates.RXGate(4.0941649085780565, 5 ))
circuit.inst(Gates.PhaseGate(1.8301283012499292, 1 ))
circuit.inst(Gates.CPhaseGate(1.547393669354307, 2, 0 ))
circuit.inst(Gates.SXdgGate( 4 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CPhaseGate(3.6025830866934596, 7, 0 ))
circuit.inst(Gates.SwapGate( 6, 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

