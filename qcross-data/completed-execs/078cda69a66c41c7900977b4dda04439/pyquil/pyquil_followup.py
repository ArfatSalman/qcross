
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("DCXGate", "CHGate", "YGate", "SGate", "RZXGate", "RXGate", "RYYGate", "CUGate", "CZGate", "iSwapGate")

circuit += defns

circuit.inst(Gates.YGate( 3 ))
circuit.inst(Gates.CUGate(4.742596091504256, 5.602098424672528, 4.320385518485325, 3.3796506020234154, 1, 2 ))
circuit.inst(Gates.DCXGate( 1, 3 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 3 ))
circuit.inst(Gates.CHGate( 0, 3 ))
circuit.inst(Gates.YGate( 0 ))
circuit.inst(Gates.CUGate(0.4698264522024645, 5.497223780656133, 0.6973970453004443, 4.135242097973106, 2, 3 ))
circuit.inst(Gates.DCXGate( 2, 0 ))
circuit.inst(Gates.CZGate( 3, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.RZXGate(3.1312684847539773)( 3, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.iSwapGate( 2, 0 ))
circuit.inst(Gates.RXGate(2.6717356275928497, 0 ))
circuit.inst(Gates.CZGate( 2, 0 ))
circuit.inst(Gates.CHGate( 2, 1 ))
circuit.inst(Gates.RYYGate(5.131718958124352)( 1, 3 ))
circuit.inst(Gates.RYYGate(2.939587764936891)( 1, 3 ))

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

