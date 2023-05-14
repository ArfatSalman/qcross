
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_2e68f3 = circuit.declare('p_2e68f3', 'REAL')
p_f3b6b3 = circuit.declare('p_f3b6b3', 'REAL')
p_02e0d1 = circuit.declare('p_02e0d1', 'REAL')
p_bdd144 = circuit.declare('p_bdd144', 'REAL')
p_031c73 = circuit.declare('p_031c73', 'REAL')
p_9bff3f = circuit.declare('p_9bff3f', 'REAL')
p_d48307 = circuit.declare('p_d48307', 'REAL')
p_cbf48f = circuit.declare('p_cbf48f', 'REAL')

defns = get_custom_get_definitions("CRZGate", "CSXGate", "TGate", "U2Gate", "ZGate", "XGate", "RZGate", "SdgGate", "RZZGate", "RYYGate", "RCCXGate", "CU1Gate", "ECRGate", "CHGate", "CRXGate", "SGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_02e0d1, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_2e68f3, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_d48307, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 4, 6 ))
circuit.inst(Gates.CHGate( 4, 0 ))
circuit.inst(Gates.C3SXGate( 2, 0, 3, 4 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CRZGate(p_bdd144, 0, 6 ))
circuit.inst(Gates.CU1Gate(p_9bff3f, 1, 4 ))
circuit.inst(Gates.C3SXGate( 2, 0, 5, 4 ))
circuit.inst(Gates.CRZGate(p_f3b6b3, 6, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, p_cbf48f)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 3, 4 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RYYGate(p_031c73)( 4, 2 ))

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



params = {
    "p_2e68f3": 4.229610589867865,
    "p_f3b6b3": 2.586208953975239,
    "p_02e0d1": 6.163759533339787,
    "p_bdd144": 4.833923139882297,
    "p_031c73": 1.9669252191306448,
    "p_9bff3f": 4.028174522740928,
    "p_d48307": 3.2142159669963557,
    "p_cbf48f": 2.1276323672732023
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        


quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

