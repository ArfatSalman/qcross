
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_1b0063 = circuit.declare('p_1b0063', 'REAL')
p_43b9a6 = circuit.declare('p_43b9a6', 'REAL')
p_831b02 = circuit.declare('p_831b02', 'REAL')
p_0584aa = circuit.declare('p_0584aa', 'REAL')
p_40c0da = circuit.declare('p_40c0da', 'REAL')
p_d34f58 = circuit.declare('p_d34f58', 'REAL')
p_aed827 = circuit.declare('p_aed827', 'REAL')

defns = get_custom_get_definitions("RZXGate", "CCXGate", "CUGate", "CXGate", "SXdgGate", "iSwapGate", "U2Gate", "TGate", "XGate", "CRXGate", "RZGate", "CSXGate", "ZGate", "RCCXGate", "SXGate", "SwapGate", "CHGate", "C3SXGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_831b02, 3 ))
circuit.inst(Gates.CRZGate(p_0584aa, 6, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.RZXGate(1.1412693567569159)( 1, 8 ))
subcircuit.inst(Gates.SwapGate( 1, 7 ))
subcircuit.inst(Gates.iSwapGate( 2, 7 ))
subcircuit.inst(Gates.RCCXGate( 2, 0, 5 ))
subcircuit.inst(Gates.CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004, 3, 1 ))
subcircuit.inst(Gates.CXGate( 8, 9 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(p_d34f58, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(p_43b9a6, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(p_1b0063, 1, 2 ))
circuit.inst(Gates.U2Gate(p_aed827, p_40c0da)( 2 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SXdgGate( 9 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_1b0063": 2.586208953975239,
    "p_43b9a6": 4.229610589867865,
    "p_831b02": 6.163759533339787,
    "p_0584aa": 4.2641612072511235,
    "p_40c0da": 2.1276323672732023,
    "p_d34f58": 5.987304452123941,
    "p_aed827": 2.5163050709890156
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

