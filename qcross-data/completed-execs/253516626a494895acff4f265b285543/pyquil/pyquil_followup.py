
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("TdgGate", "RXGate", "XGate", "DCXGate", "SwapGate")

circuit += defns

circuit.inst(Gates.DCXGate( 2, 0 ))
circuit.inst(Gates.RXGate(6.0811696452339525, 0 ))
circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SwapGate( 2, 0 ))
circuit.inst(Gates.RXGate(0.6094072051955249, 2 ))
circuit.inst(Gates.TdgGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

