
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("CSdgGate", "IGate", "RC3XGate", "SdgGate", "RZXGate", "C3XGate", "DCXGate", "C3SXGate", "RYYGate", "CUGate", "CU3Gate", "CYGate", "UGate")

circuit += defns

circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.CYGate( 0, 3 ))
circuit.inst(Gates.RC3XGate( 3, 0, 2, 1 ))
circuit.inst(Gates.CUGate(0.9157606983245934, 5.397500370041537, 3.7108393874093117, 3.651689382779405, 1, 2 ))
circuit.inst(Gates.C3SXGate( 2, 0, 1, 3 ))
circuit.inst(Gates.CSdgGate( 1, 3 ))
circuit.inst(Gates.DCXGate( 3, 0 ))
circuit.inst(Gates.RZXGate(1.7115424816079432)( 0, 3 ))
circuit.inst(Gates.RZXGate(1.6486589761943145)( 2, 0 ))
circuit.inst(Gates.C3XGate( 0, 2, 3, 1 ))
circuit.inst(Gates.RYYGate(4.794877298046951)( 0, 1 ))
circuit.inst(Gates.RZXGate(3.4346411253220106)( 3, 1 ))
circuit.inst(Gates.RYYGate(6.102373854375312)( 3, 2 ))
circuit.inst(Gates.CU3Gate(2.6976815284019784, 0.9310317943034069, 1.8906179385735775, 3, 0 ))
circuit.inst(Gates.IGate( 0 ))
circuit.inst(Gates.UGate(5.176714778665683, 0.30607591346008556, 0.8506581770011129)( 3 ))
circuit.inst(Gates.C3XGate( 2, 1, 3, 0 ))
circuit.inst(Gates.UGate(2.478741058575176, 4.422282188870415, 4.889199801305671)( 1 ))

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

