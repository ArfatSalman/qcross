
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("CRZGate", "RZXGate", "C3SXGate", "CRXGate", "CU1Gate", "CUGate", "RZGate", "TGate", "ZGate", "CZGate", "CCXGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.CZGate( 1, 4 ))
subcircuit.inst(Gates.CRXGate(4.736752714049485, 0, 4 ))
subcircuit.inst(Gates.CU1Gate(4.501598818751339, 2, 5 ))
subcircuit.inst(Gates.CZGate( 1, 0 ))
subcircuit.inst(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547, 0, 3 ))
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.RZXGate(4.563562108824195)( 4, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

