
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("U2Gate", "CU3Gate", "CUGate", "RYGate", "RZZGate", "TdgGate", "CRYGate", "U3Gate", "U1Gate", "CSXGate", "CYGate", "IGate", "SXdgGate", "YGate", "XGate")

circuit += defns

circuit.inst(Gates.U3Gate(0.7525107922079248, 1.2447972626729948, 5.921099882361809)( 2 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.CU3Gate(3.5951128532694563, 0.010919193816599988, 3.645329450090628, 0, 2 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.U2Gate(2.2781042293610834, 2.8111390321344745)( 1 ))
circuit.inst(Gates.IGate( 0 ))
circuit.inst(Gates.CRYGate(5.388940796049925, 1, 2 ))
circuit.inst(Gates.U2Gate(5.5431459174826, 1.3400715972886643)( 0 ))
circuit.inst(Gates.TdgGate( 1 ))
circuit.inst(Gates.U2Gate(0.15471247054287984, 2.4400424648148045)( 1 ))
circuit.inst(Gates.YGate( 0 ))
circuit.inst(Gates.RZZGate(5.7575659278310845)( 0, 2 ))
circuit.inst(Gates.U1Gate(1.4699956697302532, 1 ))
circuit.inst(Gates.CUGate(1.0304702852384158, 2.6685497827460365, 3.99549985610294, 5.662035192382266, 1, 2 ))
circuit.inst(Gates.CRYGate(3.4267977136464998, 1, 2 ))
circuit.inst(Gates.CYGate( 0, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.TdgGate( 0 ))
circuit.inst(Gates.RYGate(3.7754558724472616, 1 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.U3Gate(6.01948050450523, 2.72714859557862, 3.399676447189968)( 0 ))
circuit.inst(Gates.RZZGate(0.3954282502495691)( 0, 2 ))
circuit.inst(Gates.U3Gate(1.9629138136015831, 3.495764555095602, 4.032386816161946)( 2 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.CU3Gate(3.8725614355577274, 3.7233769818737543, 0.6129863346305541, 0, 1 ))
circuit.inst(Gates.U1Gate(2.410525914389015, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.TdgGate( 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

