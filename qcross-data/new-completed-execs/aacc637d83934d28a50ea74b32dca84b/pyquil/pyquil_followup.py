
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("RVGate", "SXdgGate", "CSGate", "CSdgGate", "SdgGate", "PhaseGate", "CRYGate", "U2Gate", "CPhaseGate", "iSwapGate", "XGate", "CUGate", "U1Gate", "CRZGate", "TGate")

circuit += defns

circuit.inst(Gates.CRYGate(4.682220755041814, 0, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.SdgGate( 0 ))
subcircuit.inst(Gates.SXdgGate( 0 ))
subcircuit.inst(Gates.CSGate( 1, 0 ))
subcircuit.inst(Gates.PhaseGate(5.507061057045591, 1 ))
subcircuit.inst(Gates.XGate( 0 ))
subcircuit.inst(Gates.TGate( 1 ))
subcircuit.inst(Gates.U2Gate(2.3723321578370635, 0.23310288505979176)( 1 ))
subcircuit.inst(Gates.CPhaseGate(3.5444640315452953, 0, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CUGate(5.960866266876448, 5.945098421875394, 4.418481228600101, 3.972623244718876, 1, 0 ))
circuit.inst(Gates.PhaseGate(2.031442273399285, 0 ))
circuit.inst(Gates.U1Gate(1.1449128292629545, 1 ))
circuit.inst(Gates.CRYGate(1.8638911468677428, 0, 1 ))
circuit.inst(Gates.CSdgGate( 0, 1 ))
circuit.inst(Gates.RVGate(3.2561786456517483, 4.027853623334148, 0.7501118686992972)( 1 ))
circuit.inst(Gates.PhaseGate(3.1265936864110326, 0 ))
circuit.inst(Gates.PhaseGate(2.7301494704572584, 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRZGate(2.967811594681098, 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

