
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)

p_22f003 = circuit.declare('p_22f003', 'REAL')
p_b0e1f1 = circuit.declare('p_b0e1f1', 'REAL')
p_74570c = circuit.declare('p_74570c', 'REAL')
p_2ab273 = circuit.declare('p_2ab273', 'REAL')
p_0e1639 = circuit.declare('p_0e1639', 'REAL')

defns = get_custom_get_definitions("RYYGate", "XGate", "CCXGate", "ECRGate", "ZGate", "PhaseGate", "CRZGate", "RCCXGate", "U2Gate", "RZGate", "SdgGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(p_22f003, 6, 2 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 7 ))
circuit.inst(Gates.RCCXGate( 10, 6, 8 ))
circuit.inst(Gates.RZGate(p_74570c, 0 ))
circuit.inst(Gates.CCXGate( 7, 10, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.RZGate(4.940217775579305, 1 ))
subcircuit.inst(Gates.RYYGate(0.6724371252296606)( 9, 0 ))
subcircuit.inst(Gates.PhaseGate(p_0e1639, 0 ))
subcircuit.inst(Gates.ECRGate( 3, 0 ))
subcircuit.inst(Gates.PhaseGate(p_2ab273, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.U2Gate(4.214504315296764, p_b0e1f1)( 10 ))

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



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 11)


circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_22f003": 4.2641612072511235,
    "p_b0e1f1": 4.6235667602042065,
    "p_74570c": 4.229610589867865,
    "p_2ab273": 0.4827903095199283,
    "p_0e1639": 5.5146057452272546
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

