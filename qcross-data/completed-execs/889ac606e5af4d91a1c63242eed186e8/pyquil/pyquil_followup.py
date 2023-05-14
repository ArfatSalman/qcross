
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_e4a82b = circuit.declare('p_e4a82b', 'REAL')
p_897fa0 = circuit.declare('p_897fa0', 'REAL')
p_4c8c10 = circuit.declare('p_4c8c10', 'REAL')
p_42a1d4 = circuit.declare('p_42a1d4', 'REAL')
p_b41b47 = circuit.declare('p_b41b47', 'REAL')
p_f7f517 = circuit.declare('p_f7f517', 'REAL')
p_3d4bf9 = circuit.declare('p_3d4bf9', 'REAL')
p_258753 = circuit.declare('p_258753', 'REAL')
p_a5e20b = circuit.declare('p_a5e20b', 'REAL')

defns = get_custom_get_definitions("CRZGate", "U2Gate", "SXdgGate", "ECRGate", "C3SXGate", "UGate", "CRXGate", "RZGate", "TGate", "XGate", "CSXGate", "ZGate", "SXGate", "CHGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(p_42a1d4, 6, 3 ))
circuit.inst(Gates.CRXGate(p_258753, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(p_a5e20b, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_f7f517, 1, 2 ))
circuit.inst(Gates.U2Gate(p_b41b47, p_4c8c10)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(p_e4a82b, 1 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 7, 1 ))
circuit.inst(Gates.UGate(p_897fa0, p_3d4bf9, 2.271164628944128)( 2 ))
circuit.inst(Gates.ECRGate( 4, 8 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.ZGate( 8 ))
circuit.inst(Gates.CSXGate( 1, 7 ))
circuit.inst(Gates.RZGate(3.6614081973587154, 5 ))

qr_078017 = circuit.declare("qr_078017", "BIT", 2)

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
    "p_e4a82b": 5.014941143947427,
    "p_897fa0": 5.080799300534071,
    "p_4c8c10": 2.1276323672732023,
    "p_42a1d4": 4.2641612072511235,
    "p_b41b47": 2.5163050709890156,
    "p_f7f517": 2.586208953975239,
    "p_3d4bf9": 5.023617931957853,
    "p_258753": 5.987304452123941,
    "p_a5e20b": 4.229610589867865
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

