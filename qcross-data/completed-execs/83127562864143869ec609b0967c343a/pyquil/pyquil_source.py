
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("CU1Gate", "CPhaseGate", "PhaseGate", "HGate", "TdgGate", "ECRGate", "CHGate", "CRYGate", "U1Gate", "CSwapGate", "XGate")

circuit += defns

circuit.inst(Gates.ECRGate( 9, 2 ))
circuit.inst(Gates.TdgGate( 4 ))
circuit.inst(Gates.CU1Gate(0.7405945593267375, 9, 3 ))
circuit.inst(Gates.CRYGate(4.601077991755651, 7, 9 ))
circuit.inst(Gates.CSwapGate( 6, 0, 9 ))
circuit.inst(Gates.CPhaseGate(2.9147217589256114, 6, 2 ))
circuit.inst(Gates.PhaseGate(0.5021373390560734, 9 ))
circuit.inst(Gates.XGate( 9 ))
circuit.inst(Gates.U1Gate(4.188067174285268, 4 ))
circuit.inst(Gates.CHGate( 7, 9 ))
circuit.inst(Gates.TdgGate( 0 ))
circuit.inst(Gates.CPhaseGate(2.629684885038655, 5, 3 ))
circuit.inst(Gates.CPhaseGate(5.383276207092515, 2, 7 ))
circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.ECRGate( 8, 6 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

