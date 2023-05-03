
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_7268fa = circuit.declare('p_7268fa', 'REAL')
p_1ced18 = circuit.declare('p_1ced18', 'REAL')
p_943f31 = circuit.declare('p_943f31', 'REAL')
p_7168a9 = circuit.declare('p_7168a9', 'REAL')
p_d46b4e = circuit.declare('p_d46b4e', 'REAL')
p_cc0d68 = circuit.declare('p_cc0d68', 'REAL')
p_a7ec6e = circuit.declare('p_a7ec6e', 'REAL')
p_a346be = circuit.declare('p_a346be', 'REAL')
p_165b3b = circuit.declare('p_165b3b', 'REAL')
p_ea9bf0 = circuit.declare('p_ea9bf0', 'REAL')
p_e30407 = circuit.declare('p_e30407', 'REAL')
p_29d856 = circuit.declare('p_29d856', 'REAL')

defns = get_custom_get_definitions("CHGate", "ECRGate", "SGate", "RYYGate", "CSXGate", "TGate", "CRXGate", "CUGate", "CU1Gate", "UGate", "SwapGate", "CRYGate", "C3XGate", "ZGate", "XGate", "SXdgGate", "CRZGate", "RZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_7268fa, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.SwapGate( 4, 0 ))
subcircuit.inst(Gates.CRYGate(3.1402006997068588, 2, 0 ))
subcircuit.inst(Gates.CUGate(5.0063780207098425, 3.1562533916051736, 4.940217775579305, 2.419481683937988, 2, 1 ))
subcircuit.inst(Gates.C3XGate( 3, 4, 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_cc0d68, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_d46b4e, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(p_165b3b)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_943f31, p_1ced18, p_a7ec6e, p_e30407, 1, 4 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.RYYGate(p_29d856)( 0, 2 ))
circuit.inst(Gates.CU1Gate(p_7168a9, 3, 0 ))
circuit.inst(Gates.UGate(p_ea9bf0, p_a346be, 1.4112277317699358)( 4 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_7268fa": 6.163759533339787,
    "p_1ced18": 4.167661441102218,
    "p_943f31": 5.708725119517347,
    "p_7168a9": 3.2142159669963557,
    "p_d46b4e": 1.0296448789776642,
    "p_cc0d68": 2.0099472182748075,
    "p_a7ec6e": 4.623446645668956,
    "p_a346be": 0.07157463504881167,
    "p_165b3b": 1.6723037552953224,
    "p_ea9bf0": 5.887184334931191,
    "p_e30407": 3.865496458458116,
    "p_29d856": 5.398622178940033
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

