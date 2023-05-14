
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_845551 = circuit.declare('p_845551', 'REAL')
p_1ada4b = circuit.declare('p_1ada4b', 'REAL')
p_2b124e = circuit.declare('p_2b124e', 'REAL')
p_f7bbfa = circuit.declare('p_f7bbfa', 'REAL')
p_f1397b = circuit.declare('p_f1397b', 'REAL')
p_b60795 = circuit.declare('p_b60795', 'REAL')
p_505de8 = circuit.declare('p_505de8', 'REAL')

defns = get_custom_get_definitions("CRZGate", "C3SXGate", "RCCXGate", "RZZGate", "CRXGate", "CU1Gate", "CUGate", "SGate", "RZGate", "TGate", "SXGate", "ZGate", "UGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_b60795, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(p_2b124e, 5.897054719225356, p_f7bbfa, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 5 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_f1397b, 3, 0 ))
circuit.inst(Gates.UGate(p_505de8, 0.07157463504881167, 1.4112277317699358)( 5 ))
circuit.inst(Gates.RZZGate(p_1ada4b)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 5 ))
circuit.inst(Gates.CU1Gate(p_845551, 1, 4 ))
circuit.inst(Gates.C3SXGate( 3, 0, 4, 2 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 2, 5 ))
circuit.inst(Gates.CRXGate(2.6687018103754414, 4, 5 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_845551": 4.028174522740928,
    "p_1ada4b": 5.1829934776392745,
    "p_2b124e": 0.5112149185250571,
    "p_f7bbfa": 2.3864521352475245,
    "p_f1397b": 3.2142159669963557,
    "p_b60795": 6.163759533339787,
    "p_505de8": 5.887184334931191
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

