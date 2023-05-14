
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("ZGate", "RZGate", "RZZGate", "SXGate", "C3SXGate", "CRXGate", "RYYGate", "CU1Gate", "XGate", "CSXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 4, 7 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 0, 7 ))
circuit.inst(Gates.C3SXGate( 4, 3, 7, 5 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 7, 3 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 0, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 2, 4 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 7, 2 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 3, 4 ))
circuit.inst(Gates.CSXGate( 4, 1 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.RZGate(3.775592041307464, 2 ))

circuit += MEASURE(4, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(1, qr[2])
circuit += MEASURE(5, qr[3])
circuit += MEASURE(2, qr[4])
circuit += MEASURE(6, qr[5])
circuit += MEASURE(7, qr[6])
circuit += MEASURE(3, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

