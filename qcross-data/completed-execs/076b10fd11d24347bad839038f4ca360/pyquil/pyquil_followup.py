
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_925c46 = circuit.declare('p_925c46', 'REAL')
p_b15ae8 = circuit.declare('p_b15ae8', 'REAL')
p_a28ef6 = circuit.declare('p_a28ef6', 'REAL')
p_40ca7b = circuit.declare('p_40ca7b', 'REAL')
p_26612a = circuit.declare('p_26612a', 'REAL')
p_0b1992 = circuit.declare('p_0b1992', 'REAL')
p_e50c6e = circuit.declare('p_e50c6e', 'REAL')
p_01d286 = circuit.declare('p_01d286', 'REAL')
p_635d83 = circuit.declare('p_635d83', 'REAL')
p_8885ef = circuit.declare('p_8885ef', 'REAL')
p_60901c = circuit.declare('p_60901c', 'REAL')
p_2c0ff7 = circuit.declare('p_2c0ff7', 'REAL')
p_97cf30 = circuit.declare('p_97cf30', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "U2Gate", "ZGate", "CU1Gate", "RZZGate", "CRZGate", "XGate", "RZGate", "SdgGate", "CSXGate", "TGate", "CHGate", "SXdgGate", "CCXGate", "ECRGate", "DCXGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.ECRGate( 2, 5 ))
subcircuit.inst(Gates.RZGate(p_0b1992, 1 ))
subcircuit.inst(Gates.DCXGate( 0, 5 ))
subcircuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(p_e50c6e, 3 ))
circuit.inst(Gates.CRZGate(p_635d83, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.RCCXGate( 10, 6, 8 ))
circuit.inst(Gates.RZGate(p_60901c, 0 ))
circuit.inst(Gates.CCXGate( 7, 10, 2 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.U2Gate(p_01d286, p_2c0ff7)( 10 ))
circuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(Gates.CHGate( 0, 7 ))
circuit.inst(Gates.CU1Gate(p_a28ef6, 9, 0 ))
circuit.inst(Gates.RZGate(p_26612a, 6 ))
circuit.inst(Gates.U2Gate(p_97cf30, p_925c46)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZZGate(p_b15ae8)( 4, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(Gates.RZGate(p_8885ef, 2 ))
circuit.inst(Gates.CRZGate(p_40ca7b, 5, 3 ))

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
    "p_925c46": 2.1276323672732023,
    "p_b15ae8": 3.950837470808744,
    "p_a28ef6": 4.028174522740928,
    "p_40ca7b": 0.6393443962862078,
    "p_26612a": 5.0063780207098425,
    "p_0b1992": 3.3407994338317226,
    "p_e50c6e": 6.163759533339787,
    "p_01d286": 4.214504315296764,
    "p_635d83": 4.2641612072511235,
    "p_8885ef": 4.722103101046168,
    "p_60901c": 4.229610589867865,
    "p_2c0ff7": 4.6235667602042065,
    "p_97cf30": 2.5163050709890156
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

