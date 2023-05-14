
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_f80351 = circuit.declare('p_f80351', 'REAL')
p_cb603f = circuit.declare('p_cb603f', 'REAL')
p_9a6428 = circuit.declare('p_9a6428', 'REAL')
p_14882b = circuit.declare('p_14882b', 'REAL')
p_229656 = circuit.declare('p_229656', 'REAL')
p_d83aa6 = circuit.declare('p_d83aa6', 'REAL')
p_1e7763 = circuit.declare('p_1e7763', 'REAL')

defns = get_custom_get_definitions("CCXGate", "CRXGate", "U2Gate", "TGate", "XGate", "CRZGate", "PhaseGate", "CXGate", "CU3Gate", "ECRGate", "RZGate", "DCXGate", "SXdgGate", "ZGate", "SXGate", "UGate", "CUGate", "CHGate", "CSXGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_1e7763, 3 ))
circuit.inst(Gates.CRZGate(p_cb603f, 6, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.SXdgGate( 5 ))
subcircuit.inst(Gates.DCXGate( 4, 7 ))
subcircuit.inst(Gates.CU3Gate(4.2220417977098705, 1.672427069032094, 2.447994042088217, 5, 3 ))
subcircuit.inst(Gates.CUGate(4.783709962939332, 4.509839071764646, 3.631024984774394, 2.3799139963609854, 7, 3 ))
subcircuit.inst(Gates.PhaseGate(5.949169145894372, 2 ))
subcircuit.inst(Gates.CSXGate( 1, 7 ))
subcircuit.inst(Gates.CXGate( 2, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_229656, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_9a6428, 1, 2 ))
circuit.inst(Gates.U2Gate(p_14882b, p_d83aa6)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RZGate(5.014941143947427, 1 ))
circuit.inst(Gates.CRXGate(p_f80351, 7, 1 ))
circuit.inst(Gates.UGate(5.080799300534071, 5.023617931957853, 2.271164628944128)( 2 ))
circuit.inst(Gates.ECRGate( 4, 8 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.ZGate( 8 ))

qr_3f20d8 = circuit.declare("qr_3f20d8", "BIT", 7)

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
    "p_f80351": 5.970852306777193,
    "p_cb603f": 4.2641612072511235,
    "p_9a6428": 2.586208953975239,
    "p_14882b": 2.5163050709890156,
    "p_229656": 4.167661441102218,
    "p_d83aa6": 2.1276323672732023,
    "p_1e7763": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

