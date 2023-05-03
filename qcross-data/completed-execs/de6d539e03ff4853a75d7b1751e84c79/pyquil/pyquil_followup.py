
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("SGate", "CRYGate", "CRZGate", "RZXGate", "iSwapGate", "DCXGate", "ZGate", "CYGate", "PhaseGate", "CU1Gate", "SXGate", "CSXGate", "RYGate")

circuit += defns

circuit.inst(Gates.DCXGate( 7, 1 ))
circuit.inst(Gates.CRZGate(3.5837947443419367, 7, 3 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.iSwapGate( 3, 2 ))
circuit.inst(Gates.CRYGate(4.123021946449677, 5, 1 ))
circuit.inst(Gates.CSXGate( 4, 7 ))
circuit.inst(Gates.RZXGate(4.811413391581055)( 5, 0 ))
circuit.inst(Gates.CU1Gate(3.648178050626694, 6, 4 ))
circuit.inst(Gates.RYGate(5.8216640063628375, 1 ))
circuit.inst(Gates.CU1Gate(0.7038286154091901, 7, 1 ))
circuit.inst(Gates.DCXGate( 2, 5 ))
circuit.inst(Gates.CYGate( 6, 5 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(0.18001367059010623, 1, 6 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CSXGate( 2, 6 ))
circuit.inst(Gates.PhaseGate(5.414747327887186, 1 ))
circuit.inst(Gates.CRYGate(4.001439863248854, 1, 5 ))
circuit.inst(Gates.SXGate( 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

