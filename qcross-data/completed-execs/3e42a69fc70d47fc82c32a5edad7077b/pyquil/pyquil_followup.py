
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_01ce9b = circuit.declare('p_01ce9b', 'REAL')
p_4f7ff2 = circuit.declare('p_4f7ff2', 'REAL')
p_17defe = circuit.declare('p_17defe', 'REAL')
p_e7ae71 = circuit.declare('p_e7ae71', 'REAL')
p_17befe = circuit.declare('p_17befe', 'REAL')

defns = get_custom_get_definitions("CUGate", "SXGate", "C3XGate", "ZGate", "U1Gate", "RZXGate", "CYGate", "RZGate", "CPhaseGate", "XGate", "C3SXGate", "CCXGate", "CRZGate", "TGate")

circuit += defns

circuit.inst(Gates.RZGate(p_4f7ff2, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_17defe, 2, 4 ))
circuit.inst(Gates.CUGate(p_e7ae71, p_17befe, 2.3864521352475245, p_01ce9b, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))

subcircuit = Program()
subcircuit.inst(Gates.U1Gate(6.2047416485134805, 0 ))
subcircuit.inst(Gates.CPhaseGate(4.63837786161633, 0, 2 ))
subcircuit.inst(Gates.RZXGate(4.563562108824195)( 4, 0 ))
subcircuit.inst(Gates.C3XGate( 4, 5, 2, 1 ))
subcircuit.inst(Gates.XGate( 4 ))
subcircuit.inst(Gates.CYGate( 2, 0 ))
subcircuit.inst(Gates.SXGate( 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_01ce9b": 5.987304452123941,
    "p_4f7ff2": 6.163759533339787,
    "p_17defe": 4.2641612072511235,
    "p_e7ae71": 0.5112149185250571,
    "p_17befe": 5.897054719225356
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

