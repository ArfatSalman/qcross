
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("RYGate", "CUGate", "TGate", "C3XGate", "CYGate", "PhaseGate", "iSwapGate", "U2Gate", "ZGate", "RXXGate", "CCXGate", "CSwapGate", "CRYGate", "RC3XGate")

circuit += defns

circuit.inst(Gates.CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054, 2, 1 ))
circuit.inst(Gates.CUGate(1.1871631023192395, 3.1208310247400375, 4.6969093516914615, 0.17758444859871442, 2, 0 ))
circuit.inst(Gates.CRYGate(0.6970696680696589, 0, 1 ))
circuit.inst(Gates.CSwapGate( 0, 3, 1 ))
circuit.inst(Gates.RYGate(1.6125723299807893, 1 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.RC3XGate( 0, 1, 2, 3 ))
circuit.inst(Gates.C3XGate( 1, 2, 0, 3 ))
circuit.inst(Gates.CRYGate(4.258547097390385, 3, 1 ))
circuit.inst(Gates.RYGate(5.620914585085149, 3 ))
circuit.inst(Gates.PhaseGate(2.3677386437434818, 3 ))
circuit.inst(Gates.RYGate(1.8882312521616809, 1 ))
circuit.inst(Gates.RYGate(3.4959547081113205, 3 ))
circuit.inst(Gates.RYGate(5.99120670299654, 3 ))
circuit.inst(Gates.iSwapGate( 1, 2 ))
circuit.inst(Gates.CUGate(5.709276284014425, 1.1243723913896708, 5.481400346001526, 3.157375188814291, 0, 1 ))
circuit.inst(Gates.PhaseGate(4.139653233556392, 3 ))
circuit.inst(Gates.CRYGate(1.9836175804480751, 3, 2 ))
circuit.inst(Gates.CSwapGate( 3, 0, 2 ))
circuit.inst(Gates.U2Gate(2.0386602682603954, 6.248470925834253)( 3 ))
circuit.inst(Gates.C3XGate( 3, 1, 0, 2 ))
circuit.inst(Gates.CUGate(2.945697832726557, 3.322311684185455, 2.468007457013939, 1.7221796439586554, 3, 0 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.RC3XGate( 1, 3, 0, 2 ))
circuit.inst(Gates.RYGate(0.8391711967546518, 3 ))
circuit.inst(Gates.CCXGate( 1, 2, 0 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.C3XGate( 1, 0, 3, 2 ))
circuit.inst(Gates.RXXGate(3.9517064865019407)( 3, 0 ))

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

