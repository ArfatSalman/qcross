
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 6)

p_0e7163 = circuit.declare('p_0e7163', 'REAL')
p_44a409 = circuit.declare('p_44a409', 'REAL')
p_8270ff = circuit.declare('p_8270ff', 'REAL')
p_96c96a = circuit.declare('p_96c96a', 'REAL')
p_796fab = circuit.declare('p_796fab', 'REAL')
p_8d288b = circuit.declare('p_8d288b', 'REAL')
p_facb1d = circuit.declare('p_facb1d', 'REAL')
p_492eef = circuit.declare('p_492eef', 'REAL')

defns = get_custom_get_definitions("SXGate", "CU1Gate", "UGate", "SGate", "C3SXGate", "CRZGate", "RZGate", "CCXGate", "SdgGate", "RCCXGate", "ZGate", "CUGate", "TGate", "CRXGate", "RZZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_44a409, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_8270ff, 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, p_8d288b, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(p_facb1d, 1, 5 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_0e7163, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, p_492eef)( 5 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 0, 5 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 5 ))
circuit.inst(Gates.CU1Gate(p_96c96a, 1, 4 ))
circuit.inst(Gates.C3SXGate( 3, 0, 4, 2 ))
circuit.inst(Gates.CRZGate(p_796fab, 2, 5 ))
circuit.inst(Gates.CRXGate(2.6687018103754414, 4, 5 ))
circuit.inst(Gates.CRZGate(5.742126321682921, 2, 0 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.SdgGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_0e7163": 3.2142159669963557,
    "p_44a409": 6.163759533339787,
    "p_8270ff": 4.2641612072511235,
    "p_96c96a": 4.028174522740928,
    "p_796fab": 2.586208953975239,
    "p_8d288b": 2.3864521352475245,
    "p_facb1d": 4.167661441102218,
    "p_492eef": 1.4112277317699358
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        

result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

