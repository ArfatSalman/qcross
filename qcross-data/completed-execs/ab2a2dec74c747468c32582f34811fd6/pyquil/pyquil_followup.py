
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 5)

p_219d62 = circuit.declare('p_219d62', 'REAL')
p_f67f84 = circuit.declare('p_f67f84', 'REAL')
p_b9edf2 = circuit.declare('p_b9edf2', 'REAL')
p_cac0af = circuit.declare('p_cac0af', 'REAL')
p_c04ae3 = circuit.declare('p_c04ae3', 'REAL')
p_7ec521 = circuit.declare('p_7ec521', 'REAL')

defns = get_custom_get_definitions("RYYGate", "CHGate", "XGate", "IGate", "ECRGate", "CSwapGate", "ZGate", "TGate", "CU3Gate", "CSXGate", "CU1Gate", "CRZGate", "HGate", "CRXGate", "UGate", "SXdgGate", "SGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_c04ae3, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_219d62)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))

subcircuit = Program()
subcircuit.inst(Gates.CU1Gate(p_cac0af, 2, 4 ))
subcircuit.inst(Gates.CU3Gate(p_b9edf2, 2.6636908506222836, 6.221353754875494, 4, 1 ))
subcircuit.inst(Gates.IGate( 1 ))
subcircuit.inst(Gates.IGate( 0 ))
subcircuit.inst(Gates.ECRGate( 3, 1 ))
subcircuit.inst(Gates.UGate(p_7ec521, 2.3568871696687452, 6.011900464835247)( 2 ))
subcircuit.inst(Gates.CSwapGate( 0, 4, 1 ))
subcircuit.inst(Gates.HGate( 0 ))
subcircuit.inst(Gates.CRXGate(p_f67f84, 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_219d62": 1.6723037552953224,
    "p_f67f84": 5.091930552861214,
    "p_b9edf2": 3.865496458458116,
    "p_cac0af": 4.501598818751339,
    "p_c04ae3": 6.163759533339787,
    "p_7ec521": 3.5173414605326783
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

