
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_a0ca5d = circuit.declare('p_a0ca5d', 'REAL')
p_8b617c = circuit.declare('p_8b617c', 'REAL')
p_1fce1b = circuit.declare('p_1fce1b', 'REAL')
p_32ce54 = circuit.declare('p_32ce54', 'REAL')
p_6530e4 = circuit.declare('p_6530e4', 'REAL')
p_bcda17 = circuit.declare('p_bcda17', 'REAL')
p_45f58e = circuit.declare('p_45f58e', 'REAL')
p_3962ff = circuit.declare('p_3962ff', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "U2Gate", "iSwapGate", "C3SXGate", "RCCXGate", "RZZGate", "CRXGate", "CU1Gate", "RYYGate", "CUGate", "SGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(p_a0ca5d, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, p_32ce54, p_1fce1b, 5.987304452123941, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_3962ff, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 2, 0 ))
circuit.inst(Gates.RCCXGate( 2, 3, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(2.9790366726895714, 0, 1 ))
circuit.inst(Gates.C3SXGate( 1, 2, 0, 3 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 2, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.CU1Gate(p_bcda17, 0, 3 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CRXGate(p_6530e4, 2, 0 ))
circuit.inst(Gates.U2Gate(p_8b617c, p_45f58e)( 2 ))
circuit.inst(Gates.ZGate( 0 ))

qr_937141 = circuit.declare("qr_937141", "BIT", 6)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_a0ca5d": 6.163759533339787,
    "p_8b617c": 4.214504315296764,
    "p_1fce1b": 2.3864521352475245,
    "p_32ce54": 5.897054719225356,
    "p_6530e4": 5.94477504571567,
    "p_bcda17": 3.2142159669963557,
    "p_45f58e": 4.6235667602042065,
    "p_3962ff": 5.154187354656876
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

