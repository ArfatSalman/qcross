
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("RYGate", "RZXGate", "CUGate", "HGate", "CYGate", "TGate", "CSXGate", "RZGate", "iSwapGate", "U2Gate", "CU1Gate", "CSwapGate", "CU3Gate", "CXGate")

circuit += defns

circuit.inst(Gates.CU1Gate(1.4006987211512518, 0, 2 ))
circuit.inst(Gates.CSXGate( 1, 2 ))
circuit.inst(Gates.RZGate(2.5786401929143787, 1 ))
circuit.inst(Gates.RYGate(3.1208310247400375, 0 ))
circuit.inst(Gates.CU3Gate(3.4965748481666385, 5.407902101595624, 0.6970696680696589, 0, 1 ))
circuit.inst(Gates.CSwapGate( 0, 1, 2 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.CU3Gate(3.3635160723245443, 2.227557670457083, 1.4424895697923088, 0, 2 ))
circuit.inst(Gates.RZXGate(0.4418060716084386)( 0, 1 ))
circuit.inst(Gates.CUGate(5.925227014563219, 0.21934961519025842, 2.906368483395291, 4.602208997736638, 1, 2 ))
circuit.inst(Gates.CYGate( 1, 2 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.CXGate( 0, 2 ))
circuit.inst(Gates.CXGate( 1, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.CXGate( 0, 2 ))
circuit.inst(Gates.CXGate( 1, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.CXGate( 1, 0 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.CXGate( 1, 0 ))
circuit.inst(Gates.iSwapGate( 1, 2 ))
circuit.inst(Gates.U2Gate(2.3677386437434818, 4.094703991955255)( 2 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.CU3Gate(1.3311670849927728, 3.9319327441527228, 5.390352297216399, 0, 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RYGate(5.264688008730697, 1 ))
circuit.inst(Gates.CU1Gate(5.709276284014425, 2, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

