
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("CRXGate", "ECRGate", "CRZGate", "SGate", "TGate", "XGate", "CHGate", "RZGate", "CUGate", "RYYGate", "CSXGate", "SXdgGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 0 ))
circuit.inst(Gates.SXdgGate( 3 ))
circuit.inst(Gates.CSXGate( 2, 1 ))
circuit.inst(Gates.ECRGate( 0, 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 4, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 0, 4 ))
circuit.inst(Gates.CHGate( 2, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 1, 3 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 3.865496458458116, 2, 4 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(2, qr[1])
circuit += MEASURE(3, qr[2])
circuit += MEASURE(0, qr[3])
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

