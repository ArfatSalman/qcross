
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("ZGate", "CHGate", "CU1Gate", "RCCXGate", "SGate", "C3SXGate", "ECRGate", "TGate", "XGate", "U2Gate", "CRXGate", "RZGate", "CRZGate", "CSXGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 5, 4 ))
circuit.inst(Gates.C3SXGate( 1, 0, 3, 5 ))
circuit.inst(Gates.CHGate( 2, 1 ))
circuit.inst(Gates.C3SXGate( 0, 5, 3, 4 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.ECRGate( 1, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.RCCXGate( 5, 4, 0 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 3 ))
circuit.inst(Gates.C3SXGate( 0, 5, 3, 6 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 2, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 2, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.C3SXGate( 5, 0, 6, 2 ))
circuit.inst(Gates.CSXGate( 0, 5 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 1 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 3, 2 ))
circuit.inst(Gates.C3SXGate( 5, 0, 4, 2 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 1, 5 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 5 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SdgGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(3, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(6, qr[3])
circuit += MEASURE(2, qr[4])
circuit += MEASURE(4, qr[5])
circuit += MEASURE(1, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

