
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CHGate", "CXGate", "HGate", "CRXGate", "PhaseGate", "iSwapGate", "XGate", "U3Gate", "DCXGate", "U1Gate", "RZZGate", "CCXGate", "SwapGate")

circuit += defns

circuit.inst(Gates.U3Gate(0.25389907280649565, 2.779350782980329, 4.0325416129476945)( 6 ))
circuit.inst(Gates.HGate( 7 ))
circuit.inst(Gates.U1Gate(0.3295500658949094, 9 ))
circuit.inst(Gates.U3Gate(3.6652643129524427, 3.6818876186109124, 2.469344104714078)( 7 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.iSwapGate( 3, 9 ))
circuit.inst(Gates.SwapGate( 0, 7 ))
circuit.inst(Gates.DCXGate( 4, 3 ))
circuit.inst(Gates.CXGate( 9, 2 ))
circuit.inst(Gates.CCXGate( 1, 6, 9 ))
circuit.inst(Gates.U1Gate(4.379482838154957, 0 ))
circuit.inst(Gates.DCXGate( 0, 2 ))
circuit.inst(Gates.CHGate( 5, 0 ))
circuit.inst(Gates.PhaseGate(3.0078842093393288, 0 ))
circuit.inst(Gates.DCXGate( 4, 6 ))
circuit.inst(Gates.CRXGate(4.021310180959978, 2, 3 ))
circuit.inst(Gates.RZZGate(1.6685155387019077)( 4, 0 ))

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

