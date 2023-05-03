
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("SXGate", "CRYGate", "CCZGate", "RC3XGate", "CU1Gate", "SdgGate", "RXXGate", "CCXGate", "CSGate", "ZGate", "C3SXGate", "C4XGate", "U1Gate", "CYGate", "TdgGate", "UGate")

circuit += defns

circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.RC3XGate( 9, 2, 0, 6 ))
circuit.inst(Gates.C4XGate( 5, 0, 9, 8, 6 ))
circuit.inst(Gates.UGate(3.1560639900200687, 5.736507853795902, 5.182419857278261)( 3 ))
circuit.inst(Gates.C3SXGate( 6, 3, 5, 9 ))
circuit.inst(Gates.U1Gate(5.966509081754044, 2 ))
circuit.inst(Gates.SXGate( 6 ))
circuit.inst(Gates.CU1Gate(4.213559936940442, 0, 6 ))
circuit.inst(Gates.CCZGate( 6, 5, 1 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.SXGate( 9 ))
circuit.inst(Gates.TdgGate( 6 ))
circuit.inst(Gates.CRYGate(1.543339878695638, 5, 1 ))
circuit.inst(Gates.TdgGate( 9 ))
circuit.inst(Gates.CYGate( 9, 3 ))
circuit.inst(Gates.RXXGate(3.253117584460498)( 2, 4 ))
circuit.inst(Gates.C3SXGate( 4, 3, 1, 6 ))
circuit.inst(Gates.U1Gate(4.922680836398291, 1 ))
circuit.inst(Gates.CU1Gate(4.44382187374409, 7, 4 ))
circuit.inst(Gates.CCXGate( 9, 2, 4 ))
circuit.inst(Gates.U1Gate(6.275086588388869, 9 ))
circuit.inst(Gates.CCXGate( 7, 1, 3 ))
circuit.inst(Gates.CSGate( 9, 5 ))
circuit.inst(Gates.CYGate( 1, 8 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.RXXGate(4.826421202599676)( 5, 7 ))
circuit.inst(Gates.CRYGate(0.6390825368890776, 6, 3 ))
circuit.inst(Gates.C4XGate( 9, 2, 4, 8, 7 ))

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

