
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_466c3c = circuit.declare('p_466c3c', 'REAL')
p_fb2b59 = circuit.declare('p_fb2b59', 'REAL')
p_f17856 = circuit.declare('p_f17856', 'REAL')
p_b0d476 = circuit.declare('p_b0d476', 'REAL')
p_c9d928 = circuit.declare('p_c9d928', 'REAL')
p_faf457 = circuit.declare('p_faf457', 'REAL')
p_cd9fd2 = circuit.declare('p_cd9fd2', 'REAL')
p_d9736e = circuit.declare('p_d9736e', 'REAL')
p_38ffe1 = circuit.declare('p_38ffe1', 'REAL')
p_305826 = circuit.declare('p_305826', 'REAL')
p_2e343f = circuit.declare('p_2e343f', 'REAL')
p_3eae93 = circuit.declare('p_3eae93', 'REAL')
p_499aed = circuit.declare('p_499aed', 'REAL')
p_40b220 = circuit.declare('p_40b220', 'REAL')
p_fbab31 = circuit.declare('p_fbab31', 'REAL')
p_6f4c81 = circuit.declare('p_6f4c81', 'REAL')
p_3681fa = circuit.declare('p_3681fa', 'REAL')
p_697593 = circuit.declare('p_697593', 'REAL')
p_e1e662 = circuit.declare('p_e1e662', 'REAL')

defns = get_custom_get_definitions("CRXGate", "ECRGate", "CRZGate", "UGate", "SGate", "TGate", "RCCXGate", "XGate", "CHGate", "RZGate", "CUGate", "RYYGate", "CSXGate", "CU1Gate", "SXdgGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_d9736e, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_499aed, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_c9d928, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_e1e662)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_b0d476, p_40b220, 4.623446645668956, p_fb2b59, 1, 4 ))
circuit.inst(Gates.RZGate(p_466c3c, 1 ))
circuit.inst(Gates.RYYGate(p_3681fa)( 0, 2 ))
circuit.inst(Gates.CU1Gate(p_38ffe1, 3, 0 ))
circuit.inst(Gates.UGate(p_6f4c81, p_3eae93, p_f17856)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CHGate( 0, 4 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CU1Gate(p_fbab31, 0, 3 ))
circuit.inst(Gates.RCCXGate( 0, 3, 1 ))
circuit.inst(Gates.CUGate(p_2e343f, p_faf457, p_305826, p_697593, 4, 3 ))
circuit.inst(Gates.CRZGate(p_cd9fd2, 2, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_466c3c": 4.229610589867865,
    "p_fb2b59": 3.865496458458116,
    "p_f17856": 1.4112277317699358,
    "p_b0d476": 5.708725119517347,
    "p_c9d928": 1.0296448789776642,
    "p_faf457": 5.0063780207098425,
    "p_cd9fd2": 3.839241945509346,
    "p_d9736e": 6.163759533339787,
    "p_38ffe1": 3.2142159669963557,
    "p_305826": 3.1562533916051736,
    "p_2e343f": 5.03147076606842,
    "p_3eae93": 0.07157463504881167,
    "p_499aed": 2.0099472182748075,
    "p_40b220": 4.167661441102218,
    "p_fbab31": 4.028174522740928,
    "p_6f4c81": 5.887184334931191,
    "p_3681fa": 5.398622178940033,
    "p_697593": 4.940217775579305,
    "p_e1e662": 1.6723037552953224
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

