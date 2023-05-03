
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("ZGate", "HGate", "CRXGate", "PhaseGate", "U2Gate", "TdgGate", "DCXGate", "CYGate")

circuit += defns

circuit.inst(Gates.CRXGate(3.789039586142132, 0, 1 ))
circuit.inst(Gates.PhaseGate(2.3969015822468824, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.PhaseGate(2.7534454125103585, 1 ))
circuit.inst(Gates.PhaseGate(4.877116605613038, 0 ))
circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.PhaseGate(5.974310031718985, 1 ))
circuit.inst(Gates.U2Gate(3.2332547554497055, 2.6884001068559122)( 0 ))
circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.DCXGate( 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

