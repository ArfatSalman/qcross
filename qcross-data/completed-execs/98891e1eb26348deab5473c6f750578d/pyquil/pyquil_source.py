
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("HGate", "UGate", "CRYGate", "RC3XGate", "C3XGate", "CU3Gate", "RZZGate", "PhaseGate", "SwapGate", "U1Gate", "CRZGate")

circuit += defns

circuit.inst(Gates.CRYGate(1.075739919522674, 8, 2 ))
circuit.inst(Gates.RC3XGate( 6, 2, 5, 3 ))
circuit.inst(Gates.CRZGate(1.6326010370730453, 1, 8 ))
circuit.inst(Gates.CRZGate(6.113712295160513, 0, 1 ))
circuit.inst(Gates.UGate(1.4807775550519449, 4.708394834982332, 5.108906631758365)( 6 ))
circuit.inst(Gates.CU3Gate(1.445874138242965, 0.4812746367052968, 1.4437703311652539, 2, 6 ))
circuit.inst(Gates.U1Gate(1.55032177844381, 2 ))
circuit.inst(Gates.RZZGate(0.023161113352440612)( 2, 6 ))
circuit.inst(Gates.C3XGate( 5, 2, 3, 8 ))
circuit.inst(Gates.C3XGate( 3, 8, 0, 1 ))
circuit.inst(Gates.U1Gate(5.302777250135231, 3 ))
circuit.inst(Gates.UGate(1.7927964637983416, 0.8353911218777099, 1.5856512163121241)( 1 ))
circuit.inst(Gates.CU3Gate(4.746133300531744, 4.497432396200483, 4.25035932691423, 8, 5 ))
circuit.inst(Gates.PhaseGate(4.466750388800541, 8 ))
circuit.inst(Gates.HGate( 7 ))
circuit.inst(Gates.SwapGate( 5, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

