
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)

p_fa6b38 = circuit.declare('p_fa6b38', 'REAL')
p_b444cc = circuit.declare('p_b444cc', 'REAL')
p_6274c7 = circuit.declare('p_6274c7', 'REAL')
p_8b3e71 = circuit.declare('p_8b3e71', 'REAL')
p_5f6e00 = circuit.declare('p_5f6e00', 'REAL')
p_3f9d0c = circuit.declare('p_3f9d0c', 'REAL')
p_df034d = circuit.declare('p_df034d', 'REAL')

defns = get_custom_get_definitions("CRZGate", "CHGate", "CU1Gate", "CUGate", "SXGate", "ZGate", "SdgGate", "XGate", "SGate", "RZGate", "C3SXGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_fa6b38, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_6274c7, p_df034d, p_b444cc, p_3f9d0c, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_8b3e71, 8, 3 ))
circuit.inst(Gates.CRZGate(p_5f6e00, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))

qr_f74fe2 = circuit.declare("qr_f74fe2", "BIT", 9)

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
    "p_fa6b38": 6.163759533339787,
    "p_b444cc": 2.3864521352475245,
    "p_6274c7": 0.5112149185250571,
    "p_8b3e71": 3.2142159669963557,
    "p_5f6e00": 1.4112277317699358,
    "p_3f9d0c": 5.987304452123941,
    "p_df034d": 5.897054719225356
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

