
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_435d0d = circuit.declare('p_435d0d', 'REAL')
p_3c07ca = circuit.declare('p_3c07ca', 'REAL')
p_ccc6de = circuit.declare('p_ccc6de', 'REAL')
p_f9d2fd = circuit.declare('p_f9d2fd', 'REAL')
p_6b41c3 = circuit.declare('p_6b41c3', 'REAL')
p_8c914c = circuit.declare('p_8c914c', 'REAL')

defns = get_custom_get_definitions("CPhaseGate", "PhaseGate", "CHGate", "U1Gate", "UGate")

circuit += defns

circuit.inst(Gates.CPhaseGate(p_6b41c3, 1, 2 ))
circuit.inst(Gates.U1Gate(p_3c07ca, 2 ))
circuit.inst(Gates.UGate(p_f9d2fd, p_435d0d, p_ccc6de)( 2 ))
circuit.inst(Gates.PhaseGate(p_8c914c, 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_435d0d": 1.2201500361327853,
    "p_3c07ca": 5.072633818750175,
    "p_ccc6de": 4.276690396183425,
    "p_f9d2fd": 3.8090985869250003,
    "p_6b41c3": 1.7910282654595102,
    "p_8c914c": 2.482034489972267
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

