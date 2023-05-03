
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 8)

p_9d7979 = circuit.declare('p_9d7979', 'REAL')
p_bddf4b = circuit.declare('p_bddf4b', 'REAL')
p_8e5ef3 = circuit.declare('p_8e5ef3', 'REAL')
p_b8849a = circuit.declare('p_b8849a', 'REAL')
p_40773a = circuit.declare('p_40773a', 'REAL')

defns = get_custom_get_definitions("C3SXGate", "RYYGate", "SXGate", "CRXGate", "CU1Gate", "ZGate", "XGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.CRXGate(p_40773a, 6, 0 ))
circuit.inst(Gates.CRZGate(p_8e5ef3, 5, 0 ))
circuit.inst(Gates.C3SXGate( 6, 4, 0, 1 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.RYYGate(p_b8849a)( 0, 4 ))
circuit.inst(Gates.CRZGate(p_bddf4b, 5, 4 ))
circuit.inst(Gates.RZGate(p_9d7979, 5 ))
circuit.inst(Gates.SXGate( 6 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 2, 6 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 0, 2 ))

circuit += MEASURE(6, qr[0])
circuit += MEASURE(5, qr[1])
circuit += MEASURE(7, qr[2])
circuit += MEASURE(1, qr[3])
circuit += MEASURE(2, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(0, qr[6])
circuit += MEASURE(4, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_9d7979": 4.229610589867865,
    "p_bddf4b": 4.167661441102218,
    "p_8e5ef3": 1.0296448789776642,
    "p_b8849a": 1.740253089260498,
    "p_40773a": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

