
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("CPhaseGate", "CU1Gate", "UGate", "SXGate", "TdgGate", "RZXGate", "RXGate", "CXGate", "YGate", "CSGate", "ZGate", "CRYGate", "CCZGate", "SdgGate")

circuit += defns

circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.CRYGate(0.8476513988624245, 4, 0 ))
circuit.inst(Gates.CU1Gate(1.5710197357755318, 3, 2 ))
circuit.inst(Gates.TdgGate( 2 ))
circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.CCZGate( 2, 1, 3 ))
circuit.inst(Gates.UGate(0.708502006099043, 2.97765669736744, 5.6444063351584415)( 2 ))
circuit.inst(Gates.CPhaseGate(5.597667172921795, 3, 4 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CRYGate(0.3177314062860099, 4, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.CSGate( 3, 0 ))
subcircuit.inst(Gates.SdgGate( 3 ))
subcircuit.inst(Gates.CRYGate(2.8571614999629205, 1, 0 ))
subcircuit.inst(Gates.RZXGate(1.1653856966610614)( 2, 1 ))
subcircuit.inst(Gates.RXGate(5.646774609269053, 4 ))
subcircuit.inst(Gates.CXGate( 2, 1 ))
subcircuit.inst(Gates.ZGate( 4 ))
subcircuit.inst(Gates.YGate( 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CU1Gate(1.9730677082046415, 4, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

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

