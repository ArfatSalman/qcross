
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_6737bd = circuit.declare('p_6737bd', 'REAL')
p_b168d0 = circuit.declare('p_b168d0', 'REAL')
p_89415d = circuit.declare('p_89415d', 'REAL')
p_523a69 = circuit.declare('p_523a69', 'REAL')
p_9cb6f3 = circuit.declare('p_9cb6f3', 'REAL')
p_2d91b4 = circuit.declare('p_2d91b4', 'REAL')
p_c146ca = circuit.declare('p_c146ca', 'REAL')
p_a51026 = circuit.declare('p_a51026', 'REAL')
p_e5e707 = circuit.declare('p_e5e707', 'REAL')
p_7f3871 = circuit.declare('p_7f3871', 'REAL')

defns = get_custom_get_definitions("TGate", "CRZGate", "CHGate", "CCXGate", "RCCXGate", "RZZGate", "U2Gate", "XGate", "SdgGate", "CSXGate", "RZGate", "ZGate", "CU1Gate")

circuit += defns

circuit.inst(Gates.RZGate(p_c146ca, 3 ))
circuit.inst(Gates.CRZGate(p_6737bd, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.RCCXGate( 10, 6, 8 ))
circuit.inst(Gates.RZGate(p_b168d0, 0 ))
circuit.inst(Gates.CCXGate( 7, 10, 2 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.U2Gate(p_7f3871, p_9cb6f3)( 10 ))
circuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(Gates.CHGate( 0, 7 ))
circuit.inst(Gates.CU1Gate(p_523a69, 9, 0 ))
circuit.inst(Gates.RZGate(p_a51026, 6 ))
circuit.inst(Gates.U2Gate(p_2d91b4, p_e5e707)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZZGate(p_89415d)( 4, 0 ))
circuit.inst(Gates.TGate( 0 ))

qr_04780e = circuit.declare("qr_04780e", "BIT", 4)

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
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_6737bd": 4.2641612072511235,
    "p_b168d0": 4.229610589867865,
    "p_89415d": 3.950837470808744,
    "p_523a69": 4.028174522740928,
    "p_9cb6f3": 4.6235667602042065,
    "p_2d91b4": 2.5163050709890156,
    "p_c146ca": 6.163759533339787,
    "p_a51026": 5.0063780207098425,
    "p_e5e707": 2.1276323672732023,
    "p_7f3871": 4.214504315296764
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

