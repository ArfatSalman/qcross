
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_07b864 = circuit.declare('p_07b864', 'REAL')
p_12832b = circuit.declare('p_12832b', 'REAL')
p_aa27f8 = circuit.declare('p_aa27f8', 'REAL')
p_5f4a74 = circuit.declare('p_5f4a74', 'REAL')
p_d0f83e = circuit.declare('p_d0f83e', 'REAL')
p_6afe18 = circuit.declare('p_6afe18', 'REAL')
p_6d8eba = circuit.declare('p_6d8eba', 'REAL')
p_c41e19 = circuit.declare('p_c41e19', 'REAL')
p_431464 = circuit.declare('p_431464', 'REAL')
p_96609c = circuit.declare('p_96609c', 'REAL')
p_990bb6 = circuit.declare('p_990bb6', 'REAL')

defns = get_custom_get_definitions("CHGate", "CSXGate", "ZGate", "U2Gate", "TGate", "C3SXGate", "CU1Gate", "RZGate", "CRXGate", "CRZGate", "XGate", "RYYGate", "RZZGate", "ECRGate", "RCCXGate", "SGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_990bb6, 5 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.CRXGate(p_12832b, 0, 3 ))
circuit.inst(Gates.C3SXGate( 4, 2, 6, 0 ))
circuit.inst(Gates.CHGate( 5, 4 ))
circuit.inst(Gates.C3SXGate( 2, 0, 6, 3 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ECRGate( 4, 1 ))
circuit.inst(Gates.SdgGate( 4 ))
circuit.inst(Gates.RCCXGate( 0, 3, 2 ))
circuit.inst(Gates.SGate( 6 ))
circuit.inst(Gates.RZGate(p_6afe18, 6 ))
circuit.inst(Gates.C3SXGate( 2, 0, 6, 1 ))
circuit.inst(Gates.CU1Gate(p_07b864, 5, 2 ))
circuit.inst(Gates.CRXGate(p_431464, 5, 4 ))
circuit.inst(Gates.CHGate( 5, 2 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_d0f83e, 2, 4 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 6, 5 ))
circuit.inst(Gates.C3SXGate( 0, 2, 3, 5 ))
circuit.inst(Gates.CRZGate(p_5f4a74, 4, 0 ))
circuit.inst(Gates.U2Gate(p_6d8eba, p_c41e19)( 0 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RZZGate(p_96609c)( 1, 5 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RYYGate(p_aa27f8)( 5, 0 ))

circuit += MEASURE(2, qr[0])
circuit += MEASURE(6, qr[1])
circuit += MEASURE(0, qr[2])
circuit += MEASURE(1, qr[3])
circuit += MEASURE(5, qr[4])
circuit += MEASURE(3, qr[5])
circuit += MEASURE(4, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_07b864": 3.2142159669963557,
    "p_12832b": 2.0099472182748075,
    "p_aa27f8": 1.9669252191306448,
    "p_5f4a74": 2.586208953975239,
    "p_d0f83e": 4.833923139882297,
    "p_6afe18": 4.229610589867865,
    "p_6d8eba": 2.5163050709890156,
    "p_c41e19": 2.1276323672732023,
    "p_431464": 5.94477504571567,
    "p_96609c": 3.950837470808744,
    "p_990bb6": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

