
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_4f8db3 = circuit.declare('p_4f8db3', 'REAL')
p_daae8b = circuit.declare('p_daae8b', 'REAL')
p_89f9ae = circuit.declare('p_89f9ae', 'REAL')
p_6f799f = circuit.declare('p_6f799f', 'REAL')
p_25d5a8 = circuit.declare('p_25d5a8', 'REAL')
p_eadd70 = circuit.declare('p_eadd70', 'REAL')
p_efceeb = circuit.declare('p_efceeb', 'REAL')
p_0cd2a2 = circuit.declare('p_0cd2a2', 'REAL')
p_574806 = circuit.declare('p_574806', 'REAL')
p_2907ce = circuit.declare('p_2907ce', 'REAL')
p_a8217e = circuit.declare('p_a8217e', 'REAL')
p_cf4aa0 = circuit.declare('p_cf4aa0', 'REAL')
p_a87faa = circuit.declare('p_a87faa', 'REAL')

defns = get_custom_get_definitions("SGate", "ZGate", "CU1Gate", "RZGate", "RYYGate", "CRZGate", "RCCXGate", "CRXGate", "CHGate", "TGate", "UGate", "XGate", "CUGate", "CSXGate", "ECRGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.RZGate(p_0cd2a2, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_a8217e, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_25d5a8, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_a87faa)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_6f799f, 4.167661441102218, 4.623446645668956, p_daae8b, 1, 4 ))
circuit.inst(Gates.RZGate(p_4f8db3, 1 ))
circuit.inst(Gates.RYYGate(p_efceeb)( 0, 2 ))
circuit.inst(Gates.CU1Gate(p_574806, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, p_89f9ae)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CHGate( 0, 4 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CU1Gate(p_cf4aa0, 0, 3 ))
circuit.inst(Gates.RCCXGate( 0, 3, 1 ))
circuit.inst(Gates.CUGate(5.03147076606842, p_eadd70, p_2907ce, 4.940217775579305, 4, 3 ))
circuit.inst(Gates.CRZGate(3.839241945509346, 2, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_4f8db3": 4.229610589867865,
    "p_daae8b": 3.865496458458116,
    "p_89f9ae": 1.4112277317699358,
    "p_6f799f": 5.708725119517347,
    "p_25d5a8": 1.0296448789776642,
    "p_eadd70": 5.0063780207098425,
    "p_efceeb": 5.398622178940033,
    "p_0cd2a2": 6.163759533339787,
    "p_574806": 3.2142159669963557,
    "p_2907ce": 3.1562533916051736,
    "p_a8217e": 2.0099472182748075,
    "p_cf4aa0": 4.028174522740928,
    "p_a87faa": 1.6723037552953224
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

