
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("TdgGate", "RYGate", "CUGate", "C3XGate", "HGate", "TGate", "RZGate", "CHGate", "UGate", "CSwapGate", "RXXGate", "CU1Gate", "CXGate", "CSXGate")

circuit += defns

circuit.inst(Gates.CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054, 4, 3 ))
circuit.inst(Gates.RZGate(3.1208310247400375, 6 ))
circuit.inst(Gates.RZGate(1.7510965512636645, 6 ))
circuit.inst(Gates.UGate(1.4424895697923088, 5.472664875176172, 2.66053590714238)( 0 ))
circuit.inst(Gates.C3XGate( 1, 2, 6, 5 ))
circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.CXGate( 0, 1 ))
circuit.inst(Gates.CXGate( 6, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.CXGate( 0, 1 ))
circuit.inst(Gates.CXGate( 6, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.CXGate( 6, 0 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.CXGate( 6, 0 ))
circuit.inst(Gates.CHGate( 1, 6 ))
circuit.inst(Gates.RXXGate(1.3311670849927728)( 6, 2 ))
circuit.inst(Gates.RYGate(5.99120670299654, 3 ))
circuit.inst(Gates.CUGate(5.709276284014425, 1.1243723913896708, 5.481400346001526, 3.157375188814291, 0, 6 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CSwapGate( 4, 3, 1 ))
circuit.inst(Gates.CU1Gate(4.388257530988808, 3, 4 ))
circuit.inst(Gates.CUGate(2.945697832726557, 3.322311684185455, 2.468007457013939, 1.7221796439586554, 6, 3 ))
circuit.inst(Gates.RYGate(4.206888046259435, 1 ))
circuit.inst(Gates.RZGate(5.89153421924888, 6 ))
circuit.inst(Gates.TdgGate( 4 ))
circuit.inst(Gates.RXXGate(3.9517064865019407)( 1, 6 ))

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

