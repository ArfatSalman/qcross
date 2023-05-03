
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"PARTIAL"']) )

qr = circuit.declare("ro", "BIT", 6)

p_c1c477 = circuit.declare('p_c1c477', 'REAL')
p_4266cb = circuit.declare('p_4266cb', 'REAL')
p_8c222d = circuit.declare('p_8c222d', 'REAL')
p_af0e12 = circuit.declare('p_af0e12', 'REAL')
p_6f466e = circuit.declare('p_6f466e', 'REAL')
p_ef2512 = circuit.declare('p_ef2512', 'REAL')
p_961b75 = circuit.declare('p_961b75', 'REAL')
p_aa5f2d = circuit.declare('p_aa5f2d', 'REAL')

defns = get_custom_get_definitions("UGate", "SXGate", "RZGate", "C3SXGate", "CCXGate", "RZZGate", "SGate", "TGate", "CUGate", "ZGate", "RCCXGate", "CU1Gate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_961b75, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_af0e12, 2, 4 ))
circuit.inst(Gates.CUGate(p_6f466e, 5.897054719225356, p_aa5f2d, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(p_c1c477, 1, 5 ))
circuit.inst(Gates.RZGate(p_8c222d, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_4266cb, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( 5 ))
circuit.inst(Gates.RZZGate(p_ef2512)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))

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
    "p_c1c477": 4.167661441102218,
    "p_4266cb": 3.2142159669963557,
    "p_8c222d": 4.229610589867865,
    "p_af0e12": 4.2641612072511235,
    "p_6f466e": 0.5112149185250571,
    "p_ef2512": 5.1829934776392745,
    "p_961b75": 6.163759533339787,
    "p_aa5f2d": 2.3864521352475245
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

