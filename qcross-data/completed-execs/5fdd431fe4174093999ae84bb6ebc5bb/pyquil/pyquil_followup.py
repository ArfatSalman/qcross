
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("CHGate", "ZGate", "RZGate", "XGate", "SXdgGate", "SXGate", "SGate", "SdgGate", "C3SXGate", "CRYGate", "CU1Gate", "CUGate", "CSXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 5 ))
circuit.inst(Gates.CSXGate( 8, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 2, 7 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.C3SXGate( 2, 5, 1, 6 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SGate( 5 ))

subcircuit = Program()
subcircuit.inst(Gates.CRYGate(3.1402006997068588, 8, 2 ))
subcircuit.inst(Gates.SXdgGate( 7 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 0, 3, 8, 2 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 5, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 6, 5 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.CSXGate( 2, 8 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CHGate( 7, 0 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(8, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(6, qr[5])
circuit += MEASURE(7, qr[6])
circuit += MEASURE(1, qr[7])
circuit += MEASURE(5, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

