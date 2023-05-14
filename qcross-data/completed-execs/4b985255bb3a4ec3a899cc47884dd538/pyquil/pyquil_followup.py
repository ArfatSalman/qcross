
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_bef792 = circuit.declare('p_bef792', 'REAL')
p_16c66f = circuit.declare('p_16c66f', 'REAL')
p_72801a = circuit.declare('p_72801a', 'REAL')
p_adfdc7 = circuit.declare('p_adfdc7', 'REAL')
p_a3b68b = circuit.declare('p_a3b68b', 'REAL')
p_35f264 = circuit.declare('p_35f264', 'REAL')
p_477e3c = circuit.declare('p_477e3c', 'REAL')
p_e721ac = circuit.declare('p_e721ac', 'REAL')
p_70b332 = circuit.declare('p_70b332', 'REAL')
p_8ead38 = circuit.declare('p_8ead38', 'REAL')
p_dc333a = circuit.declare('p_dc333a', 'REAL')
p_f7eb17 = circuit.declare('p_f7eb17', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "ECRGate", "C3SXGate", "UGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(p_adfdc7, 6, 3 ))
circuit.inst(Gates.CRXGate(p_e721ac, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(p_70b332, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_35f264, 1, 2 ))
circuit.inst(Gates.U2Gate(p_a3b68b, p_72801a)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(p_bef792, 1 ))
circuit.inst(Gates.CRXGate(p_8ead38, 7, 1 ))
circuit.inst(Gates.UGate(p_16c66f, p_477e3c, p_f7eb17)( 2 ))
circuit.inst(Gates.ECRGate( 4, 8 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.CSXGate( 1, 7 ))
circuit.inst(Gates.RZGate(p_dc333a, 5 ))

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
    "p_bef792": 5.014941143947427,
    "p_16c66f": 5.080799300534071,
    "p_72801a": 2.1276323672732023,
    "p_adfdc7": 4.2641612072511235,
    "p_a3b68b": 2.5163050709890156,
    "p_35f264": 2.586208953975239,
    "p_477e3c": 5.023617931957853,
    "p_e721ac": 5.987304452123941,
    "p_70b332": 4.229610589867865,
    "p_8ead38": 5.970852306777193,
    "p_dc333a": 3.6614081973587154,
    "p_f7eb17": 2.271164628944128
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

