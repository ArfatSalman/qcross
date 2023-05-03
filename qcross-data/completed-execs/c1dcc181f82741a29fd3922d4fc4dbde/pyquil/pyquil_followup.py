
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_752feb = circuit.declare('p_752feb', 'REAL')
p_2ded38 = circuit.declare('p_2ded38', 'REAL')
p_5fc981 = circuit.declare('p_5fc981', 'REAL')
p_636ed6 = circuit.declare('p_636ed6', 'REAL')
p_c6e6fc = circuit.declare('p_c6e6fc', 'REAL')
p_8e5ab7 = circuit.declare('p_8e5ab7', 'REAL')
p_68a976 = circuit.declare('p_68a976', 'REAL')

defns = get_custom_get_definitions("CUGate", "TGate", "RZGate", "C3SXGate", "RCCXGate", "SGate", "CRZGate", "UGate", "CRYGate", "SXdgGate", "RYYGate", "RZZGate", "DCXGate", "CCXGate", "ZGate", "CU1Gate")

circuit += defns

circuit.inst(Gates.RZGate(p_752feb, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, p_636ed6, p_5fc981, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 5 ))
circuit.inst(Gates.RZGate(p_68a976, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.RCCXGate( 4, 5, 1 ))
subcircuit.inst(Gates.CRYGate(3.1402006997068588, 3, 0 ))
subcircuit.inst(Gates.SXdgGate( 4 ))
subcircuit.inst(Gates.DCXGate( 1, 2 ))
subcircuit.inst(Gates.RYYGate(0.6724371252296606)( 0, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(p_2ded38, p_8e5ab7, 1.4112277317699358)( 5 ))
circuit.inst(Gates.RZZGate(p_c6e6fc)( 0, 5 ))

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
    "p_752feb": 6.163759533339787,
    "p_2ded38": 5.887184334931191,
    "p_5fc981": 2.3864521352475245,
    "p_636ed6": 5.897054719225356,
    "p_c6e6fc": 5.1829934776392745,
    "p_8e5ab7": 0.07157463504881167,
    "p_68a976": 4.229610589867865
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

