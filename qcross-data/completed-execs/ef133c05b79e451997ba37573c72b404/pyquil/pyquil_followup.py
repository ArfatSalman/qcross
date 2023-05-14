
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_37851b = circuit.declare('p_37851b', 'REAL')
p_771172 = circuit.declare('p_771172', 'REAL')
p_e59639 = circuit.declare('p_e59639', 'REAL')
p_432785 = circuit.declare('p_432785', 'REAL')
p_0f1b6d = circuit.declare('p_0f1b6d', 'REAL')
p_f2cc7e = circuit.declare('p_f2cc7e', 'REAL')
p_2c778f = circuit.declare('p_2c778f', 'REAL')
p_0c9124 = circuit.declare('p_0c9124', 'REAL')
p_a04195 = circuit.declare('p_a04195', 'REAL')
p_2361ce = circuit.declare('p_2361ce', 'REAL')
p_3f48eb = circuit.declare('p_3f48eb', 'REAL')
p_acd647 = circuit.declare('p_acd647', 'REAL')
p_609841 = circuit.declare('p_609841', 'REAL')
p_fc560c = circuit.declare('p_fc560c', 'REAL')
p_1a7816 = circuit.declare('p_1a7816', 'REAL')
p_981c1e = circuit.declare('p_981c1e', 'REAL')
p_484055 = circuit.declare('p_484055', 'REAL')

defns = get_custom_get_definitions("RYYGate", "C3SXGate", "ZGate", "RZZGate", "CU1Gate", "CRXGate", "CSXGate", "XGate", "CUGate", "SXdgGate", "SXGate", "CRZGate", "U2Gate", "RXGate", "SdgGate", "CHGate", "CPhaseGate", "RZGate", "TGate")

circuit += defns

circuit.inst(Gates.RZGate(p_3f48eb, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(p_2361ce, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_771172, 1, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(p_0f1b6d, 6, 4 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 6 ))

subcircuit = Program()
subcircuit.inst(Gates.CUGate(4.722103101046168, 5.3924725338944945, 4.88987246261121, p_609841, 2, 0 ))
subcircuit.inst(Gates.CUGate(2.862865991712737, 6.0504088665633065, p_e59639, p_0c9124, 3, 6 ))
subcircuit.inst(Gates.RXGate(3.698825211554417, 3 ))
subcircuit.inst(Gates.CHGate( 1, 6 ))
subcircuit.inst(Gates.U2Gate(p_a04195, 1.0052392769301404)( 4 ))
subcircuit.inst(Gates.RZGate(3.2374432046466546, 7 ))
subcircuit.inst(Gates.SXdgGate( 7 ))
subcircuit.inst(Gates.CPhaseGate(p_acd647, 7, 6 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(p_f2cc7e, 4 ))
circuit.inst(Gates.CRXGate(p_484055, 0, 3 ))
circuit.inst(Gates.CUGate(5.03147076606842, p_fc560c, p_1a7816, p_37851b, 6, 2 ))
circuit.inst(Gates.U2Gate(p_981c1e, p_2c778f)( 2 ))
circuit.inst(Gates.TGate( 6 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.RZZGate(p_432785)( 3, 4 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RYYGate(1.9669252191306448)( 4, 2 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 5 ))
circuit.inst(Gates.SXdgGate( 7 ))

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
    "p_37851b": 4.940217775579305,
    "p_771172": 4.167661441102218,
    "p_e59639": 1.7203758404994713,
    "p_432785": 3.950837470808744,
    "p_0f1b6d": 5.94477504571567,
    "p_f2cc7e": 3.775592041307464,
    "p_2c778f": 2.1276323672732023,
    "p_0c9124": 2.8704483107274004,
    "p_a04195": 0.25812405723927917,
    "p_2361ce": 5.987304452123941,
    "p_3f48eb": 6.163759533339787,
    "p_acd647": 1.672427069032094,
    "p_609841": 1.2497571638956968,
    "p_fc560c": 5.0063780207098425,
    "p_1a7816": 3.1562533916051736,
    "p_981c1e": 2.5163050709890156,
    "p_484055": 0.7279391018916035
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

