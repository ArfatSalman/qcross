
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("C3XGate", "UGate", "CU3Gate", "CUGate", "CRXGate", "RCCXGate", "SdgGate", "ECRGate", "CZGate", "RXGate", "DCXGate", "RC3XGate", "C3SXGate", "CYGate", "SGate", "RXXGate", "ZGate", "SXGate")

circuit += defns

circuit.inst(Gates.CYGate( 9, 3 ))
circuit.inst(Gates.CRXGate(3.006996712679364, 0, 9 ))
circuit.inst(Gates.RXXGate(6.231728094077643)( 0, 1 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CUGate(5.402681630107685, 5.7320803489582755, 1.5504227913558584, 6.117533666092848, 1, 4 ))
circuit.inst(Gates.CZGate( 0, 8 ))
circuit.inst(Gates.C3XGate( 7, 5, 0, 1 ))
circuit.inst(Gates.CYGate( 6, 9 ))
circuit.inst(Gates.CUGate(1.9776456095905999, 2.7856733477756688, 2.3725791317893616, 4.281289624237246, 4, 1 ))
circuit.inst(Gates.C3SXGate( 5, 3, 8, 2 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.DCXGate( 6, 1 ))
circuit.inst(Gates.RXGate(2.7622901582617536, 2 ))
circuit.inst(Gates.RCCXGate( 7, 0, 4 ))
circuit.inst(Gates.UGate(5.093998211740766, 4.1763972388782795, 1.3446658688471513)( 1 ))

subcircuit = Program()
subcircuit.inst(Gates.ECRGate( 3, 9 ))
subcircuit.inst(Gates.RC3XGate( 2, 4, 7, 9 ))
subcircuit.inst(Gates.CU3Gate(3.1029941305253375, 2.467778988525628, 0.806315267571145, 0, 2 ))
subcircuit.inst(Gates.SXGate( 6 ))
subcircuit.inst(Gates.SXGate( 8 ))
subcircuit.inst(Gates.CU3Gate(2.0260479577768926, 1.6908888602654353, 4.870531090171869, 3, 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CYGate( 5, 6 ))
circuit.inst(Gates.UGate(3.2780013517483826, 1.092359559443437, 2.5802478164404428)( 0 ))
circuit.inst(Gates.CUGate(5.627192099540417, 2.1947268632429866, 5.888372357253659, 1.16349884234323, 3, 4 ))
circuit.inst(Gates.CYGate( 0, 5 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.RCCXGate( 4, 0, 1 ))

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



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

