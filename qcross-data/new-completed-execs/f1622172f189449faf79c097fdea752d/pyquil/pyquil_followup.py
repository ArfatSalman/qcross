
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("CHGate", "CSGate", "RC3XGate", "CXGate", "RZGate", "UGate", "XGate", "SXGate")

circuit += defns

circuit.inst(Gates.CSGate( 5, 0 ))
circuit.inst(Gates.SXGate( 5 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RC3XGate( 5, 0, 4, 2 ))
circuit.inst(Gates.RZGate(4.9678427199825475, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CSGate( 0, 2 ))
subcircuit.inst(Gates.XGate( 1 ))
subcircuit.inst(Gates.UGate(0.21975397537203006, 2.6790197391768045, 5.406299174556028)( 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CXGate( 3, 1 ))
circuit.inst(Gates.RC3XGate( 4, 2, 0, 5 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

