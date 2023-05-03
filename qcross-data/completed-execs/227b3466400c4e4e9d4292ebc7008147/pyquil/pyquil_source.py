
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("CZGate", "U3Gate", "U2Gate", "CYGate", "RXXGate", "CHGate", "YGate", "PhaseGate", "HGate", "RZZGate", "TdgGate", "CU3Gate", "SXdgGate", "U1Gate", "SXGate")

circuit += defns

circuit.inst(Gates.TdgGate( 0 ))
circuit.inst(Gates.PhaseGate(1.3428862289262922, 0 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CU3Gate(4.165123907650545, 2.6766240976228306, 5.851109164020841, 1, 0 ))
circuit.inst(Gates.CZGate( 0, 1 ))
circuit.inst(Gates.U3Gate(3.1124943003575862, 5.033907753688158, 3.427635111293556)( 1 ))
circuit.inst(Gates.RZZGate(5.9643464495294385)( 0, 1 ))
circuit.inst(Gates.U1Gate(3.005113685069328, 0 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.PhaseGate(0.3147213681222795, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.YGate( 0 ))
circuit.inst(Gates.U3Gate(0.6932622610946984, 0.5005689189307869, 3.802023333380939)( 1 ))
circuit.inst(Gates.CZGate( 0, 1 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.U2Gate(1.5441062376251906, 1.6281357791932107)( 0 ))
circuit.inst(Gates.CYGate( 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.PhaseGate(3.369665394386499, 1 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.U1Gate(2.7233411978459645, 0 ))
circuit.inst(Gates.YGate( 0 ))
circuit.inst(Gates.RXXGate(4.459276651579209)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

