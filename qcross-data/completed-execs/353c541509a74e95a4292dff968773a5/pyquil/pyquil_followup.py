
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)

p_ca4ae7 = circuit.declare('p_ca4ae7', 'REAL')
p_350212 = circuit.declare('p_350212', 'REAL')
p_3be268 = circuit.declare('p_3be268', 'REAL')
p_e86f21 = circuit.declare('p_e86f21', 'REAL')
p_8cc9b1 = circuit.declare('p_8cc9b1', 'REAL')
p_09c913 = circuit.declare('p_09c913', 'REAL')

defns = get_custom_get_definitions("ECRGate", "CU1Gate", "RZZGate", "CXGate", "HGate", "CUGate", "RZGate", "TGate", "CSXGate", "TdgGate", "C3SXGate", "SXdgGate", "iSwapGate", "CHGate", "XGate")

circuit += defns

circuit.inst(Gates.RZGate(p_ca4ae7, 1 ))
circuit.inst(Gates.RZZGate(p_e86f21)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_350212, p_8cc9b1, p_09c913, 5.987304452123941, 0, 2 ))
circuit.inst(Gates.CU1Gate(5.154187354656876, 3, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.CXGate( 3, 0 ))
subcircuit.inst(Gates.RZGate(p_3be268, 2 ))
subcircuit.inst(Gates.TdgGate( 0 ))
subcircuit.inst(Gates.HGate( 1 ))
subcircuit.inst(Gates.CU1Gate(4.229610589867865, 1, 3 ))
subcircuit.inst(Gates.ECRGate( 1, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_ca4ae7": 6.163759533339787,
    "p_350212": 0.5112149185250571,
    "p_3be268": 3.8580685613059242,
    "p_e86f21": 4.066449154047175,
    "p_8cc9b1": 5.897054719225356,
    "p_09c913": 2.3864521352475245
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

