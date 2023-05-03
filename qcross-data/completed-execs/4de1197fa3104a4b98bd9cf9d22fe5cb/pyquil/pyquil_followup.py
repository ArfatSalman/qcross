
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_4d1002 = circuit.declare('p_4d1002', 'REAL')
p_95d4c5 = circuit.declare('p_95d4c5', 'REAL')
p_c4621c = circuit.declare('p_c4621c', 'REAL')
p_7c06d6 = circuit.declare('p_7c06d6', 'REAL')
p_1cef4d = circuit.declare('p_1cef4d', 'REAL')
p_643384 = circuit.declare('p_643384', 'REAL')
p_0fdd04 = circuit.declare('p_0fdd04', 'REAL')
p_27af66 = circuit.declare('p_27af66', 'REAL')
p_c93870 = circuit.declare('p_c93870', 'REAL')
p_acd0b1 = circuit.declare('p_acd0b1', 'REAL')
p_d935d2 = circuit.declare('p_d935d2', 'REAL')
p_56ef16 = circuit.declare('p_56ef16', 'REAL')

defns = get_custom_get_definitions("CRZGate", "C3SXGate", "CHGate", "CU1Gate", "RZZGate", "CUGate", "SwapGate", "TGate", "SXdgGate", "iSwapGate", "RCCXGate", "U1Gate", "XGate", "SGate", "RZGate", "CRXGate", "RYYGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_95d4c5, 1 ))
circuit.inst(Gates.RZZGate(p_c93870)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_0fdd04, p_c4621c, p_7c06d6, p_1cef4d, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_d935d2, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.U1Gate(4.8767543643948805, 0 ))
subcircuit.inst(Gates.SwapGate( 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(p_acd0b1)( 2, 0 ))
circuit.inst(Gates.RCCXGate( 2, 3, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(p_643384, 0, 1 ))
circuit.inst(Gates.C3SXGate( 1, 2, 0, 3 ))
circuit.inst(Gates.RYYGate(p_56ef16)( 2, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.CU1Gate(p_27af66, 0, 3 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CRXGate(p_4d1002, 2, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_4d1002": 5.94477504571567,
    "p_95d4c5": 6.163759533339787,
    "p_c4621c": 5.897054719225356,
    "p_7c06d6": 2.3864521352475245,
    "p_1cef4d": 5.987304452123941,
    "p_643384": 2.9790366726895714,
    "p_0fdd04": 0.5112149185250571,
    "p_27af66": 3.2142159669963557,
    "p_c93870": 4.066449154047175,
    "p_acd0b1": 1.740253089260498,
    "p_d935d2": 5.154187354656876,
    "p_56ef16": 5.398622178940033
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

