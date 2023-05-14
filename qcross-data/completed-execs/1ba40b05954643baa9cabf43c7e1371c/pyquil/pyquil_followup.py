
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 9)

p_a97204 = circuit.declare('p_a97204', 'REAL')
p_c78fcf = circuit.declare('p_c78fcf', 'REAL')
p_209b89 = circuit.declare('p_209b89', 'REAL')
p_f92e12 = circuit.declare('p_f92e12', 'REAL')
p_0564dd = circuit.declare('p_0564dd', 'REAL')
p_e4c2ac = circuit.declare('p_e4c2ac', 'REAL')

defns = get_custom_get_definitions("XGate", "CRZGate", "CU1Gate", "ZGate", "SXGate", "U2Gate", "CUGate", "CHGate", "TGate", "CSXGate", "RZGate", "C3SXGate", "SGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_a97204, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_209b89, p_0564dd, 2.3864521352475245, 5.987304452123941, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 8, 3 ))
circuit.inst(Gates.CRZGate(p_c78fcf, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(p_e4c2ac, 1, 2 ))
circuit.inst(Gates.U2Gate(p_f92e12, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 8 ))

qr_173848 = circuit.declare("qr_173848", "BIT", 3)

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
    "p_a97204": 6.163759533339787,
    "p_c78fcf": 1.4112277317699358,
    "p_209b89": 0.5112149185250571,
    "p_f92e12": 2.5163050709890156,
    "p_0564dd": 5.897054719225356,
    "p_e4c2ac": 2.586208953975239
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

