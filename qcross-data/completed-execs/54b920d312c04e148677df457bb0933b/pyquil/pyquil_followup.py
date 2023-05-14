
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 8)

p_097544 = circuit.declare('p_097544', 'REAL')
p_6bf657 = circuit.declare('p_6bf657', 'REAL')
p_cda6ce = circuit.declare('p_cda6ce', 'REAL')
p_74776f = circuit.declare('p_74776f', 'REAL')
p_45ab98 = circuit.declare('p_45ab98', 'REAL')
p_814b0e = circuit.declare('p_814b0e', 'REAL')
p_2092b7 = circuit.declare('p_2092b7', 'REAL')
p_9cf47d = circuit.declare('p_9cf47d', 'REAL')
p_2a789a = circuit.declare('p_2a789a', 'REAL')
p_f9d44b = circuit.declare('p_f9d44b', 'REAL')
p_a08081 = circuit.declare('p_a08081', 'REAL')
p_6b1e96 = circuit.declare('p_6b1e96', 'REAL')
p_e59b9b = circuit.declare('p_e59b9b', 'REAL')

defns = get_custom_get_definitions("XGate", "CRZGate", "RYYGate", "CU1Gate", "RZZGate", "ZGate", "CRXGate", "SXGate", "U2Gate", "CUGate", "TGate", "CSXGate", "RZGate", "C3SXGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_6bf657, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_cda6ce, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_f9d44b)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_814b0e, 1, 7 ))
circuit.inst(Gates.RZGate(p_e59b9b, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_2092b7, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 6, 4 ))
circuit.inst(Gates.RZZGate(p_097544)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_6b1e96, 4 ))
circuit.inst(Gates.CRXGate(p_9cf47d, 0, 3 ))
circuit.inst(Gates.CUGate(p_2a789a, p_74776f, 3.1562533916051736, p_a08081, 6, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, p_45ab98)( 2 ))
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
    "p_097544": 5.1829934776392745,
    "p_6bf657": 6.163759533339787,
    "p_cda6ce": 5.987304452123941,
    "p_74776f": 5.0063780207098425,
    "p_45ab98": 2.1276323672732023,
    "p_814b0e": 4.167661441102218,
    "p_2092b7": 3.2142159669963557,
    "p_9cf47d": 0.7279391018916035,
    "p_2a789a": 5.03147076606842,
    "p_f9d44b": 1.740253089260498,
    "p_a08081": 4.940217775579305,
    "p_6b1e96": 3.775592041307464,
    "p_e59b9b": 4.229610589867865
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

