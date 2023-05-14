
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("RYYGate", "ZGate", "CSwapGate", "CU1Gate", "CRXGate", "ECRGate", "SGate", "YGate", "CSXGate", "HGate", "RCCXGate", "XGate", "CUGate", "SXdgGate", "SXGate", "CRZGate", "C3XGate", "CHGate", "RZGate", "TGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.SXdgGate( 4 ))

subcircuit = Program()
subcircuit.inst(Gates.C3XGate( 4, 3, 0, 1 ))
subcircuit.inst(Gates.CSwapGate( 3, 1, 0 ))
subcircuit.inst(Gates.HGate( 3 ))
subcircuit.inst(Gates.CRXGate(5.091930552861214, 4, 3 ))
subcircuit.inst(Gates.SXGate( 3 ))
subcircuit.inst(Gates.CRZGate(2.008796895454228, 3, 2 ))
subcircuit.inst(Gates.YGate( 3 ))
subcircuit.inst(Gates.RCCXGate( 1, 0, 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 0, 3 ))
circuit.inst(Gates.ECRGate( 2, 4 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 1, 2 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 2, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 3, 4 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 3.865496458458116, 0, 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 0 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 3, 4 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 2, 3 ))

qr_31c29b = circuit.declare("qr_31c29b", "BIT", 3)

circuit += MEASURE(3, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(2, qr[3])
circuit += MEASURE(1, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

