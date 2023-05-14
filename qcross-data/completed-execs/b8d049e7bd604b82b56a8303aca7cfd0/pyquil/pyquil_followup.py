
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_a2b8a1 = circuit.declare('p_a2b8a1', 'REAL')
p_c71b89 = circuit.declare('p_c71b89', 'REAL')
p_109b12 = circuit.declare('p_109b12', 'REAL')
p_61c866 = circuit.declare('p_61c866', 'REAL')
p_55837c = circuit.declare('p_55837c', 'REAL')
p_bcdc65 = circuit.declare('p_bcdc65', 'REAL')
p_ad1c79 = circuit.declare('p_ad1c79', 'REAL')
p_0e4f1e = circuit.declare('p_0e4f1e', 'REAL')
p_708df6 = circuit.declare('p_708df6', 'REAL')
p_b373ee = circuit.declare('p_b373ee', 'REAL')
p_89d7ca = circuit.declare('p_89d7ca', 'REAL')
p_55cda5 = circuit.declare('p_55cda5', 'REAL')
p_1d0fad = circuit.declare('p_1d0fad', 'REAL')
p_a3b617 = circuit.declare('p_a3b617', 'REAL')
p_a0a530 = circuit.declare('p_a0a530', 'REAL')

defns = get_custom_get_definitions("CHGate", "ZGate", "RZGate", "CRZGate", "TGate", "SXdgGate", "SXGate", "ECRGate", "C3SXGate", "CRXGate", "UGate", "U2Gate", "XGate", "CSXGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_1d0fad, 3 ))
circuit.inst(Gates.CRZGate(p_708df6, 6, 3 ))
circuit.inst(Gates.CRXGate(p_0e4f1e, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))

subcircuit = Program()
subcircuit.inst(Gates.U2Gate(p_a0a530, p_a3b617)( 0 ))
subcircuit.inst(Gates.SXdgGate( 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_61c866, 1, 6 ))
circuit.inst(Gates.RZGate(p_55cda5, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_c71b89, 1, 2 ))
circuit.inst(Gates.U2Gate(p_b373ee, p_ad1c79)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(p_a2b8a1, 1 ))
circuit.inst(Gates.CRXGate(p_89d7ca, 7, 1 ))
circuit.inst(Gates.UGate(p_55837c, p_bcdc65, p_109b12)( 2 ))
circuit.inst(Gates.ECRGate( 4, 8 ))
circuit.inst(Gates.ZGate( 3 ))

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




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_a2b8a1": 5.014941143947427,
    "p_c71b89": 2.586208953975239,
    "p_109b12": 2.271164628944128,
    "p_61c866": 4.167661441102218,
    "p_55837c": 5.080799300534071,
    "p_bcdc65": 5.023617931957853,
    "p_ad1c79": 2.1276323672732023,
    "p_0e4f1e": 5.987304452123941,
    "p_708df6": 4.2641612072511235,
    "p_b373ee": 2.5163050709890156,
    "p_89d7ca": 5.970852306777193,
    "p_55cda5": 4.229610589867865,
    "p_1d0fad": 6.163759533339787,
    "p_a3b617": 1.0052392769301404,
    "p_a0a530": 0.25812405723927917
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

