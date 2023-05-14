
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_51446f = circuit.declare('p_51446f', 'REAL')
p_40d80f = circuit.declare('p_40d80f', 'REAL')
p_2e845a = circuit.declare('p_2e845a', 'REAL')
p_75570c = circuit.declare('p_75570c', 'REAL')
p_94fb1b = circuit.declare('p_94fb1b', 'REAL')
p_002797 = circuit.declare('p_002797', 'REAL')
p_b6d4eb = circuit.declare('p_b6d4eb', 'REAL')

defns = get_custom_get_definitions("SXdgGate", "iSwapGate", "C3SXGate", "RCCXGate", "RZZGate", "CU1Gate", "CUGate", "RZGate", "TGate", "XGate", "CSXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(p_40d80f, 1 ))
circuit.inst(Gates.RZZGate(p_75570c)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_94fb1b, p_002797, p_51446f, p_b6d4eb, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_2e845a, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_51446f": 2.3864521352475245,
    "p_40d80f": 6.163759533339787,
    "p_2e845a": 5.154187354656876,
    "p_75570c": 4.066449154047175,
    "p_94fb1b": 0.5112149185250571,
    "p_002797": 5.897054719225356,
    "p_b6d4eb": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

