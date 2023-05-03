
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_340c8c = circuit.declare('p_340c8c', 'REAL')
p_a4a463 = circuit.declare('p_a4a463', 'REAL')
p_011c31 = circuit.declare('p_011c31', 'REAL')
p_cb453e = circuit.declare('p_cb453e', 'REAL')

defns = get_custom_get_definitions("SXdgGate", "CHGate", "XGate", "CCXGate", "ECRGate", "ZGate", "TGate", "CSXGate", "CRZGate", "C3SXGate", "SXGate", "CRXGate", "U2Gate", "UGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_a4a463, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_340c8c, 1, 2 ))
circuit.inst(Gates.U2Gate(p_011c31, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(5.014941143947427, 1 ))
circuit.inst(Gates.CRXGate(p_cb453e, 7, 1 ))
circuit.inst(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( 2 ))
circuit.inst(Gates.ECRGate( 4, 8 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.CSXGate( 1, 7 ))

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
    "p_340c8c": 2.586208953975239,
    "p_a4a463": 6.163759533339787,
    "p_011c31": 2.5163050709890156,
    "p_cb453e": 5.970852306777193
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

