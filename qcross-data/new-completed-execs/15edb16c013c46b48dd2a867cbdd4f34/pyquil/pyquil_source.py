
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("RZZGate", "SXdgGate", "ECRGate", "DCXGate", "SXGate", "CUGate", "CRYGate", "CRXGate", "C4XGate", "RGate", "CU3Gate", "CRZGate", "RYGate")

circuit += defns

circuit.inst(Gates.RGate(1.3462943863788401, 2.0625679674283215)( 2 ))
circuit.inst(Gates.RYGate(3.7263733381135333, 4 ))
circuit.inst(Gates.CRZGate(3.624574776344154, 7, 3 ))
circuit.inst(Gates.CUGate(2.7575077791457248, 2.0665317573057798, 5.876304122002991, 5.455724865836178, 3, 0 ))
circuit.inst(Gates.RZZGate(6.059622421697095)( 2, 6 ))
circuit.inst(Gates.C4XGate( 0, 4, 1, 5, 6 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.ECRGate( 2, 4 ))
circuit.inst(Gates.SXdgGate( 6 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.CRZGate(3.472333959218345, 7, 3 ))
circuit.inst(Gates.CRYGate(2.364247849527231, 7, 1 ))
circuit.inst(Gates.CRZGate(0.8522442036798011, 6, 4 ))
circuit.inst(Gates.RGate(0.44671874703610037, 4.595620654661833)( 3 ))
circuit.inst(Gates.SXGate( 3 ))
circuit.inst(Gates.DCXGate( 1, 5 ))
circuit.inst(Gates.CUGate(2.010079880074799, 3.570167881942785, 3.7199764092307213, 0.8777762419082662, 6, 4 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.CRXGate(5.895791450120457, 0, 5 ))
circuit.inst(Gates.CU3Gate(2.3777076314685166, 0.2787777190001789, 6.013755670278601, 5, 6 ))

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





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

