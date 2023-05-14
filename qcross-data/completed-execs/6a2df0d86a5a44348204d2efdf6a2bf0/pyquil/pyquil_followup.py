
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_311c30 = circuit.declare('p_311c30', 'REAL')
p_ef6cfa = circuit.declare('p_ef6cfa', 'REAL')
p_5c92ee = circuit.declare('p_5c92ee', 'REAL')
p_f8cd13 = circuit.declare('p_f8cd13', 'REAL')

defns = get_custom_get_definitions("CHGate", "RCCXGate", "CRXGate", "XGate", "ECRGate", "C3SXGate", "SdgGate", "RZGate", "ZGate", "CU1Gate", "SGate")

circuit += defns

circuit.inst(Gates.RZGate(p_311c30, 1 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.CRXGate(p_5c92ee, 2, 3 ))
circuit.inst(Gates.C3SXGate( 5, 4, 6, 2 ))
circuit.inst(Gates.CHGate( 1, 5 ))
circuit.inst(Gates.C3SXGate( 4, 2, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 5, 0 ))
circuit.inst(Gates.SdgGate( 5 ))
circuit.inst(Gates.RCCXGate( 2, 3, 4 ))
circuit.inst(Gates.SGate( 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 6 ))
circuit.inst(Gates.C3SXGate( 4, 2, 6, 0 ))
circuit.inst(Gates.CU1Gate(p_f8cd13, 1, 4 ))
circuit.inst(Gates.CRXGate(p_ef6cfa, 1, 5 ))

circuit += MEASURE(4, qr[0])
circuit += MEASURE(6, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(0, qr[3])
circuit += MEASURE(1, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(5, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_311c30": 6.163759533339787,
    "p_ef6cfa": 5.94477504571567,
    "p_5c92ee": 2.0099472182748075,
    "p_f8cd13": 3.2142159669963557
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

