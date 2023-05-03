
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("CZGate", "CYGate", "CU3Gate", "YGate", "ECRGate", "UGate", "CSdgGate", "DCXGate", "CRXGate", "RGate", "CHGate", "CXGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.UGate(4.403788193532198, 5.238005217278175, 2.414376925356305)( 1 ))
circuit.inst(Gates.RGate(3.9800961208659213, 2.54258238968427)( 0 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CXGate( 1, 0 ))
circuit.inst(Gates.CRXGate(3.0761375449158193, 1, 0 ))
circuit.inst(Gates.CSdgGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.CU3Gate(3.359364374345002, 4.018048446348199, 2.251031643786726, 0, 1 ))
circuit.inst(Gates.CZGate( 1, 0 ))
circuit.inst(Gates.RGate(4.3040860238694725, 4.7611258330830655)( 1 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.UGate(3.820196974130503, 1.381440535002157, 5.6467633400840755)( 1 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.ECRGate( 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

