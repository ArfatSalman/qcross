
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_b4dbcc = circuit.declare('p_b4dbcc', 'REAL')
p_5ea921 = circuit.declare('p_5ea921', 'REAL')

defns = get_custom_get_definitions("ZGate", "CHGate", "CU1Gate", "RCCXGate", "SGate", "C3SXGate", "ECRGate", "XGate", "CRXGate", "RZGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_b4dbcc, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(p_5ea921, 4, 6 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_b4dbcc": 6.163759533339787,
    "p_5ea921": 5.94477504571567
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

