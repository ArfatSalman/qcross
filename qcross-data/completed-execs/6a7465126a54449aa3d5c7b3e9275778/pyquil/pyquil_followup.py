
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CCXGate", "TGate", "CRXGate", "RZGate", "CRZGate", "U3Gate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 2, 8 ))

subcircuit = Program()
subcircuit.inst(Gates.U3Gate(5.007412428963378, 4.658325508156331, 3.8184561666262637)( 6 ))
subcircuit.inst(Gates.CRXGate(4.736752714049485, 7, 5 ))
subcircuit.inst(Gates.TGate( 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CCXGate( 4, 7, 8 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(2, qr[1])
circuit += MEASURE(9, qr[2])
circuit += MEASURE(1, qr[3])
circuit += MEASURE(3, qr[4])
circuit += MEASURE(4, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(8, qr[7])
circuit += MEASURE(5, qr[8])
circuit += MEASURE(7, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

