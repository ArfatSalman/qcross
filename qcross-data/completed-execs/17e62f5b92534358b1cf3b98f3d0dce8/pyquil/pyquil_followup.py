
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_efcc68 = circuit.declare('p_efcc68', 'REAL')
p_2061b2 = circuit.declare('p_2061b2', 'REAL')
p_536d06 = circuit.declare('p_536d06', 'REAL')
p_732b5a = circuit.declare('p_732b5a', 'REAL')
p_dbfaed = circuit.declare('p_dbfaed', 'REAL')
p_28ab37 = circuit.declare('p_28ab37', 'REAL')
p_c8704d = circuit.declare('p_c8704d', 'REAL')
p_77100f = circuit.declare('p_77100f', 'REAL')

defns = get_custom_get_definitions("RZGate", "CRXGate", "CSXGate", "U2Gate", "CCXGate", "CHGate", "SXGate", "SXdgGate", "TGate", "CRZGate", "C3SXGate", "XGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_536d06, 3 ))
circuit.inst(Gates.CRZGate(p_dbfaed, 6, 3 ))
circuit.inst(Gates.CRXGate(p_2061b2, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_28ab37, 1, 6 ))
circuit.inst(Gates.RZGate(p_efcc68, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_77100f, 1, 2 ))
circuit.inst(Gates.U2Gate(p_c8704d, p_732b5a)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))

qr_78a91c = circuit.declare("qr_78a91c", "BIT", 2)

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
    "p_efcc68": 4.229610589867865,
    "p_2061b2": 5.987304452123941,
    "p_536d06": 6.163759533339787,
    "p_732b5a": 2.1276323672732023,
    "p_dbfaed": 4.2641612072511235,
    "p_28ab37": 4.167661441102218,
    "p_c8704d": 2.5163050709890156,
    "p_77100f": 2.586208953975239
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

