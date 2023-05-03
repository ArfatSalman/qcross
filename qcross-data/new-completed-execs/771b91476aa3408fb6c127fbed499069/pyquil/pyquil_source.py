
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CSGate", "RXXGate", "CU3Gate", "U2Gate", "XGate", "CCZGate", "RZZGate", "U1Gate", "RGate", "SwapGate")

circuit += defns

circuit.inst(Gates.U1Gate(5.479758197394313, 1 ))
circuit.inst(Gates.RGate(6.143639644288786, 3.8563981362966246)( 2 ))
circuit.inst(Gates.SwapGate( 3, 5 ))
circuit.inst(Gates.CU3Gate(0.22167464109509083, 6.012192432688993, 0.4115095208941581, 5, 1 ))
circuit.inst(Gates.CCZGate( 1, 3, 0 ))
circuit.inst(Gates.U2Gate(0.9648254328971443, 2.9933536728613173)( 4 ))
circuit.inst(Gates.RXXGate(2.032522200125169)( 4, 1 ))
circuit.inst(Gates.CSGate( 3, 1 ))
circuit.inst(Gates.RGate(4.790279244293115, 5.917497614834585)( 1 ))
circuit.inst(Gates.RZZGate(1.6645038233620808)( 4, 6 ))
circuit.inst(Gates.U1Gate(0.07676574518435057, 2 ))
circuit.inst(Gates.XGate( 4 ))
circuit.inst(Gates.XGate( 2 ))

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

