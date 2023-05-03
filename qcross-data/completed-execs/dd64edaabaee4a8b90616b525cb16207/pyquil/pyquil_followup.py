
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 8)

p_31eb9a = circuit.declare('p_31eb9a', 'REAL')
p_2f614c = circuit.declare('p_2f614c', 'REAL')
p_0aa758 = circuit.declare('p_0aa758', 'REAL')
p_98af8b = circuit.declare('p_98af8b', 'REAL')
p_296b91 = circuit.declare('p_296b91', 'REAL')
p_704f8c = circuit.declare('p_704f8c', 'REAL')

defns = get_custom_get_definitions("RYYGate", "C3SXGate", "XGate", "ZGate", "RZGate", "RYGate", "CRZGate", "CRXGate", "CU1Gate", "SXGate")

circuit += defns

circuit.inst(Gates.RZGate(p_31eb9a, 4 ))
circuit.inst(Gates.ZGate( 6 ))
circuit.inst(Gates.XGate( 6 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 6 ))
circuit.inst(Gates.CRZGate(p_704f8c, 1, 6 ))
circuit.inst(Gates.C3SXGate( 0, 7, 6, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 1 ))

subcircuit = Program()
subcircuit.inst(Gates.RYGate(2.936349225876477, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RYYGate(p_98af8b)( 6, 7 ))
circuit.inst(Gates.CRZGate(p_0aa758, 1, 7 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_296b91, 4, 0 ))
circuit.inst(Gates.CRXGate(p_2f614c, 6, 4 ))

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
    "p_31eb9a": 6.163759533339787,
    "p_2f614c": 5.94477504571567,
    "p_0aa758": 4.167661441102218,
    "p_98af8b": 1.740253089260498,
    "p_296b91": 3.2142159669963557,
    "p_704f8c": 1.0296448789776642
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

