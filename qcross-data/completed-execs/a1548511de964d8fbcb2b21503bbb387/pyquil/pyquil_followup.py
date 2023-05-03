
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_32432c = circuit.declare('p_32432c', 'REAL')

defns = get_custom_get_definitions("HGate", "RZXGate", "DCXGate", "CPhaseGate", "CXGate", "RXGate", "ZGate", "ECRGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.ECRGate( 1, 0 ))
subcircuit.inst(Gates.HGate( 1 ))
subcircuit.inst(Gates.RZXGate(0.6833824466861163)( 0, 2 ))
subcircuit.inst(Gates.DCXGate( 1, 4 ))
subcircuit.inst(Gates.CPhaseGate(1.6161683469432118, 1, 4 ))
subcircuit.inst(Gates.RXGate(p_32432c, 1 ))
subcircuit.inst(Gates.ZGate( 0 ))
subcircuit.inst(Gates.CXGate( 2, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())


circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_32432c": 6.033961191253911
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

