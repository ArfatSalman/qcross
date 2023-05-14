
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_fa5922 = circuit.declare('p_fa5922', 'REAL')
p_1464bc = circuit.declare('p_1464bc', 'REAL')
p_03ad92 = circuit.declare('p_03ad92', 'REAL')
p_d5daad = circuit.declare('p_d5daad', 'REAL')
p_72766f = circuit.declare('p_72766f', 'REAL')

defns = get_custom_get_definitions("SdgGate", "RCCXGate", "RYYGate", "C3SXGate", "CRZGate", "CSXGate", "CRXGate", "XGate", "CU1Gate", "HGate", "SXdgGate", "RZGate", "ECRGate", "SGate", "ZGate", "CHGate", "SwapGate", "RZZGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.HGate( 0 ))
subcircuit.inst(Gates.RZZGate(p_03ad92)( 0, 5 ))
subcircuit.inst(Gates.CRZGate(p_1464bc, 0, 5 ))
subcircuit.inst(Gates.CSXGate( 4, 0 ))
subcircuit.inst(Gates.SwapGate( 1, 4 ))
subcircuit.inst(Gates.RYYGate(0.5501056885328758)( 2, 0 ))
subcircuit.inst(Gates.SXdgGate( 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(p_d5daad, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_fa5922, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_72766f, 4, 0 ))
circuit.inst(Gates.CRXGate(5.94477504571567, 4, 6 ))

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
    "p_fa5922": 4.229610589867865,
    "p_1464bc": 2.008796895454228,
    "p_03ad92": 5.017245588344839,
    "p_d5daad": 2.0099472182748075,
    "p_72766f": 3.2142159669963557
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

