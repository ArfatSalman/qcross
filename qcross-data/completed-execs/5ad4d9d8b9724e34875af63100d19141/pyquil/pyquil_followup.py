
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"NAIVE"']) )

qr = circuit.declare("ro", "BIT", 7)

p_bb87af = circuit.declare('p_bb87af', 'REAL')

defns = get_custom_get_definitions("RZXGate", "C3XGate", "CHGate", "RXGate", "RCCXGate", "CZGate", "IGate", "CYGate", "CRXGate", "XGate", "ECRGate", "C3SXGate", "SdgGate", "RZGate", "ZGate")

circuit += defns

circuit.inst(Gates.RZGate(p_bb87af, 4 ))
circuit.inst(Gates.ZGate( 6 ))

subcircuit = Program()
subcircuit.inst(Gates.CZGate( 4, 1 ))
subcircuit.inst(Gates.IGate( 1 ))
subcircuit.inst(Gates.RXGate(0.2906326206587185, 0 ))
subcircuit.inst(Gates.RZXGate(4.563562108824195)( 4, 0 ))
subcircuit.inst(Gates.C3XGate( 4, 6, 2, 1 ))
subcircuit.inst(Gates.XGate( 4 ))
subcircuit.inst(Gates.CYGate( 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 2, 5 ))
circuit.inst(Gates.C3SXGate( 6, 0, 1, 2 ))
circuit.inst(Gates.CHGate( 4, 6 ))
circuit.inst(Gates.C3SXGate( 0, 2, 1, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.ECRGate( 6, 3 ))
circuit.inst(Gates.SdgGate( 6 ))
circuit.inst(Gates.RCCXGate( 2, 5, 0 ))

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
    "p_bb87af": 6.163759533339787
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

