
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("RZGate", "CCXGate", "CSXGate", "SGate", "SdgGate", "iSwapGate", "CRXGate", "SXdgGate", "XGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.iSwapGate( 0, 2 ))
circuit.inst(Gates.CSXGate( 2, 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CCXGate( 2, 1, 0 ))
circuit.inst(Gates.CHGate( 0, 1 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(2, qr[1])
circuit += MEASURE(0, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

