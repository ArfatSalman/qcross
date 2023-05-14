
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("ZGate", "CHGate", "CU1Gate", "RCCXGate", "SGate", "SXGate", "C3SXGate", "CUGate", "TGate", "CCXGate", "XGate", "U2Gate", "CRXGate", "RZGate", "iSwapGate", "CRZGate", "CSXGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 6 ))
circuit.inst(Gates.CSXGate( 4, 5 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 3, 1 ))
circuit.inst(Gates.SdgGate( 8 ))
circuit.inst(Gates.C3SXGate( 3, 6, 2, 7 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.SGate( 6 ))
circuit.inst(Gates.C3SXGate( 8, 0, 4, 3 ))
circuit.inst(Gates.SXGate( 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 6, 0 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 7, 6 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CSXGate( 3, 4 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CHGate( 1, 8 ))
circuit.inst(Gates.CSXGate( 0, 3 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 8, 4 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 4 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.CCXGate( 3, 1, 8 ))
circuit.inst(Gates.RCCXGate( 5, 3, 8 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.RZGate(5.014941143947427, 8 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 8, 6 ))
circuit.inst(Gates.iSwapGate( 4, 1 ))
circuit.inst(Gates.CU1Gate(1.2497571638956968, 4, 7 ))
circuit.inst(Gates.RZGate(2.862865991712737, 7 ))

circuit += MEASURE(3, qr[0])
circuit += MEASURE(8, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(0, qr[3])
circuit += MEASURE(5, qr[4])
circuit += MEASURE(7, qr[5])
circuit += MEASURE(1, qr[6])
circuit += MEASURE(2, qr[7])
circuit += MEASURE(6, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

