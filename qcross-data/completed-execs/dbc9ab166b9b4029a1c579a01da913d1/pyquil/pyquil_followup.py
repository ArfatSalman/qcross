
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_c69e12 = circuit.declare('p_c69e12', 'REAL')
p_23fe7b = circuit.declare('p_23fe7b', 'REAL')
p_3b83fb = circuit.declare('p_3b83fb', 'REAL')
p_d5ab30 = circuit.declare('p_d5ab30', 'REAL')
p_9f1173 = circuit.declare('p_9f1173', 'REAL')
p_8cc75e = circuit.declare('p_8cc75e', 'REAL')
p_ed89c2 = circuit.declare('p_ed89c2', 'REAL')
p_f1fd0a = circuit.declare('p_f1fd0a', 'REAL')

defns = get_custom_get_definitions("IGate", "XGate", "RZGate", "ZGate", "RCCXGate", "SGate", "CSXGate", "PhaseGate", "CHGate", "CRXGate", "C3SXGate", "ECRGate", "SdgGate", "TGate", "CU1Gate", "CRZGate", "U2Gate")

circuit += defns

circuit.inst(Gates.RZGate(p_f1fd0a, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))

subcircuit = Program()
subcircuit.inst(Gates.TGate( 0 ))
subcircuit.inst(Gates.IGate( 3 ))
subcircuit.inst(Gates.PhaseGate(0.4827903095199283, 6 ))
subcircuit.inst(Gates.RZGate(1.2484842640635918, 0 ))
subcircuit.inst(Gates.CRZGate(4.747288222618085, 1, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(p_9f1173, 1 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.CRXGate(p_d5ab30, 4, 6 ))
circuit.inst(Gates.CHGate( 4, 0 ))
circuit.inst(Gates.C3SXGate( 2, 0, 3, 4 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.CRZGate(p_3b83fb, 0, 6 ))
circuit.inst(Gates.CU1Gate(p_8cc75e, 1, 4 ))
circuit.inst(Gates.C3SXGate( 2, 0, 5, 4 ))
circuit.inst(Gates.CRZGate(p_23fe7b, 6, 2 ))
circuit.inst(Gates.U2Gate(p_c69e12, p_ed89c2)( 2 ))

qr_ef5c94 = circuit.declare("qr_ef5c94", "BIT", 8)

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
    "p_c69e12": 2.5163050709890156,
    "p_23fe7b": 2.586208953975239,
    "p_3b83fb": 4.833923139882297,
    "p_d5ab30": 5.94477504571567,
    "p_9f1173": 4.229610589867865,
    "p_8cc75e": 4.028174522740928,
    "p_ed89c2": 2.1276323672732023,
    "p_f1fd0a": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

