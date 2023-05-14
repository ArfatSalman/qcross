
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("SXdgGate", "XGate", "RZGate", "CSXGate", "SGate", "ZGate", "RCCXGate", "CHGate", "CRXGate", "RYYGate", "UGate", "ECRGate", "TGate", "CU1Gate", "CUGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 4, 2 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 3, 4 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 4, 3 ))
circuit.inst(Gates.CHGate( 1, 3 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.CSXGate( 1, 3 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 3.865496458458116, 1, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 0, 2 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( 3 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CHGate( 0, 3 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 0, 4 ))
circuit.inst(Gates.RCCXGate( 0, 4, 1 ))
circuit.inst(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305, 3, 4 ))
circuit.inst(Gates.CRZGate(3.839241945509346, 2, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(4, qr[3])
circuit += MEASURE(3, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })
