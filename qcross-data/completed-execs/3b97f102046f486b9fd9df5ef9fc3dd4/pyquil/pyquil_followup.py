
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"PARTIAL"']) )

qr = circuit.declare("ro", "BIT", 4)

p_26bdc5 = circuit.declare('p_26bdc5', 'REAL')
p_ef51d2 = circuit.declare('p_ef51d2', 'REAL')
p_b28578 = circuit.declare('p_b28578', 'REAL')
p_129651 = circuit.declare('p_129651', 'REAL')
p_ca72f6 = circuit.declare('p_ca72f6', 'REAL')
p_6111a3 = circuit.declare('p_6111a3', 'REAL')
p_04934c = circuit.declare('p_04934c', 'REAL')

defns = get_custom_get_definitions("CHGate", "CUGate", "TdgGate", "RZZGate", "RZGate", "RXGate", "PhaseGate", "CXGate", "iSwapGate", "C3SXGate", "CRYGate", "CU1Gate", "U1Gate", "XGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_26bdc5, 1 ))
circuit.inst(Gates.RZZGate(p_b28578)( 2, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.TdgGate( 2 ))
subcircuit.inst(Gates.U1Gate(5.01836135520768, 1 ))
subcircuit.inst(Gates.CRYGate(4.736752714049485, 0, 3 ))
subcircuit.inst(Gates.RXGate(6.1292830756636185, 2 ))
subcircuit.inst(Gates.CHGate( 2, 3 ))
subcircuit.inst(Gates.CXGate( 2, 0 ))
subcircuit.inst(Gates.RZZGate(3.516607467010828)( 3, 1 ))
subcircuit.inst(Gates.PhaseGate(3.2287759437031154, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(p_ef51d2, p_ca72f6, p_6111a3, p_129651, 0, 2 ))
circuit.inst(Gates.CU1Gate(p_04934c, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_26bdc5": 6.163759533339787,
    "p_ef51d2": 0.5112149185250571,
    "p_b28578": 4.066449154047175,
    "p_129651": 5.987304452123941,
    "p_ca72f6": 5.897054719225356,
    "p_6111a3": 2.3864521352475245,
    "p_04934c": 5.154187354656876
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

