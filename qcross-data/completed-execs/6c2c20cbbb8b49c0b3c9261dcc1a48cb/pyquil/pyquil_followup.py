
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 7)

p_b96123 = circuit.declare('p_b96123', 'REAL')
p_016d54 = circuit.declare('p_016d54', 'REAL')
p_99427e = circuit.declare('p_99427e', 'REAL')
p_93d5ac = circuit.declare('p_93d5ac', 'REAL')
p_7691c4 = circuit.declare('p_7691c4', 'REAL')
p_7ec4f4 = circuit.declare('p_7ec4f4', 'REAL')

defns = get_custom_get_definitions("SdgGate", "RCCXGate", "RYYGate", "C3SXGate", "CRZGate", "CSXGate", "CRXGate", "XGate", "CU1Gate", "HGate", "SXdgGate", "RZGate", "ECRGate", "SGate", "ZGate", "CHGate", "SwapGate", "RZZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.HGate( 0 ))
subcircuit.inst(Gates.RZZGate(p_99427e)( 0, 5 ))
subcircuit.inst(Gates.CRZGate(p_016d54, 0, 5 ))
subcircuit.inst(Gates.CSXGate( 4, 0 ))
subcircuit.inst(Gates.SwapGate( 1, 4 ))
subcircuit.inst(Gates.RYYGate(0.5501056885328758)( 2, 0 ))
subcircuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(p_93d5ac, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_b96123, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_7691c4, 4, 0 ))
circuit.inst(Gates.CRXGate(p_7ec4f4, 4, 6 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])




circuit.wrap_in_numshots_loop(1959)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_b96123": 4.229610589867865,
    "p_016d54": 2.008796895454228,
    "p_99427e": 5.017245588344839,
    "p_93d5ac": 2.0099472182748075,
    "p_7691c4": 3.2142159669963557,
    "p_7ec4f4": 5.94477504571567
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

