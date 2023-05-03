
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_7d7ce5 = circuit.declare('p_7d7ce5', 'REAL')
p_7291d9 = circuit.declare('p_7291d9', 'REAL')
p_f3c89a = circuit.declare('p_f3c89a', 'REAL')
p_8a1a82 = circuit.declare('p_8a1a82', 'REAL')
p_922074 = circuit.declare('p_922074', 'REAL')
p_6c1345 = circuit.declare('p_6c1345', 'REAL')
p_4bcda6 = circuit.declare('p_4bcda6', 'REAL')
p_45c2b7 = circuit.declare('p_45c2b7', 'REAL')

defns = get_custom_get_definitions("SXdgGate", "XGate", "RZGate", "CSXGate", "SGate", "ZGate", "RCCXGate", "CHGate", "CRXGate", "RYYGate", "SdgGate", "ECRGate", "TGate", "CCXGate", "U1Gate", "iSwapGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_7291d9, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(p_922074, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(p_4bcda6)( 1, 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.ECRGate( 2, 0 ))
circuit.inst(Gates.XGate( 1 ))

subcircuit = Program()
subcircuit.inst(Gates.RYYGate(p_7d7ce5)( 2, 0 ))
subcircuit.inst(Gates.U1Gate(p_45c2b7, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RCCXGate( 1, 0, 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RCCXGate( 0, 2, 1 ))
circuit.inst(Gates.CRZGate(p_6c1345, 2, 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CRZGate(p_f3c89a, 2, 1 ))
circuit.inst(Gates.RYYGate(p_8a1a82)( 1, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_7d7ce5": 0.2906326206587185,
    "p_7291d9": 6.163759533339787,
    "p_f3c89a": 0.05525155902669336,
    "p_8a1a82": 3.2287759437031154,
    "p_922074": 5.987304452123941,
    "p_6c1345": 4.167661441102218,
    "p_4bcda6": 1.6723037552953224,
    "p_45c2b7": 1.4447770477048325
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

