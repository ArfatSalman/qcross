
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("SXdgGate", "CU3Gate", "CXGate", "HGate", "RYYGate", "UGate", "U1Gate", "ECRGate", "RZZGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.ECRGate( 7, 1 ))
subcircuit.inst(Gates.CXGate( 6, 0 ))
subcircuit.inst(Gates.SXdgGate( 4 ))
subcircuit.inst(Gates.HGate( 6 ))
subcircuit.inst(Gates.RZZGate(1.1809864697709562)( 0, 6 ))
subcircuit.inst(Gates.U1Gate(3.0511475243475985, 3 ))
subcircuit.inst(Gates.UGate(1.758300519432271, 2.7759984582269563, 5.130578246510858)( 1 ))
subcircuit.inst(Gates.RYYGate(2.8616233109786804)( 5, 2 ))
subcircuit.inst(Gates.CU3Gate(5.782992008877923, 2.583390532654726, 3.229621753302509, 6, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())


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




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

