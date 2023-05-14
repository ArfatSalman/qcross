
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_5d06b8 = circuit.declare('p_5d06b8', 'REAL')
p_97a6da = circuit.declare('p_97a6da', 'REAL')
p_9bb2df = circuit.declare('p_9bb2df', 'REAL')
p_1f1cd8 = circuit.declare('p_1f1cd8', 'REAL')
p_38c5ce = circuit.declare('p_38c5ce', 'REAL')

defns = get_custom_get_definitions("CRZGate", "TGate", "SXGate", "SXdgGate", "U2Gate", "ZGate", "UGate", "XGate", "RZGate", "CCXGate", "CHGate", "CRXGate", "CSXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 7 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 8, 7 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 6, 4 ))
circuit.inst(Gates.CCXGate( 3, 1, 4 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 6, 8 ))
circuit.inst(Gates.RZGate(p_9bb2df, 6 ))
circuit.inst(Gates.SXGate( 5 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.CCXGate( 0, 1, 3 ))
circuit.inst(Gates.C3SXGate( 5, 0, 9, 1 ))
circuit.inst(Gates.CSXGate( 9, 5 ))
circuit.inst(Gates.ZGate( 9 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.CSXGate( 5, 9 ))
circuit.inst(Gates.CRZGate(p_5d06b8, 6, 5 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 5 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.RZGate(5.014941143947427, 6 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 4, 6 ))
circuit.inst(Gates.UGate(p_38c5ce, p_1f1cd8, p_97a6da)( 5 ))

qr_df4e3d = circuit.declare("qr_df4e3d", "BIT", 1)

circuit += MEASURE(9, qr[0])
circuit += MEASURE(6, qr[1])
circuit += MEASURE(5, qr[2])
circuit += MEASURE(7, qr[3])
circuit += MEASURE(0, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(8, qr[6])
circuit += MEASURE(4, qr[7])
circuit += MEASURE(2, qr[8])
circuit += MEASURE(1, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_5d06b8": 2.586208953975239,
    "p_97a6da": 2.271164628944128,
    "p_9bb2df": 4.229610589867865,
    "p_1f1cd8": 5.023617931957853,
    "p_38c5ce": 5.080799300534071
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

