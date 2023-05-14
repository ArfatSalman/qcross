
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("CRXGate", "RYYGate", "CU3Gate", "XGate", "CRZGate", "C3XGate", "RZGate", "SXGate", "CSXGate", "ZGate", "C3SXGate", "CPhaseGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.CPhaseGate(4.63837786161633, 6, 2 ))
subcircuit.inst(Gates.SXGate( 4 ))
subcircuit.inst(Gates.C3XGate( 6, 4, 7, 2 ))
subcircuit.inst(Gates.CU3Gate(5.1829934776392745, 2.7315239782495464, 3.9984051265341463, 2, 0 ))
subcircuit.inst(Gates.SXGate( 0 ))
subcircuit.inst(Gates.CRZGate(2.008796895454228, 0, 5 ))
subcircuit.inst(Gates.CSXGate( 4, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 6, 7 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))

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

