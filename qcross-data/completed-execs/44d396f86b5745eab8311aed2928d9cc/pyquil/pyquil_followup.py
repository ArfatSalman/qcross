
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("C3SXGate", "CCXGate", "ZGate", "RXXGate", "CSwapGate", "RZGate", "SXGate", "TGate", "CRZGate", "CSXGate", "DCXGate", "RCCXGate", "XGate", "PhaseGate", "CRXGate", "ECRGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))

subcircuit = Program()
subcircuit.inst(Gates.CSwapGate( 0, 5, 4 ))
subcircuit.inst(Gates.RCCXGate( 9, 1, 8 ))
subcircuit.inst(Gates.RXXGate(5.25962645863375)( 4, 6 ))
subcircuit.inst(Gates.DCXGate( 2, 7 ))
subcircuit.inst(Gates.ECRGate( 2, 0 ))
subcircuit.inst(Gates.PhaseGate(5.5146057452272546, 0 ))
subcircuit.inst(Gates.ECRGate( 3, 4 ))
subcircuit.inst(Gates.PhaseGate(0.4827903095199283, 8 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 0, 2 ))

qr_a1bb74 = circuit.declare("qr_a1bb74", "BIT", 9)

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




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

