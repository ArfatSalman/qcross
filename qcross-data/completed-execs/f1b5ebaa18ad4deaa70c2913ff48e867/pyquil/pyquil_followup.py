
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("RXXGate", "TGate", "SXGate", "CSXGate", "CRXGate", "CYGate", "CCXGate", "ZGate", "XGate", "RCCXGate", "TdgGate", "DCXGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 9, 4 ))

subcircuit = Program()
subcircuit.inst(Gates.TdgGate( 2 ))
subcircuit.inst(Gates.CYGate( 5, 2 ))
subcircuit.inst(Gates.SXGate( 8 ))
subcircuit.inst(Gates.CRZGate(2.008796895454228, 8, 6 ))
subcircuit.inst(Gates.RCCXGate( 3, 7, 1 ))
subcircuit.inst(Gates.RXXGate(5.25962645863375)( 2, 9 ))
subcircuit.inst(Gates.DCXGate( 5, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(5.987304452123941, 7, 0 ))
circuit.inst(Gates.CCXGate( 6, 3, 0 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 7, 9 ))
circuit.inst(Gates.RZGate(4.229610589867865, 7 ))
circuit.inst(Gates.SXGate( 5 ))
circuit.inst(Gates.CSXGate( 2, 1 ))

qr_b0b0b7 = circuit.declare("qr_b0b0b7", "BIT", 8)

circuit += MEASURE(8, qr[0])
circuit += MEASURE(7, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(4, qr[3])
circuit += MEASURE(2, qr[4])
circuit += MEASURE(6, qr[5])
circuit += MEASURE(9, qr[6])
circuit += MEASURE(0, qr[7])
circuit += MEASURE(1, qr[8])
circuit += MEASURE(3, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

