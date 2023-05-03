
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("CU1Gate", "RXXGate", "CRYGate", "CSXGate", "ECRGate", "CRZGate", "SwapGate")

circuit += defns

circuit.inst(Gates.CRZGate(1.3789403400889426, 1, 0 ))
circuit.inst(Gates.ECRGate( 0, 1 ))
circuit.inst(Gates.CRYGate(0.793394619995631, 1, 0 ))
circuit.inst(Gates.CRYGate(1.751652383527618, 0, 1 ))
circuit.inst(Gates.RXXGate(0.19609305461275878)( 1, 0 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.CRZGate(0.4924711250283179, 0, 1 ))
circuit.inst(Gates.ECRGate( 0, 1 ))
circuit.inst(Gates.CU1Gate(4.448608931258779, 1, 0 ))
circuit.inst(Gates.ECRGate( 1, 0 ))

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

