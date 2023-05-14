
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_e3c499 = circuit.declare('p_e3c499', 'REAL')
p_52f0db = circuit.declare('p_52f0db', 'REAL')

defns = get_custom_get_definitions("CHGate", "iSwapGate", "RYYGate", "SdgGate", "CCXGate", "RZGate", "CRXGate", "CSXGate", "SGate", "SXdgGate", "ZGate", "XGate")

circuit += defns

circuit.inst(Gates.RZGate(p_e3c499, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(p_52f0db)( 1, 0 ))
circuit.inst(Gates.ZGate( 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_e3c499": 6.163759533339787,
    "p_52f0db": 1.6723037552953224
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

