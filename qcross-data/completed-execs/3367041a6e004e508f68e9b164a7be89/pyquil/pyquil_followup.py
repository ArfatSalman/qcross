
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_5e2272 = circuit.declare('p_5e2272', 'REAL')
p_f1d349 = circuit.declare('p_f1d349', 'REAL')
p_6cc0de = circuit.declare('p_6cc0de', 'REAL')
p_093bc9 = circuit.declare('p_093bc9', 'REAL')
p_96f88b = circuit.declare('p_96f88b', 'REAL')
p_4e3e7e = circuit.declare('p_4e3e7e', 'REAL')
p_5c737b = circuit.declare('p_5c737b', 'REAL')
p_47b2f7 = circuit.declare('p_47b2f7', 'REAL')

defns = get_custom_get_definitions("RYYGate", "XGate", "ECRGate", "ZGate", "SXdgGate", "TGate", "SGate", "RZGate", "CSXGate", "CRZGate", "CRXGate", "CHGate", "CU1Gate", "CUGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_093bc9, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_6cc0de, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_5c737b)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_5e2272, p_4e3e7e, 4.623446645668956, p_f1d349, 1, 4 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.RYYGate(p_96f88b)( 0, 2 ))
circuit.inst(Gates.CU1Gate(p_47b2f7, 3, 0 ))

qr_82f68e = circuit.declare("qr_82f68e", "BIT", 2)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_5e2272": 5.708725119517347,
    "p_f1d349": 3.865496458458116,
    "p_6cc0de": 1.0296448789776642,
    "p_093bc9": 2.0099472182748075,
    "p_96f88b": 5.398622178940033,
    "p_4e3e7e": 4.167661441102218,
    "p_5c737b": 1.6723037552953224,
    "p_47b2f7": 3.2142159669963557
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

