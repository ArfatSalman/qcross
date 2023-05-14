
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_63d6aa = circuit.declare('p_63d6aa', 'REAL')
p_92b6fe = circuit.declare('p_92b6fe', 'REAL')
p_db8eb2 = circuit.declare('p_db8eb2', 'REAL')
p_b138c0 = circuit.declare('p_b138c0', 'REAL')
p_2f176b = circuit.declare('p_2f176b', 'REAL')
p_4a9935 = circuit.declare('p_4a9935', 'REAL')
p_b2e764 = circuit.declare('p_b2e764', 'REAL')
p_bfb580 = circuit.declare('p_bfb580', 'REAL')
p_dfd8ce = circuit.declare('p_dfd8ce', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "XGate", "RZGate", "TGate", "CUGate", "RYYGate", "SXdgGate", "CHGate", "CSXGate", "SGate", "C3SXGate", "CRZGate", "CU1Gate", "iSwapGate", "RZZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_92b6fe, 1 ))
circuit.inst(Gates.RZZGate(p_4a9935)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_dfd8ce, p_db8eb2, 2.3864521352475245, p_bfb580, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_b2e764, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(p_2f176b)( 2, 0 ))
circuit.inst(Gates.RCCXGate( 2, 3, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(p_b138c0, 0, 1 ))
circuit.inst(Gates.C3SXGate( 1, 2, 0, 3 ))
circuit.inst(Gates.RYYGate(p_63d6aa)( 2, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))

qr_c7cdf6 = circuit.declare("qr_c7cdf6", "BIT", 8)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_63d6aa": 5.398622178940033,
    "p_92b6fe": 6.163759533339787,
    "p_db8eb2": 5.897054719225356,
    "p_b138c0": 2.9790366726895714,
    "p_2f176b": 1.740253089260498,
    "p_4a9935": 4.066449154047175,
    "p_b2e764": 5.154187354656876,
    "p_bfb580": 5.987304452123941,
    "p_dfd8ce": 0.5112149185250571
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        


quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

