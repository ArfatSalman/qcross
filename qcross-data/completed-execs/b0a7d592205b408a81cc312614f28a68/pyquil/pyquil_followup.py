
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)

p_8f5281 = circuit.declare('p_8f5281', 'REAL')
p_39dba4 = circuit.declare('p_39dba4', 'REAL')
p_5f2994 = circuit.declare('p_5f2994', 'REAL')
p_b6dc31 = circuit.declare('p_b6dc31', 'REAL')
p_078f44 = circuit.declare('p_078f44', 'REAL')
p_7ad57d = circuit.declare('p_7ad57d', 'REAL')
p_bb9f8c = circuit.declare('p_bb9f8c', 'REAL')
p_31d873 = circuit.declare('p_31d873', 'REAL')
p_ab882a = circuit.declare('p_ab882a', 'REAL')
p_3d1a45 = circuit.declare('p_3d1a45', 'REAL')
p_14147f = circuit.declare('p_14147f', 'REAL')
p_584aac = circuit.declare('p_584aac', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "iSwapGate", "C3SXGate", "UGate", "CU1Gate", "RYYGate", "CUGate", "SGate", "RZGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CSwapGate", "SXGate", "PhaseGate")

circuit += defns

circuit.inst(Gates.RZGate(p_bb9f8c, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_8f5281, p_b6dc31, p_ab882a, p_31d873, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_078f44, 8, 3 ))
circuit.inst(Gates.CRZGate(p_7ad57d, 5, 8 ))

subcircuit = Program()
subcircuit.inst(Gates.CSwapGate( 0, 6, 5 ))
subcircuit.inst(Gates.CSXGate( 6, 1 ))
subcircuit.inst(Gates.SXGate( 3 ))
subcircuit.inst(Gates.SXdgGate( 6 ))
subcircuit.inst(Gates.RYYGate(p_3d1a45)( 0, 4 ))
subcircuit.inst(Gates.iSwapGate( 5, 7 ))
subcircuit.inst(Gates.UGate(p_39dba4, p_14147f, p_5f2994)( 3 ))
subcircuit.inst(Gates.PhaseGate(p_584aac, 8 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))

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
    "p_8f5281": 0.5112149185250571,
    "p_39dba4": 2.438459595578943,
    "p_5f2994": 3.4232119351142516,
    "p_b6dc31": 5.897054719225356,
    "p_078f44": 3.2142159669963557,
    "p_7ad57d": 1.4112277317699358,
    "p_bb9f8c": 6.163759533339787,
    "p_31d873": 5.987304452123941,
    "p_ab882a": 2.3864521352475245,
    "p_3d1a45": 0.6724371252296606,
    "p_14147f": 3.326780904591333,
    "p_584aac": 0.4827903095199283
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

