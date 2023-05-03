
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("CCZGate", "RC3XGate", "CU1Gate", "CRXGate", "CSdgGate", "CYGate", "CUGate", "CHGate", "SXdgGate", "RVGate", "YGate", "CRZGate", "RYYGate", "DCXGate", "CU3Gate", "IGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RYYGate(4.230538610152256)( 3, 8 ))
circuit.inst(Gates.CRXGate(3.3203084344733997, 2, 3 ))
circuit.inst(Gates.CRXGate(4.622916213622228, 6, 8 ))
circuit.inst(Gates.C3SXGate( 8, 2, 6, 1 ))
circuit.inst(Gates.CRZGate(2.3252143484585774, 4, 8 ))
circuit.inst(Gates.CU3Gate(3.9779731506025207, 1.8692602791557653, 3.52092355767973, 0, 7 ))
circuit.inst(Gates.CSdgGate( 5, 7 ))
circuit.inst(Gates.C3SXGate( 6, 1, 8, 4 ))
circuit.inst(Gates.CYGate( 8, 5 ))
circuit.inst(Gates.CU1Gate(6.092983263138358, 6, 8 ))
circuit.inst(Gates.DCXGate( 2, 1 ))
circuit.inst(Gates.CRZGate(0.2732434042738512, 2, 8 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CYGate( 3, 4 ))
circuit.inst(Gates.CSdgGate( 5, 2 ))
circuit.inst(Gates.CYGate( 0, 5 ))
circuit.inst(Gates.CUGate(1.3294053085361235, 1.6134324891544933, 1.3668738903035305, 2.2614780495462785, 1, 6 ))
circuit.inst(Gates.CHGate( 6, 8 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.RC3XGate( 1, 7, 0, 8 ))
circuit.inst(Gates.RVGate(4.325005000959295, 1.4884924689724215, 2.122323708296557)( 6 ))
circuit.inst(Gates.CUGate(4.129509958864599, 2.661313282317246, 3.471286270687046, 3.3400786207701714, 2, 5 ))
circuit.inst(Gates.CUGate(5.55653769076178, 4.605056011495016, 0.9700427538550028, 1.9703735803987805, 8, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.C3SXGate( 1, 3, 5, 2 ))
circuit.inst(Gates.CCZGate( 1, 5, 0 ))
circuit.inst(Gates.CSdgGate( 3, 8 ))

circuit += MEASURE(5, qr[0])
circuit += MEASURE(0, qr[1])
circuit += MEASURE(8, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(1, qr[4])
circuit += MEASURE(7, qr[5])
circuit += MEASURE(4, qr[6])
circuit += MEASURE(2, qr[7])
circuit += MEASURE(6, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

