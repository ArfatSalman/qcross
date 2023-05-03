
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("RVGate", "ZGate", "HGate", "CRXGate", "CPhaseGate", "U2Gate", "DCXGate", "SXGate", "U1Gate", "ECRGate", "TGate")

circuit += defns

circuit.inst(Gates.DCXGate( 0, 4 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.RVGate(6.18003471835015, 5.977025954690239, 2.6287210175731346)( 4 ))
circuit.inst(Gates.U1Gate(0.18970742217530903, 3 ))
circuit.inst(Gates.CPhaseGate(2.916558815706837, 2, 1 ))
circuit.inst(Gates.U2Gate(1.5787156628547458, 2.0930109781345063)( 2 ))
circuit.inst(Gates.CRXGate(5.786879734179932, 0, 3 ))
circuit.inst(Gates.CPhaseGate(4.358574517050474, 3, 2 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.U1Gate(2.950818625000669, 0 ))
circuit.inst(Gates.CPhaseGate(1.6476787886644708, 2, 0 ))
circuit.inst(Gates.ECRGate( 2, 4 ))
circuit.inst(Gates.CPhaseGate(4.051497867526455, 4, 3 ))
circuit.inst(Gates.SXGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

