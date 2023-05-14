
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_280a56 = circuit.declare('p_280a56', 'REAL')
p_376f59 = circuit.declare('p_376f59', 'REAL')
p_046fa5 = circuit.declare('p_046fa5', 'REAL')
p_0bfb4f = circuit.declare('p_0bfb4f', 'REAL')
p_2fed8d = circuit.declare('p_2fed8d', 'REAL')
p_bf5488 = circuit.declare('p_bf5488', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "C3SXGate", "CRXGate", "RZZGate", "RYYGate", "CU1Gate", "CUGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SdgGate", "SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_376f59, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_046fa5, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_bf5488, 1, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 6, 4 ))
circuit.inst(Gates.RZZGate(p_280a56)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(3.775592041307464, 4 ))
circuit.inst(Gates.CRXGate(0.7279391018916035, 0, 3 ))
circuit.inst(Gates.CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, p_0bfb4f, 6, 2 ))
circuit.inst(Gates.U2Gate(p_2fed8d, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))

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
    "p_280a56": 5.1829934776392745,
    "p_376f59": 6.163759533339787,
    "p_046fa5": 5.987304452123941,
    "p_0bfb4f": 4.940217775579305,
    "p_2fed8d": 2.5163050709890156,
    "p_bf5488": 4.167661441102218
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

