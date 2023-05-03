
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("U2Gate", "C3XGate", "UGate", "CU1Gate", "TGate", "CRXGate", "CUGate", "CRYGate", "DCXGate", "U3Gate", "CSXGate", "C3SXGate", "SXGate", "SwapGate", "IGate", "ZGate", "XGate")

circuit += defns

circuit.inst(Gates.IGate( 3 ))
circuit.inst(Gates.XGate( 4 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.C3XGate( 4, 6, 3, 2 ))
circuit.inst(Gates.CU1Gate(3.9840757667715256, 3, 6 ))
circuit.inst(Gates.U2Gate(1.2445320670388027, 5.484541161403915)( 5 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.DCXGate( 6, 3 ))
circuit.inst(Gates.U3Gate(2.0075607189768796, 4.451648094855798, 0.9112643954181384)( 5 ))
circuit.inst(Gates.CRXGate(2.3584860491406796, 1, 6 ))
circuit.inst(Gates.CU1Gate(0.1446301149031628, 3, 1 ))
circuit.inst(Gates.CUGate(0.5186416756754034, 0.37593935376934196, 5.5900874211259195, 1.3667758390177343, 2, 3 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.UGate(5.054317038195475, 0.7695110069701433, 1.2922416810957755)( 1 ))
circuit.inst(Gates.U2Gate(0.1149636377110738, 4.386499201930481)( 2 ))
circuit.inst(Gates.U3Gate(4.785990021070069, 3.3831192493434576, 3.322394937884733)( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRYGate(0.6395924521893505, 1, 0 ))
circuit.inst(Gates.SwapGate( 0, 5 ))
circuit.inst(Gates.SwapGate( 5, 3 ))
circuit.inst(Gates.CRYGate(1.3751732052958698, 4, 5 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CSXGate( 6, 3 ))
circuit.inst(Gates.C3SXGate( 5, 2, 0, 3 ))
circuit.inst(Gates.ZGate( 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

