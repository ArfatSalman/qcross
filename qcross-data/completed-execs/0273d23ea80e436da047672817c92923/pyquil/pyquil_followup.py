
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("CSwapGate", "ECRGate", "CCXGate", "CUGate", "PhaseGate", "RZGate", "ZGate", "CRZGate", "RCCXGate", "U3Gate", "XGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))

subcircuit = Program()
subcircuit.inst(Gates.U3Gate(0.5150078127444868, 5.017245588344839, 2.936349225876477)( 3 ))
subcircuit.inst(Gates.XGate( 0 ))
subcircuit.inst(Gates.RCCXGate( 8, 10, 6 ))
subcircuit.inst(Gates.CUGate(5.0063780207098425, 3.1562533916051736, 4.940217775579305, 2.419481683937988, 2, 1 ))
subcircuit.inst(Gates.CSwapGate( 10, 0, 7 ))
subcircuit.inst(Gates.PhaseGate(5.5146057452272546, 0 ))
subcircuit.inst(Gates.ECRGate( 3, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 7 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

