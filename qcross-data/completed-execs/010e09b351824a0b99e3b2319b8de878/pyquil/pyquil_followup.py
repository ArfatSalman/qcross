
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)

p_0272f7 = circuit.declare('p_0272f7', 'REAL')
p_ea3f54 = circuit.declare('p_ea3f54', 'REAL')
p_0ac6c9 = circuit.declare('p_0ac6c9', 'REAL')
p_4e1de3 = circuit.declare('p_4e1de3', 'REAL')
p_7a489b = circuit.declare('p_7a489b', 'REAL')
p_74b354 = circuit.declare('p_74b354', 'REAL')
p_331ab9 = circuit.declare('p_331ab9', 'REAL')
p_2c12c6 = circuit.declare('p_2c12c6', 'REAL')
p_41dadf = circuit.declare('p_41dadf', 'REAL')
p_12df2a = circuit.declare('p_12df2a', 'REAL')

defns = get_custom_get_definitions("ZGate", "CHGate", "CU1Gate", "SGate", "SXGate", "C3SXGate", "CUGate", "XGate", "U2Gate", "RZGate", "CRZGate", "CSXGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_2c12c6, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_41dadf, p_7a489b, p_12df2a, p_4e1de3, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_0ac6c9, 8, 3 ))
circuit.inst(Gates.CRZGate(p_74b354, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(p_ea3f54, 1, 2 ))
circuit.inst(Gates.U2Gate(p_0272f7, p_331ab9)( 2 ))

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
    "p_0272f7": 2.5163050709890156,
    "p_ea3f54": 2.586208953975239,
    "p_0ac6c9": 3.2142159669963557,
    "p_4e1de3": 5.987304452123941,
    "p_7a489b": 5.897054719225356,
    "p_74b354": 1.4112277317699358,
    "p_331ab9": 2.1276323672732023,
    "p_2c12c6": 6.163759533339787,
    "p_41dadf": 0.5112149185250571,
    "p_12df2a": 2.3864521352475245
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

