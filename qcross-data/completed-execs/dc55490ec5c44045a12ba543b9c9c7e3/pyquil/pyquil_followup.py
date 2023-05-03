
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("RZGate", "CSXGate", "RZXGate", "ECRGate", "CRZGate", "CU3Gate", "SwapGate", "CYGate")

circuit += defns

circuit.inst(Gates.ECRGate( 0, 1 ))
circuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.CU3Gate(0.19530688895228782, 1.7508214741181105, 0.6509821962978967, 1, 0 ))
circuit.inst(Gates.RZGate(0.07613141147187574, 0 ))
circuit.inst(Gates.CYGate( 0, 1 ))
circuit.inst(Gates.RZXGate(2.3441041272871757)( 1, 0 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.CRZGate(0.11523003750909885, 0, 1 ))
circuit.inst(Gates.CYGate( 0, 1 ))

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

