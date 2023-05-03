
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("CRZGate", "TGate", "CU1Gate", "CHGate", "ZGate", "RCCXGate", "RZZGate", "SXdgGate", "U2Gate", "CSXGate", "CCXGate", "UGate", "XGate", "RZGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 10 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 1 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CCXGate( 0, 7, 4 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 4 ))
circuit.inst(Gates.RCCXGate( 9, 6, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 2 ))
circuit.inst(Gates.CCXGate( 4, 9, 1 ))
circuit.inst(Gates.SdgGate( 4 ))
circuit.inst(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( 9 ))
circuit.inst(Gates.CSXGate( 10, 1 ))
circuit.inst(Gates.CHGate( 2, 4 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 7, 2 ))
circuit.inst(Gates.RZGate(5.0063780207098425, 6 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 1 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 8, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RZGate(4.722103101046168, 1 ))
circuit.inst(Gates.CRZGate(0.6393443962862078, 0, 10 ))
circuit.inst(Gates.CU1Gate(2.5476776328466872, 10, 3 ))
circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.RZGate(3.6614081973587154, 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CSXGate( 4, 2 ))
circuit.inst(Gates.CU1Gate(3.631024984774394, 9, 4 ))
circuit.inst(Gates.UGate(3.4183332103477166, 1.1450785027645094, 1.308491043619365)( 6 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(5, qr[1])
circuit += MEASURE(1, qr[2])
circuit += MEASURE(10, qr[3])
circuit += MEASURE(8, qr[4])
circuit += MEASURE(0, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(4, qr[7])
circuit += MEASURE(3, qr[8])
circuit += MEASURE(7, qr[9])
circuit += MEASURE(9, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

