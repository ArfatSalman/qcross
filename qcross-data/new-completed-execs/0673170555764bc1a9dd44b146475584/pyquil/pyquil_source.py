
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CSGate", "CU3Gate", "CSdgGate", "CRXGate", "PhaseGate", "RYYGate", "RCCXGate", "CCZGate", "CUGate", "CSXGate", "CZGate", "U1Gate", "CRZGate", "RZZGate", "TGate")

circuit += defns

circuit.inst(Gates.RZZGate(3.138388361681893)( 1, 0 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.U1Gate(0.396418175987844, 9 ))
circuit.inst(Gates.CRZGate(5.16452425350899, 1, 4 ))
circuit.inst(Gates.CRXGate(3.0664993083734644, 6, 2 ))
circuit.inst(Gates.RCCXGate( 4, 1, 8 ))
circuit.inst(Gates.CSGate( 8, 6 ))
circuit.inst(Gates.CCZGate( 3, 7, 9 ))
circuit.inst(Gates.CU3Gate(2.8185804779007992, 5.261790461945118, 2.326141806696294, 1, 4 ))
circuit.inst(Gates.CZGate( 3, 8 ))
circuit.inst(Gates.CSdgGate( 3, 4 ))
circuit.inst(Gates.CUGate(3.522950755972168, 4.8949869688966565, 1.528172084251171, 3.5827113474296604, 8, 5 ))
circuit.inst(Gates.RCCXGate( 3, 5, 7 ))
circuit.inst(Gates.CSXGate( 6, 8 ))
circuit.inst(Gates.RCCXGate( 6, 4, 7 ))
circuit.inst(Gates.RYYGate(4.484588825647207)( 4, 5 ))
circuit.inst(Gates.U1Gate(6.019643147584277, 0 ))
circuit.inst(Gates.PhaseGate(5.38252061225771, 7 ))

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

