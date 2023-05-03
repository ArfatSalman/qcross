
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 9)

p_299687 = circuit.declare('p_299687', 'REAL')
p_2d28aa = circuit.declare('p_2d28aa', 'REAL')
p_efba95 = circuit.declare('p_efba95', 'REAL')
p_c3019d = circuit.declare('p_c3019d', 'REAL')
p_0fe9c2 = circuit.declare('p_0fe9c2', 'REAL')
p_9640e8 = circuit.declare('p_9640e8', 'REAL')
p_0e9aa7 = circuit.declare('p_0e9aa7', 'REAL')
p_101f6d = circuit.declare('p_101f6d', 'REAL')
p_2ef906 = circuit.declare('p_2ef906', 'REAL')

defns = get_custom_get_definitions("CHGate", "SGate", "C3SXGate", "CSXGate", "CUGate", "SdgGate", "SXGate", "CU1Gate", "TGate", "CCXGate", "U2Gate", "ZGate", "XGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_2d28aa, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_9640e8, 5.897054719225356, p_2ef906, p_0fe9c2, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_299687, 8, 3 ))
circuit.inst(Gates.CRZGate(p_c3019d, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(p_efba95, 1, 2 ))
circuit.inst(Gates.U2Gate(p_0e9aa7, p_101f6d)( 2 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.CCXGate( 0, 6, 1 ))

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
    "p_299687": 3.2142159669963557,
    "p_2d28aa": 6.163759533339787,
    "p_efba95": 2.586208953975239,
    "p_c3019d": 1.4112277317699358,
    "p_0fe9c2": 5.987304452123941,
    "p_9640e8": 0.5112149185250571,
    "p_0e9aa7": 2.5163050709890156,
    "p_101f6d": 2.1276323672732023,
    "p_2ef906": 2.3864521352475245
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

