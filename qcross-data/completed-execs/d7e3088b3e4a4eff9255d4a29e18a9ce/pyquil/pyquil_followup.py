
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 4)

p_597899 = circuit.declare('p_597899', 'REAL')
p_300a3c = circuit.declare('p_300a3c', 'REAL')
p_b934bd = circuit.declare('p_b934bd', 'REAL')
p_9136a9 = circuit.declare('p_9136a9', 'REAL')
p_bcf56a = circuit.declare('p_bcf56a', 'REAL')
p_ee7fe0 = circuit.declare('p_ee7fe0', 'REAL')
p_9fd00a = circuit.declare('p_9fd00a', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "XGate", "RZGate", "TGate", "CUGate", "RYYGate", "U2Gate", "SXdgGate", "CHGate", "CSXGate", "SGate", "C3SXGate", "CXGate", "ECRGate", "CU1Gate", "iSwapGate", "RZZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_bcf56a, 1 ))
circuit.inst(Gates.RZZGate(p_597899)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_9136a9, p_b934bd, 2.3864521352475245, p_9fd00a, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_ee7fe0, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.ECRGate( 1, 3 ))
subcircuit.inst(Gates.U2Gate(6.171674001528992, 4.948673314014118)( 0 ))
subcircuit.inst(Gates.SGate( 1 ))
subcircuit.inst(Gates.CXGate( 0, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(p_300a3c)( 2, 0 ))
circuit.inst(Gates.RCCXGate( 2, 3, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_597899": 4.066449154047175,
    "p_300a3c": 1.740253089260498,
    "p_b934bd": 5.897054719225356,
    "p_9136a9": 0.5112149185250571,
    "p_bcf56a": 6.163759533339787,
    "p_ee7fe0": 5.154187354656876,
    "p_9fd00a": 5.987304452123941
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

