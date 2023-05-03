
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_d40aec = circuit.declare('p_d40aec', 'REAL')
p_10c631 = circuit.declare('p_10c631', 'REAL')
p_a7734b = circuit.declare('p_a7734b', 'REAL')
p_c8b7aa = circuit.declare('p_c8b7aa', 'REAL')
p_8f9e53 = circuit.declare('p_8f9e53', 'REAL')
p_da6dd8 = circuit.declare('p_da6dd8', 'REAL')
p_7f634a = circuit.declare('p_7f634a', 'REAL')

defns = get_custom_get_definitions("XGate", "RZGate", "ZGate", "RCCXGate", "SGate", "CSXGate", "CHGate", "CRXGate", "C3SXGate", "RYYGate", "ECRGate", "SdgGate", "CYGate", "CU1Gate", "SXGate", "SwapGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_da6dd8, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.CYGate( 2, 0 ))
subcircuit.inst(Gates.SXGate( 0 ))
subcircuit.inst(Gates.CRZGate(p_7f634a, 0, 5 ))
subcircuit.inst(Gates.CSXGate( 4, 0 ))
subcircuit.inst(Gates.SwapGate( 1, 4 ))
subcircuit.inst(Gates.RYYGate(p_a7734b)( 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(p_c8b7aa, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_10c631, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_d40aec, 4, 0 ))
circuit.inst(Gates.CRXGate(p_8f9e53, 4, 6 ))
circuit.inst(Gates.CHGate( 4, 0 ))

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
    "p_d40aec": 3.2142159669963557,
    "p_10c631": 4.229610589867865,
    "p_a7734b": 0.5501056885328758,
    "p_c8b7aa": 2.0099472182748075,
    "p_8f9e53": 5.94477504571567,
    "p_da6dd8": 6.163759533339787,
    "p_7f634a": 2.008796895454228
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

