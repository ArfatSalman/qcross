
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_384a3b = circuit.declare('p_384a3b', 'REAL')

defns = get_custom_get_definitions("CCXGate", "ZGate", "RZGate", "TGate", "RZZGate", "SXGate", "SGate", "C3SXGate", "RC3XGate", "RXXGate", "RYYGate", "CU1Gate", "UGate", "CUGate", "RCCXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 1 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 2, 0 ))
circuit.inst(Gates.C3SXGate( 5, 1, 4, 2 ))
circuit.inst(Gates.CCXGate( 5, 3, 4 ))
circuit.inst(Gates.C3SXGate( 1, 0, 3, 4 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.RCCXGate( 3, 0, 1 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 5, 3 ))
circuit.inst(Gates.RZGate(4.229610589867865, 5 ))

subcircuit = Program()
subcircuit.inst(Gates.RC3XGate( 3, 1, 4, 5 ))
subcircuit.inst(Gates.RXXGate(1.1349349609188835)( 5, 2 ))
subcircuit.inst(Gates.RYYGate(0.6724371252296606)( 4, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 4, 2, 5, 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 0, 4 ))
circuit.inst(Gates.UGate(p_384a3b, 0.07157463504881167, 1.4112277317699358)( 3 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 4, 3 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 4, 3 ))

circuit += MEASURE(4, qr[0])
circuit += MEASURE(5, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(0, qr[3])
circuit += MEASURE(1, qr[4])
circuit += MEASURE(3, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_384a3b": 5.887184334931191
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

