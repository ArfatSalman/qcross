
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("SXdgGate", "RXXGate", "CU3Gate", "HGate", "CPhaseGate", "CRYGate", "RCCXGate", "XGate", "iSwapGate", "CCZGate", "CUGate", "U1Gate", "ECRGate")

circuit += defns

circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRYGate(2.4498821250483043, 10, 9 ))

subcircuit = Program()
subcircuit.inst(Gates.CPhaseGate(5.94833048963124, 6, 3 ))
subcircuit.inst(Gates.RCCXGate( 2, 9, 4 ))
subcircuit.inst(Gates.CCZGate( 2, 9, 5 ))
subcircuit.inst(Gates.SXdgGate( 4 ))
subcircuit.inst(Gates.iSwapGate( 0, 6 ))
subcircuit.inst(Gates.U1Gate(4.170850588142773, 6 ))
subcircuit.inst(Gates.CUGate(3.6349610195058815, 3.819623549514622, 1.4862870686636986, 3.4327806393198337, 3, 6 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.CPhaseGate(3.3516599839543195, 4, 3 ))
circuit.inst(Gates.ECRGate( 5, 8 ))
circuit.inst(Gates.CU3Gate(5.423661738344168, 1.2257558063112008, 4.146906161622092, 1, 8 ))
circuit.inst(Gates.RXXGate(0.4988271119481185)( 7, 0 ))

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

