
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_aab82c = circuit.declare('p_aab82c', 'REAL')
p_61e37c = circuit.declare('p_61e37c', 'REAL')
p_3f39bf = circuit.declare('p_3f39bf', 'REAL')
p_e66f86 = circuit.declare('p_e66f86', 'REAL')
p_d9b3b7 = circuit.declare('p_d9b3b7', 'REAL')
p_58380b = circuit.declare('p_58380b', 'REAL')
p_4bf6d4 = circuit.declare('p_4bf6d4', 'REAL')
p_457d2e = circuit.declare('p_457d2e', 'REAL')
p_dc6a99 = circuit.declare('p_dc6a99', 'REAL')
p_2fe099 = circuit.declare('p_2fe099', 'REAL')
p_b5cb9c = circuit.declare('p_b5cb9c', 'REAL')
p_251638 = circuit.declare('p_251638', 'REAL')
p_f86d7f = circuit.declare('p_f86d7f', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXGate", "TGate", "U2Gate", "ZGate", "XGate", "RZGate", "CUGate", "RZZGate", "SdgGate", "CU1Gate", "RYYGate", "CRXGate", "CSXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_58380b, 0, 6 ))
circuit.inst(Gates.CRZGate(p_f86d7f, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_b5cb9c)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_3f39bf, 1, 7 ))
circuit.inst(Gates.RZGate(p_aab82c, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_4bf6d4, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 6, 4 ))
circuit.inst(Gates.RZZGate(p_251638)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(3.775592041307464, 4 ))
circuit.inst(Gates.CRXGate(p_dc6a99, 0, 3 ))
circuit.inst(Gates.CUGate(p_457d2e, p_d9b3b7, p_2fe099, p_e66f86, 6, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, p_61e37c)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(3.950837470808744)( 3, 4 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RYYGate(1.9669252191306448)( 4, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_aab82c": 4.229610589867865,
    "p_61e37c": 2.1276323672732023,
    "p_3f39bf": 4.167661441102218,
    "p_e66f86": 4.940217775579305,
    "p_d9b3b7": 5.0063780207098425,
    "p_58380b": 5.987304452123941,
    "p_4bf6d4": 3.2142159669963557,
    "p_457d2e": 5.03147076606842,
    "p_dc6a99": 0.7279391018916035,
    "p_2fe099": 3.1562533916051736,
    "p_b5cb9c": 1.740253089260498,
    "p_251638": 5.1829934776392745,
    "p_f86d7f": 1.0296448789776642
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

