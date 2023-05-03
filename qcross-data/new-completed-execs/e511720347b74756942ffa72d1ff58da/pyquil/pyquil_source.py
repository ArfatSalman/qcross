
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("CRYGate", "U2Gate", "CSdgGate", "SGate", "U1Gate", "RXXGate", "RZGate", "U3Gate", "CCXGate", "CSwapGate", "CZGate", "CU3Gate", "C3SXGate", "CUGate", "SXGate", "CYGate", "RGate", "RVGate")

circuit += defns

circuit.inst(Gates.CYGate( 1, 3 ))
circuit.inst(Gates.CSdgGate( 2, 0 ))
circuit.inst(Gates.U2Gate(6.224224267022873, 0.5062108542599196)( 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.RXXGate(2.849709666292305)( 2, 0 ))
circuit.inst(Gates.CUGate(1.4830756139727388, 4.336270484416077, 4.496803337305518, 0.23255854856360128, 2, 0 ))
circuit.inst(Gates.U1Gate(3.989772590171974, 2 ))
circuit.inst(Gates.RVGate(2.3749233592982653, 1.242766903811508, 5.902936157186667)( 1 ))
circuit.inst(Gates.CCXGate( 2, 1, 3 ))
circuit.inst(Gates.RGate(5.3389684124335135, 4.983335490773843)( 0 ))
circuit.inst(Gates.CU3Gate(2.9985355066762964, 4.6584355985305175, 5.286009370798176, 1, 2 ))
circuit.inst(Gates.U1Gate(1.23766565597922, 1 ))
circuit.inst(Gates.CRYGate(0.7050339438266124, 3, 0 ))
circuit.inst(Gates.CU3Gate(0.26880077817102677, 4.703772321262758, 2.2003352220865064, 0, 3 ))
circuit.inst(Gates.RXXGate(1.7988659594922651)( 1, 3 ))
circuit.inst(Gates.CZGate( 3, 2 ))
circuit.inst(Gates.U1Gate(3.091046473463947, 2 ))
circuit.inst(Gates.CU3Gate(4.07826629550777, 0.6948315212195522, 3.971785158778898, 1, 0 ))
circuit.inst(Gates.RZGate(6.114994939448648, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.U1Gate(3.885678856232139, 1 ))
circuit.inst(Gates.U3Gate(1.3122881955531616, 0.33578911439943154, 4.332701855049643)( 1 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CSwapGate( 3, 0, 1 ))
circuit.inst(Gates.CZGate( 3, 2 ))
circuit.inst(Gates.U3Gate(0.07989271098060978, 3.2475433527931767, 3.3028156122014454)( 0 ))

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

