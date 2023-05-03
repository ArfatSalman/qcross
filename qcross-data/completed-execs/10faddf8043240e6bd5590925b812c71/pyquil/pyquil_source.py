
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("CXGate", "CU3Gate", "HGate", "CUGate", "CCXGate", "U3Gate", "CSXGate", "ZGate")

circuit += defns

circuit.inst(Gates.CSXGate( 1, 2 ))
circuit.inst(Gates.U3Gate(5.449671872109171, 3.00254832672447, 1.991190402029831)( 1 ))
circuit.inst(Gates.CCXGate( 0, 2, 1 ))
circuit.inst(Gates.CU3Gate(3.490361155617595, 2.1967031852441936, 3.6089446638145946, 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.CUGate(5.96415316326551, 5.459163154688654, 3.541730522116933, 2.478896182682137, 1, 2 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.CXGate( 1, 0 ))

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

