
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("RZGate", "ZGate", "RCCXGate", "SGate", "C3SXGate", "RZZGate", "UGate", "TGate", "CCXGate", "CU1Gate", "SXGate", "CUGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 4, 1 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 4, 0 ))
circuit.inst(Gates.C3SXGate( 2, 1, 5, 4 ))
circuit.inst(Gates.CCXGate( 2, 3, 5 ))
circuit.inst(Gates.C3SXGate( 1, 0, 3, 5 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.RCCXGate( 3, 0, 1 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 2, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 2 ))
circuit.inst(Gates.C3SXGate( 5, 4, 2, 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 0, 5 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( 3 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 5, 3 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.SXGate( 5 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 5, 3 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 2, 1 ))

circuit += MEASURE(5, qr[0])
circuit += MEASURE(2, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(0, qr[3])
circuit += MEASURE(1, qr[4])
circuit += MEASURE(3, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

