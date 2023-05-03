
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_28ea63 = circuit.declare('p_28ea63', 'REAL')
p_651c14 = circuit.declare('p_651c14', 'REAL')
p_3602d5 = circuit.declare('p_3602d5', 'REAL')
p_72aff8 = circuit.declare('p_72aff8', 'REAL')
p_169af4 = circuit.declare('p_169af4', 'REAL')
p_0a613b = circuit.declare('p_0a613b', 'REAL')
p_9cbb9b = circuit.declare('p_9cbb9b', 'REAL')
p_5bab06 = circuit.declare('p_5bab06', 'REAL')
p_878acf = circuit.declare('p_878acf', 'REAL')

defns = get_custom_get_definitions("CCXGate", "SdgGate", "CU1Gate", "CRZGate", "CSXGate", "U2Gate", "RZZGate", "CHGate", "XGate", "RZGate", "RCCXGate", "TGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_9cbb9b, 3 ))
circuit.inst(Gates.CRZGate(p_28ea63, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.RCCXGate( 10, 6, 8 ))
circuit.inst(Gates.RZGate(p_651c14, 0 ))
circuit.inst(Gates.CCXGate( 7, 10, 2 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.U2Gate(4.214504315296764, p_169af4)( 10 ))
circuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(Gates.CHGate( 0, 7 ))
circuit.inst(Gates.CU1Gate(p_72aff8, 9, 0 ))
circuit.inst(Gates.RZGate(p_5bab06, 6 ))
circuit.inst(Gates.U2Gate(p_0a613b, p_878acf)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZZGate(p_3602d5)( 4, 0 ))
circuit.inst(Gates.TGate( 0 ))

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
    "p_28ea63": 4.2641612072511235,
    "p_651c14": 4.229610589867865,
    "p_3602d5": 3.950837470808744,
    "p_72aff8": 4.028174522740928,
    "p_169af4": 4.6235667602042065,
    "p_0a613b": 2.5163050709890156,
    "p_9cbb9b": 6.163759533339787,
    "p_5bab06": 5.0063780207098425,
    "p_878acf": 2.1276323672732023
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

