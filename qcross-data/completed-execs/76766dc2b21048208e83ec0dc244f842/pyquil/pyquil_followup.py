
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)

p_bec6f4 = circuit.declare('p_bec6f4', 'REAL')
p_6e47ec = circuit.declare('p_6e47ec', 'REAL')
p_b52923 = circuit.declare('p_b52923', 'REAL')
p_b0edf1 = circuit.declare('p_b0edf1', 'REAL')
p_7fdf26 = circuit.declare('p_7fdf26', 'REAL')
p_c19a9b = circuit.declare('p_c19a9b', 'REAL')
p_4a7236 = circuit.declare('p_4a7236', 'REAL')
p_eca484 = circuit.declare('p_eca484', 'REAL')
p_7c75a3 = circuit.declare('p_7c75a3', 'REAL')

defns = get_custom_get_definitions("RCCXGate", "RXXGate", "CPhaseGate", "CXGate", "SXGate", "CRXGate", "XGate", "CCXGate", "RZGate", "ZGate", "U2Gate", "TGate", "CRZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_4a7236, 3 ))
circuit.inst(Gates.CRZGate(p_7fdf26, 6, 3 ))
circuit.inst(Gates.CRXGate(p_bec6f4, 1, 7 ))

subcircuit = Program()
subcircuit.inst(Gates.CPhaseGate(4.63837786161633, 3, 0 ))
subcircuit.inst(Gates.U2Gate(p_c19a9b, p_b0edf1)( 8 ))
subcircuit.inst(Gates.CXGate( 2, 4 ))
subcircuit.inst(Gates.SXGate( 0 ))
subcircuit.inst(Gates.CRZGate(p_b52923, 0, 5 ))
subcircuit.inst(Gates.RCCXGate( 9, 1, 8 ))
subcircuit.inst(Gates.RXXGate(p_6e47ec)( 4, 6 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(p_7c75a3, 1, 6 ))
circuit.inst(Gates.RZGate(p_eca484, 1 ))

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




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_bec6f4": 5.987304452123941,
    "p_6e47ec": 5.25962645863375,
    "p_b52923": 2.008796895454228,
    "p_b0edf1": 0.07157463504881167,
    "p_7fdf26": 4.2641612072511235,
    "p_c19a9b": 5.887184334931191,
    "p_4a7236": 6.163759533339787,
    "p_eca484": 4.229610589867865,
    "p_7c75a3": 4.167661441102218
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

