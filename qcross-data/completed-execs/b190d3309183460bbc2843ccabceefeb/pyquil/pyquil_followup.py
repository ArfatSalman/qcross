
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_158674 = circuit.declare('p_158674', 'REAL')
p_bac5cc = circuit.declare('p_bac5cc', 'REAL')
p_1a1575 = circuit.declare('p_1a1575', 'REAL')
p_f59945 = circuit.declare('p_f59945', 'REAL')

defns = get_custom_get_definitions("RZGate", "ZGate", "RCCXGate", "SGate", "C3SXGate", "RZZGate", "RYYGate", "UGate", "TGate", "CCXGate", "CU1Gate", "SXGate", "RXXGate", "CUGate", "CRZGate", "RC3XGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(p_1a1575, 1, 5 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.RC3XGate( 5, 4, 0, 1 ))
subcircuit.inst(Gates.RXXGate(1.1349349609188835)( 1, 2 ))
subcircuit.inst(Gates.RYYGate(0.6724371252296606)( 0, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(p_158674, 0.07157463504881167, p_f59945)( 5 ))
circuit.inst(Gates.RZZGate(p_bac5cc)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 5 ))

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
    "p_158674": 5.887184334931191,
    "p_bac5cc": 5.1829934776392745,
    "p_1a1575": 4.167661441102218,
    "p_f59945": 1.4112277317699358
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

