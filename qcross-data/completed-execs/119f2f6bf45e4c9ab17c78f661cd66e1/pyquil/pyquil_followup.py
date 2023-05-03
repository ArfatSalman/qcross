
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("ZGate", "U3Gate", "CPhaseGate", "RZGate", "RYGate", "DCXGate", "C3XGate", "RXXGate", "CZGate", "TdgGate", "CRXGate", "RZZGate", "CSwapGate", "RYYGate", "UGate", "RC3XGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.CRXGate(4.540485128061974, 2, 0 ))
circuit.inst(Gates.CSwapGate( 3, 1, 2 ))
circuit.inst(Gates.CSwapGate( 5, 1, 2 ))
circuit.inst(Gates.RYYGate(4.463823258920204)( 1, 3 ))
circuit.inst(Gates.CPhaseGate(3.371946193609531, 6, 2 ))
circuit.inst(Gates.RYYGate(3.3281963864143704)( 2, 0 ))
circuit.inst(Gates.C3SXGate( 3, 5, 1, 6 ))
circuit.inst(Gates.RYGate(4.644790991147617, 0 ))
circuit.inst(Gates.CPhaseGate(0.3126995978940275, 2, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.RYYGate(6.048921809752355)( 5, 2 ))
circuit.inst(Gates.U3Gate(3.2280333223438684, 1.6763403778979529, 1.308375256732971)( 4 ))
circuit.inst(Gates.UGate(3.300493821011834, 2.7595037431292786, 0.0456041163048407)( 1 ))
circuit.inst(Gates.CSwapGate( 2, 1, 6 ))
circuit.inst(Gates.C3XGate( 3, 6, 4, 1 ))
circuit.inst(Gates.UGate(4.005766554739231, 3.562181008920026, 1.1726853359197904)( 2 ))
circuit.inst(Gates.C3XGate( 2, 5, 1, 6 ))
circuit.inst(Gates.DCXGate( 5, 4 ))
circuit.inst(Gates.RXXGate(1.0617494142412416)( 4, 0 ))
circuit.inst(Gates.CZGate( 4, 2 ))
circuit.inst(Gates.C3XGate( 4, 5, 1, 6 ))
circuit.inst(Gates.CPhaseGate(3.64559874218163, 0, 5 ))
circuit.inst(Gates.RC3XGate( 5, 6, 1, 2 ))
circuit.inst(Gates.TdgGate( 6 ))
circuit.inst(Gates.RZGate(3.7376045176206487, 3 ))
circuit.inst(Gates.RZZGate(0.353928536272812)( 1, 5 ))

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




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

