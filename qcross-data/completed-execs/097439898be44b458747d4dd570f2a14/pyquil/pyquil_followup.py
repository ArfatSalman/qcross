
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_38d9cb = circuit.declare('p_38d9cb', 'REAL')
p_6fbfe4 = circuit.declare('p_6fbfe4', 'REAL')
p_6b711e = circuit.declare('p_6b711e', 'REAL')
p_bb0c9a = circuit.declare('p_bb0c9a', 'REAL')
p_afbfa9 = circuit.declare('p_afbfa9', 'REAL')
p_985fe0 = circuit.declare('p_985fe0', 'REAL')
p_f413fb = circuit.declare('p_f413fb', 'REAL')
p_dc4e0f = circuit.declare('p_dc4e0f', 'REAL')
p_7ac4d4 = circuit.declare('p_7ac4d4', 'REAL')
p_559ba5 = circuit.declare('p_559ba5', 'REAL')
p_6b4cf2 = circuit.declare('p_6b4cf2', 'REAL')
p_30bc99 = circuit.declare('p_30bc99', 'REAL')
p_3e628e = circuit.declare('p_3e628e', 'REAL')
p_e762e6 = circuit.declare('p_e762e6', 'REAL')
p_f754b8 = circuit.declare('p_f754b8', 'REAL')
p_a9c7f4 = circuit.declare('p_a9c7f4', 'REAL')
p_01c9cb = circuit.declare('p_01c9cb', 'REAL')
p_ae29cc = circuit.declare('p_ae29cc', 'REAL')

defns = get_custom_get_definitions("RYYGate", "CSXGate", "U2Gate", "CUGate", "CU1Gate", "SdgGate", "SXGate", "XGate", "CRZGate", "C3SXGate", "CRXGate", "RZZGate", "TGate", "RZGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_559ba5, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_38d9cb, 0, 6 ))
circuit.inst(Gates.CRZGate(p_bb0c9a, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_3e628e)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_f413fb, 1, 7 ))
circuit.inst(Gates.RZGate(p_6fbfe4, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_6b4cf2, 4, 0 ))
circuit.inst(Gates.CRXGate(p_e762e6, 6, 4 ))
circuit.inst(Gates.RZZGate(p_30bc99)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.RZGate(p_f754b8, 4 ))
circuit.inst(Gates.CRXGate(p_dc4e0f, 0, 3 ))
circuit.inst(Gates.CUGate(p_01c9cb, p_6b711e, p_ae29cc, p_7ac4d4, 6, 2 ))
circuit.inst(Gates.U2Gate(p_a9c7f4, p_985fe0)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(p_afbfa9)( 3, 4 ))
circuit.inst(Gates.TGate( 5 ))

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
    "p_38d9cb": 5.987304452123941,
    "p_6fbfe4": 4.229610589867865,
    "p_6b711e": 5.0063780207098425,
    "p_bb0c9a": 1.0296448789776642,
    "p_afbfa9": 3.950837470808744,
    "p_985fe0": 2.1276323672732023,
    "p_f413fb": 4.167661441102218,
    "p_dc4e0f": 0.7279391018916035,
    "p_7ac4d4": 4.940217775579305,
    "p_559ba5": 6.163759533339787,
    "p_6b4cf2": 3.2142159669963557,
    "p_30bc99": 5.1829934776392745,
    "p_3e628e": 1.740253089260498,
    "p_e762e6": 5.94477504571567,
    "p_f754b8": 3.775592041307464,
    "p_a9c7f4": 2.5163050709890156,
    "p_01c9cb": 5.03147076606842,
    "p_ae29cc": 3.1562533916051736
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

