
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_44bd2b = circuit.declare('p_44bd2b', 'REAL')
p_2e218a = circuit.declare('p_2e218a', 'REAL')

defns = get_custom_get_definitions("SwapGate", "U1Gate", "RZGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.U1Gate(p_2e218a, 2 ))
subcircuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(p_44bd2b, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_44bd2b": 6.163759533339787,
    "p_2e218a": 6.225782237242023
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

