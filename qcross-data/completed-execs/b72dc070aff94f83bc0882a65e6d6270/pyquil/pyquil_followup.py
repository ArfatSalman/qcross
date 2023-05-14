
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_78601e = circuit.declare('p_78601e', 'REAL')
p_91bcc8 = circuit.declare('p_91bcc8', 'REAL')
p_0a0a4b = circuit.declare('p_0a0a4b', 'REAL')
p_0ecc7a = circuit.declare('p_0ecc7a', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "ECRGate", "iSwapGate", "RCCXGate", "CRXGate", "RYYGate", "SGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SdgGate", "UGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_0ecc7a, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.UGate(2.9790366726895714, p_0a0a4b, 3.2287759437031154)( 1 ))
subcircuit.inst(Gates.SdgGate( 1 ))
subcircuit.inst(Gates.RYYGate(0.2906326206587185)( 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(p_91bcc8, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 1, 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.ECRGate( 2, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RCCXGate( 1, 0, 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RCCXGate( 0, 2, 1 ))
circuit.inst(Gates.CRZGate(p_78601e, 2, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_78601e": 4.167661441102218,
    "p_91bcc8": 5.987304452123941,
    "p_0a0a4b": 5.974354952564585,
    "p_0ecc7a": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

