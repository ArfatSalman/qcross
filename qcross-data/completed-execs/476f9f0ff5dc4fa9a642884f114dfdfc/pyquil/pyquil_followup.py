
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("HGate", "SdgGate", "RYYGate", "RC3XGate", "U3Gate", "RCCXGate", "CRZGate", "DCXGate", "U2Gate")

circuit += defns

circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.U3Gate(0.2435863694263356, 4.952605016068409, 1.0462631235631594)( 0 ))
circuit.inst(Gates.CRZGate(3.8430137210716477, 0, 3 ))
circuit.inst(Gates.RCCXGate( 1, 2, 0 ))
circuit.inst(Gates.RYYGate(1.9038331447854693)( 0, 3 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.RC3XGate( 0, 2, 3, 1 ))
circuit.inst(Gates.DCXGate( 3, 0 ))
circuit.inst(Gates.U2Gate(2.315671616264609, 3.642280082030703)( 1 ))
circuit.inst(Gates.DCXGate( 1, 3 ))

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

