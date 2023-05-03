
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("SXGate", "CRXGate", "RYGate", "CYGate", "CU1Gate", "ECRGate", "CSGate", "CZGate", "RXGate", "SXdgGate", "RZXGate", "CSwapGate", "CU3Gate", "CUGate", "RYYGate", "YGate", "HGate")

circuit += defns

circuit.inst(Gates.RYYGate(0.1584650651944304)( 1, 2 ))
circuit.inst(Gates.YGate( 2 ))
circuit.inst(Gates.RXGate(1.9643059251773882, 6 ))
circuit.inst(Gates.CRXGate(2.2091452154672204, 0, 6 ))
circuit.inst(Gates.CUGate(5.28444061678252, 2.26438130892656, 4.508815818648728, 5.843141721322287, 4, 0 ))
circuit.inst(Gates.RXGate(2.316480646141322, 1 ))
circuit.inst(Gates.RZXGate(1.7530034337193163)( 0, 4 ))
circuit.inst(Gates.CU1Gate(2.75818719037007, 4, 1 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.CSwapGate( 0, 4, 5 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.CU3Gate(0.29341892717166834, 6.249908353941511, 2.9247183841853848, 4, 3 ))
circuit.inst(Gates.RYGate(3.70789888536151, 5 ))
circuit.inst(Gates.CYGate( 5, 0 ))
circuit.inst(Gates.CZGate( 3, 6 ))
circuit.inst(Gates.CSGate( 3, 0 ))
circuit.inst(Gates.CSwapGate( 2, 5, 4 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.CRXGate(2.360789071411234, 3, 4 ))
circuit.inst(Gates.CZGate( 1, 0 ))
circuit.inst(Gates.RXGate(2.191505539211396, 3 ))
circuit.inst(Gates.RYYGate(0.39681210536068023)( 1, 4 ))
circuit.inst(Gates.CYGate( 4, 5 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.YGate( 0 ))
circuit.inst(Gates.CU3Gate(5.928213929259535, 1.0062255952575803, 2.115561623846294, 5, 2 ))
circuit.inst(Gates.CYGate( 1, 6 ))
circuit.inst(Gates.CZGate( 3, 0 ))
circuit.inst(Gates.ECRGate( 2, 4 ))

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





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

