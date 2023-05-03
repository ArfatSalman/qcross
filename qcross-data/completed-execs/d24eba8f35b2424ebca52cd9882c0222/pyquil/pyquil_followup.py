
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_cd62bb = circuit.declare('p_cd62bb', 'REAL')
p_d57ef9 = circuit.declare('p_d57ef9', 'REAL')

defns = get_custom_get_definitions("CSXGate", "ECRGate", "CXGate", "CPhaseGate", "RZGate", "SXdgGate", "RXGate", "ZGate", "DCXGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_d57ef9, 2 ))
circuit.inst(Gates.SXdgGate( 3 ))
circuit.inst(Gates.CSXGate( 0, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.DCXGate( 0, 4 ))
subcircuit.inst(Gates.CPhaseGate(1.6161683469432118, 0, 4 ))
subcircuit.inst(Gates.RXGate(p_cd62bb, 0 ))
subcircuit.inst(Gates.ZGate( 1 ))
subcircuit.inst(Gates.CXGate( 3, 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ECRGate( 2, 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 4, 2 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(3, qr[2])
circuit += MEASURE(2, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_cd62bb": 6.033961191253911,
    "p_d57ef9": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

