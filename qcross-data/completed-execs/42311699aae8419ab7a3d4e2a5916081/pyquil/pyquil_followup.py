
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_b55b30 = circuit.declare('p_b55b30', 'REAL')
p_5d3d3d = circuit.declare('p_5d3d3d', 'REAL')
p_48d37c = circuit.declare('p_48d37c', 'REAL')
p_5d4f5c = circuit.declare('p_5d4f5c', 'REAL')
p_c95cea = circuit.declare('p_c95cea', 'REAL')
p_806bcc = circuit.declare('p_806bcc', 'REAL')
p_e6233a = circuit.declare('p_e6233a', 'REAL')
p_c8910e = circuit.declare('p_c8910e', 'REAL')
p_78f4ca = circuit.declare('p_78f4ca', 'REAL')
p_f29331 = circuit.declare('p_f29331', 'REAL')

defns = get_custom_get_definitions("RYYGate", "CSXGate", "U2Gate", "CUGate", "CU1Gate", "SdgGate", "SXGate", "XGate", "CRZGate", "C3SXGate", "CRXGate", "RZZGate", "TGate", "RZGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_806bcc, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_b55b30, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_e6233a, 1, 7 ))
circuit.inst(Gates.RZGate(p_c95cea, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(p_78f4ca, 6, 4 ))
circuit.inst(Gates.RZZGate(p_5d3d3d)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_f29331, 4 ))
circuit.inst(Gates.CRXGate(0.7279391018916035, 0, 3 ))
circuit.inst(Gates.CUGate(5.03147076606842, 5.0063780207098425, p_5d4f5c, 4.940217775579305, 6, 2 ))
circuit.inst(Gates.U2Gate(p_c8910e, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(p_48d37c)( 3, 4 ))

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
    "p_b55b30": 5.987304452123941,
    "p_5d3d3d": 5.1829934776392745,
    "p_48d37c": 3.950837470808744,
    "p_5d4f5c": 3.1562533916051736,
    "p_c95cea": 4.229610589867865,
    "p_806bcc": 6.163759533339787,
    "p_e6233a": 4.167661441102218,
    "p_c8910e": 2.5163050709890156,
    "p_78f4ca": 5.94477504571567,
    "p_f29331": 3.775592041307464
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

