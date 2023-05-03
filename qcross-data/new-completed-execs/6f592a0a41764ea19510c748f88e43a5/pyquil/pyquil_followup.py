
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("CZGate", "IGate", "RGate", "CPhaseGate", "RZXGate", "CU3Gate", "PhaseGate", "SXGate", "YGate", "HGate", "U2Gate", "SwapGate", "CRYGate", "U3Gate", "CRXGate", "ZGate", "CHGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.CPhaseGate(3.5690023406020117, 1, 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CRXGate(0.5834164558695757, 1, 0 ))
circuit.inst(Gates.PhaseGate(3.894930545586774, 0 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CZGate( 0, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.U2Gate(5.482574947566191, 0.8373110034524618)( 0 ))
circuit.inst(Gates.PhaseGate(0.3578418944802631, 1 ))
circuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.CPhaseGate(5.397112728340784, 1, 0 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRYGate(1.174494077676677, 0, 1 ))
circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.YGate( 0 ))
circuit.inst(Gates.RGate(2.8467414627241734, 3.5481884646507713)( 1 ))
circuit.inst(Gates.RZXGate(3.2681088907886817)( 1, 0 ))
circuit.inst(Gates.CRYGate(5.6914225992075504, 0, 1 ))
circuit.inst(Gates.U3Gate(4.266994303739899, 1.914216390388542, 1.0614410494494415)( 1 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.CU3Gate(0.6949120689264752, 0.9164071466076199, 5.136397164125832, 0, 1 ))
circuit.inst(Gates.CRYGate(2.843774029250561, 1, 0 ))
circuit.inst(Gates.CU3Gate(0.6994648472584757, 3.50667959618503, 5.986466284185033, 1, 0 ))
circuit.inst(Gates.SXGate( 0 ))

circuit += MEASURE(1, qr[0])
circuit += MEASURE(0, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

