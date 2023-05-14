
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_9c95f7 = circuit.declare('p_9c95f7', 'REAL')
p_201117 = circuit.declare('p_201117', 'REAL')
p_3f3854 = circuit.declare('p_3f3854', 'REAL')
p_eeece4 = circuit.declare('p_eeece4', 'REAL')
p_8ca533 = circuit.declare('p_8ca533', 'REAL')
p_47be8d = circuit.declare('p_47be8d', 'REAL')
p_0c155d = circuit.declare('p_0c155d', 'REAL')

defns = get_custom_get_definitions("CHGate", "ZGate", "RXXGate", "CU1Gate", "RCCXGate", "SGate", "C3SXGate", "CUGate", "SXdgGate", "XGate", "iSwapGate", "RZZGate", "RZGate", "TGate", "CSXGate", "RYYGate")

circuit += defns

circuit.inst(Gates.RZGate(p_201117, 1 ))
circuit.inst(Gates.RZZGate(p_3f3854)( 2, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.RXXGate(0.2906326206587185)( 3, 0 ))
subcircuit.inst(Gates.ZGate( 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_eeece4, p_0c155d, p_8ca533, p_9c95f7, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_47be8d, 3, 0 ))
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

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_9c95f7": 5.987304452123941,
    "p_201117": 6.163759533339787,
    "p_3f3854": 4.066449154047175,
    "p_eeece4": 0.5112149185250571,
    "p_8ca533": 2.3864521352475245,
    "p_47be8d": 5.154187354656876,
    "p_0c155d": 5.897054719225356
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

