
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_697101 = circuit.declare('p_697101', 'REAL')
p_5a355d = circuit.declare('p_5a355d', 'REAL')
p_eb0661 = circuit.declare('p_eb0661', 'REAL')
p_219124 = circuit.declare('p_219124', 'REAL')
p_31ccf5 = circuit.declare('p_31ccf5', 'REAL')
p_c0bd09 = circuit.declare('p_c0bd09', 'REAL')
p_f7209d = circuit.declare('p_f7209d', 'REAL')
p_c4e7fa = circuit.declare('p_c4e7fa', 'REAL')

defns = get_custom_get_definitions("CRZGate", "ECRGate", "U2Gate", "iSwapGate", "C3SXGate", "RCCXGate", "CRXGate", "CU1Gate", "SGate", "RZGate", "XGate", "CSXGate", "ZGate", "SdgGate", "CPhaseGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(p_c0bd09, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(p_697101, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(p_c4e7fa, 4, 0 ))
circuit.inst(Gates.CRXGate(p_f7209d, 4, 6 ))
circuit.inst(Gates.CHGate( 4, 0 ))
circuit.inst(Gates.C3SXGate( 2, 0, 3, 4 ))
circuit.inst(Gates.CSXGate( 0, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.iSwapGate( 1, 6 ))
subcircuit.inst(Gates.CPhaseGate(p_31ccf5, 0, 6 ))
subcircuit.inst(Gates.CU1Gate(2.0685963035149753, 4, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 6 ))
circuit.inst(Gates.CU1Gate(p_5a355d, 1, 4 ))
circuit.inst(Gates.C3SXGate( 2, 0, 5, 4 ))
circuit.inst(Gates.CRZGate(p_eb0661, 6, 2 ))
circuit.inst(Gates.U2Gate(p_219124, 2.1276323672732023)( 2 ))

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
    "p_697101": 2.0099472182748075,
    "p_5a355d": 4.028174522740928,
    "p_eb0661": 2.586208953975239,
    "p_219124": 2.5163050709890156,
    "p_31ccf5": 3.326780904591333,
    "p_c0bd09": 6.163759533339787,
    "p_f7209d": 5.94477504571567,
    "p_c4e7fa": 3.2142159669963557
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

