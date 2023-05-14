
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 9)

p_a2a414 = circuit.declare('p_a2a414', 'REAL')
p_560035 = circuit.declare('p_560035', 'REAL')
p_47c65c = circuit.declare('p_47c65c', 'REAL')
p_0a6c0e = circuit.declare('p_0a6c0e', 'REAL')
p_fa3e46 = circuit.declare('p_fa3e46', 'REAL')
p_26dfb8 = circuit.declare('p_26dfb8', 'REAL')

defns = get_custom_get_definitions("ZGate", "RZGate", "XGate", "SXGate", "SGate", "SdgGate", "C3SXGate", "CU1Gate", "CUGate", "CSXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_0a6c0e, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_a2a414, p_560035, p_26dfb8, p_47c65c, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_fa3e46, 8, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))

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



params = {
    "p_a2a414": 0.5112149185250571,
    "p_560035": 5.897054719225356,
    "p_47c65c": 5.987304452123941,
    "p_0a6c0e": 6.163759533339787,
    "p_fa3e46": 3.2142159669963557,
    "p_26dfb8": 2.3864521352475245
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

