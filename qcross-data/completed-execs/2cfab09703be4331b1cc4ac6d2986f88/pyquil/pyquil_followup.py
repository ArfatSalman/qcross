
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("RZGate", "ZGate", "SXdgGate", "ECRGate", "CSXGate", "C3SXGate", "CHGate", "UGate", "CRZGate", "CRXGate", "SXGate", "U2Gate", "CCXGate", "XGate", "TGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 9, 2 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 6, 0 ))
circuit.inst(Gates.CCXGate( 7, 3, 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 6, 9 ))
circuit.inst(Gates.RZGate(4.229610589867865, 6 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CSXGate( 8, 5 ))
circuit.inst(Gates.CCXGate( 8, 3, 7 ))
circuit.inst(Gates.C3SXGate( 1, 8, 4, 3 ))
circuit.inst(Gates.CSXGate( 4, 1 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CHGate( 0, 6 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 6, 1 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 1 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.SXdgGate( 3 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RZGate(5.014941143947427, 6 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 0, 6 ))
circuit.inst(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( 1 ))
circuit.inst(Gates.ECRGate( 8, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CSXGate( 6, 0 ))

circuit += MEASURE(4, qr[0])
circuit += MEASURE(6, qr[1])
circuit += MEASURE(1, qr[2])
circuit += MEASURE(2, qr[3])
circuit += MEASURE(8, qr[4])
circuit += MEASURE(7, qr[5])
circuit += MEASURE(9, qr[6])
circuit += MEASURE(0, qr[7])
circuit += MEASURE(5, qr[8])
circuit += MEASURE(3, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

