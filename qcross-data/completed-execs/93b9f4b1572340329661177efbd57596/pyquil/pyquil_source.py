
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("CHGate", "CU1Gate", "RCCXGate", "SGate", "C3SXGate", "CUGate", "SXdgGate", "XGate", "iSwapGate", "RZZGate", "RZGate", "TGate", "CSXGate", "RYYGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 2 ))
circuit.inst(Gates.CU1Gate(5.154187354656876, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 2, 0 ))
circuit.inst(Gates.RCCXGate( 2, 3, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.SGate( 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

