
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("IGate", "RZZGate", "RC3XGate", "XGate", "CU1Gate", "SdgGate", "RXGate", "CRYGate", "U1Gate", "RYGate", "PhaseGate", "DCXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RC3XGate( 9, 6, 0, 2 ))
circuit.inst(Gates.PhaseGate(6.09316043121222, 7 ))
circuit.inst(Gates.CHGate( 3, 9 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.CU1Gate(3.0503162741407537, 8, 6 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.U1Gate(5.75020155959207, 3 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.IGate( 6 ))
circuit.inst(Gates.RYGate(6.135776937038943, 5 ))
circuit.inst(Gates.RXGate(0.5846665175165219, 2 ))
circuit.inst(Gates.DCXGate( 0, 5 ))
circuit.inst(Gates.RZZGate(5.985328734366836)( 0, 8 ))
circuit.inst(Gates.CRYGate(2.033688313756901, 8, 7 ))
circuit.inst(Gates.SdgGate( 6 ))

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

