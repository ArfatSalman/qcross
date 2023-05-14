
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("ZGate", "RZGate", "TGate", "ECRGate", "C3SXGate", "CRXGate", "U2Gate", "CZGate", "U1Gate", "CU3Gate", "XGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))

subcircuit = Program()
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.CZGate( 1, 0 ))
subcircuit.inst(Gates.CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789, 2, 5 ))
subcircuit.inst(Gates.CZGate( 0, 1 ))
subcircuit.inst(Gates.U1Gate(6.2047416485134805, 0 ))
subcircuit.inst(Gates.ECRGate( 3, 0 ))
subcircuit.inst(Gates.U2Gate(5.887184334931191, 0.07157463504881167)( 6 ))
subcircuit.inst(Gates.CU3Gate(5.1829934776392745, 2.7315239782495464, 3.9984051265341463, 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

