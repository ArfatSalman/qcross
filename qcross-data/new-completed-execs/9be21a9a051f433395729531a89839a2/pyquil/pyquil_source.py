
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("RVGate", "CHGate", "RXXGate", "IGate", "XGate", "CCZGate", "CUGate", "SXGate", "U1Gate", "YGate", "RGate", "CCXGate", "SGate", "SwapGate")

circuit += defns

circuit.inst(Gates.RVGate(5.730485179497036, 5.1815317617582535, 4.954506343035782)( 0 ))
circuit.inst(Gates.U1Gate(5.5351729304729, 6 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.RXXGate(1.620673138384231)( 1, 4 ))
circuit.inst(Gates.SwapGate( 0, 3 ))
circuit.inst(Gates.CUGate(2.5179284740661867, 4.218025714484969, 5.538801185807778, 0.2277932967359332, 4, 5 ))
circuit.inst(Gates.SXGate( 3 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.RGate(2.373112537407949, 2.0806292204834302)( 1 ))
circuit.inst(Gates.CCZGate( 4, 1, 5 ))
circuit.inst(Gates.YGate( 4 ))
circuit.inst(Gates.RGate(1.3139288690051985, 5.834685188574328)( 6 ))
circuit.inst(Gates.CCZGate( 2, 5, 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.U1Gate(0.5163920678872455, 5 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 4, 0, 5 ))

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

