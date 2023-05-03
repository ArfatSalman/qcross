
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("RVGate", "RXGate", "CU3Gate", "HGate", "CRXGate", "CPhaseGate", "RZZGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.CRXGate(6.189367290017951, 6, 0 ))
subcircuit.inst(Gates.HGate( 1 ))
subcircuit.inst(Gates.CU3Gate(3.795093132245643, 5.482804960064541, 3.392543408251406, 0, 6 ))
subcircuit.inst(Gates.RXGate(2.870607397554538, 4 ))
subcircuit.inst(Gates.CPhaseGate(4.002346068007423, 3, 0 ))
subcircuit.inst(Gates.RVGate(4.068029717857408, 0.567304873816878, 3.215798805925656)( 6 ))
subcircuit.inst(Gates.RZZGate(3.9665175003040227)( 0, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())


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




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

