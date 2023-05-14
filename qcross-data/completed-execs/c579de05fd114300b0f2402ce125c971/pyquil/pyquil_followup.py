
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_d25745 = circuit.declare('p_d25745', 'REAL')
p_7280db = circuit.declare('p_7280db', 'REAL')
p_66bc6f = circuit.declare('p_66bc6f', 'REAL')
p_7efb1a = circuit.declare('p_7efb1a', 'REAL')
p_9e0b52 = circuit.declare('p_9e0b52', 'REAL')
p_6a275f = circuit.declare('p_6a275f', 'REAL')
p_a8dc96 = circuit.declare('p_a8dc96', 'REAL')
p_6c61a4 = circuit.declare('p_6c61a4', 'REAL')
p_0f968c = circuit.declare('p_0f968c', 'REAL')
p_55502a = circuit.declare('p_55502a', 'REAL')
p_74ecdc = circuit.declare('p_74ecdc', 'REAL')
p_3ebfd3 = circuit.declare('p_3ebfd3', 'REAL')
p_eb0914 = circuit.declare('p_eb0914', 'REAL')
p_e304cd = circuit.declare('p_e304cd', 'REAL')
p_5dbd96 = circuit.declare('p_5dbd96', 'REAL')
p_0caccb = circuit.declare('p_0caccb', 'REAL')

defns = get_custom_get_definitions("CRZGate", "CU1Gate", "RZZGate", "ZGate", "UGate", "SXGate", "CUGate", "TGate", "RCCXGate", "CCXGate", "RZGate", "C3SXGate", "SGate")

circuit += defns

circuit.inst(Gates.RZGate(p_0caccb, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_9e0b52, 1, 4 ))
circuit.inst(Gates.CUGate(p_55502a, p_74ecdc, p_5dbd96, p_66bc6f, 1, 3 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 1 ))
circuit.inst(Gates.CCXGate( 2, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(p_a8dc96, 2, 5 ))
circuit.inst(Gates.RZGate(p_6c61a4, 2 ))
circuit.inst(Gates.C3SXGate( 0, 1, 2, 3 ))
circuit.inst(Gates.CU1Gate(p_3ebfd3, 3, 0 ))
circuit.inst(Gates.UGate(p_e304cd, p_0f968c, p_6a275f)( 5 ))
circuit.inst(Gates.RZZGate(p_d25745)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(p_eb0914, 0, 5 ))
circuit.inst(Gates.CU1Gate(p_7efb1a, 2, 4 ))
circuit.inst(Gates.C3SXGate( 3, 0, 4, 1 ))
circuit.inst(Gates.CRZGate(p_7280db, 1, 5 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(2, qr[1])
circuit += MEASURE(1, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_d25745": 5.1829934776392745,
    "p_7280db": 2.586208953975239,
    "p_66bc6f": 5.987304452123941,
    "p_7efb1a": 4.028174522740928,
    "p_9e0b52": 4.2641612072511235,
    "p_6a275f": 1.4112277317699358,
    "p_a8dc96": 4.167661441102218,
    "p_6c61a4": 4.229610589867865,
    "p_0f968c": 0.07157463504881167,
    "p_55502a": 0.5112149185250571,
    "p_74ecdc": 5.897054719225356,
    "p_3ebfd3": 3.2142159669963557,
    "p_eb0914": 4.833923139882297,
    "p_e304cd": 5.887184334931191,
    "p_5dbd96": 2.3864521352475245,
    "p_0caccb": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

