
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 2)

p_492844 = circuit.declare('p_492844', 'REAL')
p_730e02 = circuit.declare('p_730e02', 'REAL')
p_57eb86 = circuit.declare('p_57eb86', 'REAL')
p_66f8bd = circuit.declare('p_66f8bd', 'REAL')
p_413130 = circuit.declare('p_413130', 'REAL')
p_00b361 = circuit.declare('p_00b361', 'REAL')
p_37a10a = circuit.declare('p_37a10a', 'REAL')
p_8594a5 = circuit.declare('p_8594a5', 'REAL')
p_1a08ce = circuit.declare('p_1a08ce', 'REAL')
p_ec5eaf = circuit.declare('p_ec5eaf', 'REAL')
p_dd7bb0 = circuit.declare('p_dd7bb0', 'REAL')

defns = get_custom_get_definitions("CHGate", "CRZGate", "RZZGate", "TGate", "ECRGate", "RZGate", "SXGate", "iSwapGate", "CRXGate", "RYYGate", "CU1Gate", "XGate", "CSXGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.RZZGate(p_492844)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_1a08ce)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(p_730e02, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_37a10a, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_00b361, 1 ))
circuit.inst(Gates.RZGate(p_413130, 1 ))
circuit.inst(Gates.CU1Gate(p_57eb86, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(p_8594a5)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(p_66f8bd)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_ec5eaf, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_dd7bb0)( 1, 0 ))

qr_908ff6 = circuit.declare("qr_908ff6", "BIT", 4)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_492844": 6.163759533339787,
    "p_730e02": 5.987304452123941,
    "p_57eb86": 1.6723037552953224,
    "p_66f8bd": 3.3705408413231095,
    "p_413130": 5.512260524440591,
    "p_00b361": 5.320621737498446,
    "p_37a10a": 2.2498881927557752,
    "p_8594a5": 6.086884486572108,
    "p_1a08ce": 1.977559237989846,
    "p_ec5eaf": 5.190931186022931,
    "p_dd7bb0": 5.167261531657622
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

