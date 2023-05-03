
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("RVGate", "CU1Gate", "CSwapGate", "RC3XGate", "ZGate", "HGate", "CRXGate", "PhaseGate", "U2Gate", "RYGate", "IGate", "XGate", "CSXGate", "ECRGate", "CRZGate", "SGate")

circuit += defns

circuit.inst(Gates.CSwapGate( 0, 9, 7 ))
circuit.inst(Gates.PhaseGate(3.343442682560371, 0 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.HGate( 5 ))
circuit.inst(Gates.CRZGate(3.2858177251722944, 9, 7 ))
circuit.inst(Gates.RVGate(1.6270903792852736, 1.0744526495059412, 3.7558505518080576)( 3 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.U2Gate(0.5159858283914562, 3.092014702746218)( 6 ))
circuit.inst(Gates.RVGate(5.944576757265284, 5.021353132730173, 4.714404259070525)( 0 ))
circuit.inst(Gates.RC3XGate( 0, 1, 7, 2 ))
circuit.inst(Gates.ZGate( 9 ))
circuit.inst(Gates.CRXGate(1.0327406277155489, 4, 6 ))
circuit.inst(Gates.CRZGate(3.051239290740801, 1, 0 ))
circuit.inst(Gates.ECRGate( 5, 4 ))
circuit.inst(Gates.RYGate(5.127275071501011, 8 ))
circuit.inst(Gates.IGate( 5 ))
circuit.inst(Gates.CSXGate( 3, 7 ))
circuit.inst(Gates.CRZGate(1.6690058311460272, 7, 2 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRZGate(1.620800307377981, 1, 5 ))
circuit.inst(Gates.CU1Gate(0.4967177059820002, 0, 7 ))

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

