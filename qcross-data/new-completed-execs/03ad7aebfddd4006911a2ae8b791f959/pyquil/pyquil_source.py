
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("CYGate", "IGate", "RCCXGate", "CU3Gate", "RZZGate", "U2Gate", "TdgGate", "RYGate", "C4XGate", "PhaseGate", "U1Gate", "C3SXGate", "SGate")

circuit += defns

circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.C4XGate( 4, 7, 8, 0, 6 ))
circuit.inst(Gates.TdgGate( 4 ))
circuit.inst(Gates.PhaseGate(3.583928898313607, 5 ))
circuit.inst(Gates.C4XGate( 3, 0, 5, 8, 2 ))
circuit.inst(Gates.RYGate(5.6536210846521495, 0 ))
circuit.inst(Gates.TdgGate( 3 ))
circuit.inst(Gates.U2Gate(5.070978145808224, 4.861997899593006)( 6 ))
circuit.inst(Gates.CU3Gate(1.0200536425931515, 6.100759745363555, 3.891803045839442, 0, 4 ))
circuit.inst(Gates.C3SXGate( 7, 0, 1, 8 ))
circuit.inst(Gates.RYGate(3.345954529034082, 0 ))
circuit.inst(Gates.PhaseGate(0.6916556361503159, 3 ))
circuit.inst(Gates.RZZGate(5.548043373759139)( 0, 6 ))
circuit.inst(Gates.CYGate( 1, 2 ))
circuit.inst(Gates.CYGate( 4, 2 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.RCCXGate( 8, 5, 7 ))
circuit.inst(Gates.C4XGate( 0, 4, 5, 2, 6 ))
circuit.inst(Gates.U1Gate(0.1283649697684065, 8 ))
circuit.inst(Gates.U1Gate(5.195347791320497, 2 ))

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

