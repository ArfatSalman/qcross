
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("CCXGate", "SXdgGate", "CXGate", "RZGate", "RZXGate", "ZGate", "iSwapGate", "CRZGate", "CYGate", "SdgGate", "RXXGate", "CSwapGate", "CPhaseGate", "U1Gate", "RYYGate", "CUGate", "XGate")

circuit += defns

circuit.inst(Gates.CYGate( 3, 2 ))
circuit.inst(Gates.RZXGate(4.992926923750951)( 1, 3 ))
circuit.inst(Gates.RYYGate(1.9555057510547085)( 0, 1 ))
circuit.inst(Gates.U1Gate(0.8252193008316542, 1 ))
circuit.inst(Gates.CSwapGate( 3, 1, 0 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.iSwapGate( 0, 2 ))
circuit.inst(Gates.RYYGate(3.416474043372992)( 1, 3 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.CRZGate(3.738048947778281, 2, 0 ))
circuit.inst(Gates.CXGate( 2, 1 ))
circuit.inst(Gates.RXXGate(1.2110824459718403)( 0, 1 ))
circuit.inst(Gates.CPhaseGate(0.538151089952194, 0, 1 ))
circuit.inst(Gates.CCXGate( 0, 1, 3 ))
circuit.inst(Gates.RZGate(1.2470325800417235, 3 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CUGate(0.8310820236250993, 5.196031699053289, 1.9585166986172349, 4.659181440347051, 3, 2 ))

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

