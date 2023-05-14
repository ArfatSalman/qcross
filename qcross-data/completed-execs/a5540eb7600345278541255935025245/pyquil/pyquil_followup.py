
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CRZGate", "TGate", "SwapGate", "RZGate", "RCCXGate", "C3SXGate", "SXdgGate", "ZGate", "iSwapGate", "CHGate", "U2Gate", "XGate", "CU1Gate", "RYYGate", "CSXGate", "SGate", "SdgGate", "CCXGate", "RZZGate", "ECRGate", "CRXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
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

subcircuit = Program()
subcircuit.inst(Gates.SwapGate( 1, 3 ))
subcircuit.inst(Gates.TGate( 1 ))
subcircuit.inst(Gates.iSwapGate( 3, 6 ))
subcircuit.inst(Gates.CHGate( 2, 0 ))
subcircuit.inst(Gates.SXdgGate( 6 ))
subcircuit.inst(Gates.CCXGate( 5, 3, 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(4.833923139882297, 0, 6 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 1, 4 ))
circuit.inst(Gates.C3SXGate( 2, 0, 5, 4 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 6, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 3, 4 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RYYGate(1.9669252191306448)( 4, 2 ))

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

