
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)

p_94d012 = circuit.declare('p_94d012', 'REAL')
p_7f95e9 = circuit.declare('p_7f95e9', 'REAL')
p_97b6e3 = circuit.declare('p_97b6e3', 'REAL')
p_3bb993 = circuit.declare('p_3bb993', 'REAL')
p_3ab710 = circuit.declare('p_3ab710', 'REAL')
p_77c43b = circuit.declare('p_77c43b', 'REAL')
p_3c804b = circuit.declare('p_3c804b', 'REAL')
p_5a4f4d = circuit.declare('p_5a4f4d', 'REAL')

defns = get_custom_get_definitions("U2Gate", "ECRGate", "C3SXGate", "U1Gate", "CUGate", "RZGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_7f95e9, 8 ))

subcircuit = Program()
subcircuit.inst(Gates.RZGate(p_77c43b, 0 ))
subcircuit.inst(Gates.CZGate( 5, 0 ))
subcircuit.inst(Gates.U1Gate(p_5a4f4d, 0 ))
subcircuit.inst(Gates.ECRGate( 3, 0 ))
subcircuit.inst(Gates.U2Gate(p_97b6e3, p_3bb993)( 6 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(p_3ab710, 5.897054719225356, p_94d012, p_3c804b, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))

qr_8e3ddb = circuit.declare("qr_8e3ddb", "BIT", 5)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_94d012": 2.3864521352475245,
    "p_7f95e9": 6.163759533339787,
    "p_97b6e3": 5.887184334931191,
    "p_3bb993": 0.07157463504881167,
    "p_3ab710": 0.5112149185250571,
    "p_77c43b": 3.672121211148789,
    "p_3c804b": 5.987304452123941,
    "p_5a4f4d": 6.2047416485134805
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

