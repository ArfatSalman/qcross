
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_ec106f = circuit.declare('p_ec106f', 'REAL')
p_5f113d = circuit.declare('p_5f113d', 'REAL')
p_cf8439 = circuit.declare('p_cf8439', 'REAL')
p_7e38fe = circuit.declare('p_7e38fe', 'REAL')
p_50c455 = circuit.declare('p_50c455', 'REAL')
p_e13c2b = circuit.declare('p_e13c2b', 'REAL')

defns = get_custom_get_definitions("UGate", "IGate", "U3Gate", "RZGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_ec106f, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.U3Gate(p_7e38fe, p_5f113d, 0.4903361071050254)( 1 ))
subcircuit.inst(Gates.IGate( 2 ))
subcircuit.inst(Gates.UGate(p_e13c2b, p_50c455, p_cf8439)( 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 2 ))

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
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_ec106f": 6.163759533339787,
    "p_5f113d": 5.154187354656876,
    "p_cf8439": 1.2128092629174942,
    "p_7e38fe": 4.094867647151279,
    "p_50c455": 5.190931186022931,
    "p_e13c2b": 5.01836135520768
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

