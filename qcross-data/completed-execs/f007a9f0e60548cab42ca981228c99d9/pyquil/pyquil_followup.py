
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CRZGate", "CU1Gate", "CXGate", "XGate", "CSXGate", "ECRGate", "PhaseGate", "CPhaseGate", "C3SXGate", "SGate", "SXdgGate", "RCCXGate", "CUGate", "RZGate", "ZGate", "iSwapGate", "CRXGate", "SdgGate", "SXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))

subcircuit = Program()
subcircuit.inst(Gates.SXdgGate( 0 ))
subcircuit.inst(Gates.CXGate( 2, 3 ))
subcircuit.inst(Gates.iSwapGate( 1, 6 ))
subcircuit.inst(Gates.CPhaseGate(3.326780904591333, 0, 6 ))
subcircuit.inst(Gates.CU1Gate(2.0685963035149753, 4, 0 ))
subcircuit.inst(Gates.PhaseGate(5.336667571035288, 0 ))
subcircuit.inst(Gates.CUGate(5.014941143947427, 4.437078557875917, 6.016631690603051, 3.1243053509071124, 1, 2 ))
subcircuit.inst(Gates.SXGate( 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 4, 6 ))
circuit.inst(Gates.CHGate( 4, 0 ))
circuit.inst(Gates.C3SXGate( 2, 0, 3, 4 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 6 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 1, 4 ))
circuit.inst(Gates.C3SXGate( 2, 0, 5, 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])




circuit.wrap_in_numshots_loop(1959)

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

