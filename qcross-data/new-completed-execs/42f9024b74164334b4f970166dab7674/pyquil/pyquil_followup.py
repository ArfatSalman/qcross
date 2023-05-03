
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_f5ce15 = circuit.declare('p_f5ce15', 'REAL')
p_fa05b6 = circuit.declare('p_fa05b6', 'REAL')
p_75b77c = circuit.declare('p_75b77c', 'REAL')
p_e32c43 = circuit.declare('p_e32c43', 'REAL')
p_d9b3a9 = circuit.declare('p_d9b3a9', 'REAL')
p_415e22 = circuit.declare('p_415e22', 'REAL')
p_6c6aa2 = circuit.declare('p_6c6aa2', 'REAL')
p_66d326 = circuit.declare('p_66d326', 'REAL')
p_cf1375 = circuit.declare('p_cf1375', 'REAL')
p_9b1974 = circuit.declare('p_9b1974', 'REAL')
p_638ece = circuit.declare('p_638ece', 'REAL')
p_ee1794 = circuit.declare('p_ee1794', 'REAL')

defns = get_custom_get_definitions("CZGate", "CYGate", "CU3Gate", "YGate", "ECRGate", "UGate", "CSdgGate", "DCXGate", "CRXGate", "RGate", "CHGate", "CXGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.UGate(p_415e22, p_66d326, p_fa05b6)( 1 ))
circuit.inst(Gates.RGate(3.9800961208659213, p_9b1974)( 0 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CXGate( 1, 0 ))
circuit.inst(Gates.CRXGate(p_f5ce15, 1, 0 ))
circuit.inst(Gates.CSdgGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.CU3Gate(p_6c6aa2, p_638ece, p_e32c43, 0, 1 ))
circuit.inst(Gates.CZGate( 1, 0 ))
circuit.inst(Gates.RGate(p_ee1794, p_d9b3a9)( 1 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.UGate(p_75b77c, p_cf1375, 5.6467633400840755)( 1 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.ECRGate( 1, 0 ))

qr_d66e91 = circuit.declare("qr_d66e91", "BIT", 8)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_f5ce15": 3.0761375449158193,
    "p_fa05b6": 2.414376925356305,
    "p_75b77c": 3.820196974130503,
    "p_e32c43": 2.251031643786726,
    "p_d9b3a9": 4.7611258330830655,
    "p_415e22": 4.403788193532198,
    "p_6c6aa2": 3.359364374345002,
    "p_66d326": 5.238005217278175,
    "p_cf1375": 1.381440535002157,
    "p_9b1974": 2.54258238968427,
    "p_638ece": 4.018048446348199,
    "p_ee1794": 4.3040860238694725
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

