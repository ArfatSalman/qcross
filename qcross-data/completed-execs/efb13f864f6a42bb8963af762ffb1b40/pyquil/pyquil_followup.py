
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("RCCXGate", "UGate", "ZGate", "CU1Gate", "RZZGate", "CRZGate", "C3SXGate", "RZGate", "TGate", "SGate", "SdgGate", "CCXGate", "SXGate", "CUGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 5, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 5, 2 ))
circuit.inst(Gates.C3SXGate( 0, 4, 3, 5 ))
circuit.inst(Gates.CCXGate( 0, 1, 3 ))
circuit.inst(Gates.C3SXGate( 4, 2, 1, 3 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 1, 2, 4 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 0, 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.C3SXGate( 3, 5, 0, 2 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 2, 3 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( 1 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 3, 1 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 3 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 3, 1 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 0, 4 ))
circuit.inst(Gates.C3SXGate( 2, 3, 4, 5 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 5, 1 ))
circuit.inst(Gates.CRXGate(2.6687018103754414, 4, 1 ))
circuit.inst(Gates.CRZGate(5.742126321682921, 5, 3 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SdgGate( 3 ))

circuit += MEASURE(3, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(2, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(1, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

