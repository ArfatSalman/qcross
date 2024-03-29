
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)

p_35205c = circuit.declare('p_35205c', 'REAL')
p_5601c2 = circuit.declare('p_5601c2', 'REAL')
p_cd242e = circuit.declare('p_cd242e', 'REAL')
p_d80ef0 = circuit.declare('p_d80ef0', 'REAL')

defns = get_custom_get_definitions("C3SXGate", "CSXGate", "SXdgGate", "RYYGate", "CXGate", "C3XGate", "RZZGate", "RZGate", "CU1Gate", "CRXGate", "ZGate", "SwapGate", "XGate", "CRZGate", "PhaseGate", "SXGate", "CSwapGate")

circuit += defns

circuit.inst(Gates.RZGate(p_5601c2, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(1.0296448789776642, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 6, 7 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_35205c, 4, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.CSwapGate( 0, 5, 4 ))
subcircuit.inst(Gates.CSXGate( 4, 0 ))
subcircuit.inst(Gates.SwapGate( 1, 4 ))
subcircuit.inst(Gates.RYYGate(0.5501056885328758)( 2, 0 ))
subcircuit.inst(Gates.SXdgGate( 2 ))
subcircuit.inst(Gates.C3XGate( 6, 5, 4, 7 ))
subcircuit.inst(Gates.CXGate( 2, 3 ))
subcircuit.inst(Gates.PhaseGate(p_cd242e, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRXGate(5.94477504571567, 6, 4 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 7, 0 ))
circuit.inst(Gates.CSXGate( 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_35205c": 3.2142159669963557,
    "p_5601c2": 6.163759533339787,
    "p_cd242e": 1.7897858384938228,
    "p_d80ef0": 2.6687018103754414
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

