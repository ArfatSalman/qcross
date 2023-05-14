
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)

p_dda1d3 = circuit.declare('p_dda1d3', 'REAL')
p_ce61f1 = circuit.declare('p_ce61f1', 'REAL')
p_d9b1ff = circuit.declare('p_d9b1ff', 'REAL')
p_98dc6e = circuit.declare('p_98dc6e', 'REAL')
p_e3b9a1 = circuit.declare('p_e3b9a1', 'REAL')
p_1bb590 = circuit.declare('p_1bb590', 'REAL')
p_ac58f5 = circuit.declare('p_ac58f5', 'REAL')
p_a8532b = circuit.declare('p_a8532b', 'REAL')
p_42b602 = circuit.declare('p_42b602', 'REAL')

defns = get_custom_get_definitions("CRZGate", "SXdgGate", "iSwapGate", "CRXGate", "RYYGate", "ZGate", "CU1Gate", "CUGate", "SGate", "RZGate", "TGate", "XGate", "CSXGate", "ECRGate", "SdgGate", "UGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(p_a8532b, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(p_dda1d3, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CRZGate(p_1bb590, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SGate( 4 ))
circuit.inst(Gates.CUGate(p_42b602, 4.167661441102218, p_98dc6e, p_d9b1ff, 1, 4 ))
circuit.inst(Gates.RZGate(p_ce61f1, 1 ))
circuit.inst(Gates.RYYGate(p_e3b9a1)( 0, 2 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 3, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, p_ac58f5, 1.4112277317699358)( 4 ))

subcircuit = Program()
subcircuit.inst(Gates.RYYGate(0.5501056885328758)( 3, 0 ))
subcircuit.inst(Gates.SXdgGate( 3 ))
subcircuit.inst(Gates.CRXGate(3.401136029677084, 1, 2 ))
subcircuit.inst(Gates.RYYGate(0.6724371252296606)( 0, 4 ))
subcircuit.inst(Gates.SdgGate( 0 ))
subcircuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CHGate( 0, 4 ))

qr_db075a = circuit.declare("qr_db075a", "BIT", 2)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_dda1d3": 2.0099472182748075,
    "p_ce61f1": 4.229610589867865,
    "p_d9b1ff": 3.865496458458116,
    "p_98dc6e": 4.623446645668956,
    "p_e3b9a1": 5.398622178940033,
    "p_1bb590": 1.0296448789776642,
    "p_ac58f5": 0.07157463504881167,
    "p_a8532b": 6.163759533339787,
    "p_42b602": 5.708725119517347
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

