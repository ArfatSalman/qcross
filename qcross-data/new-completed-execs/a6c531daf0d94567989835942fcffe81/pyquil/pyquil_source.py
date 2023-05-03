
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CU1Gate", "CXGate", "CRXGate", "CPhaseGate", "U2Gate", "PhaseGate", "CSXGate", "U3Gate", "DCXGate", "SXGate", "CRZGate", "SwapGate")

circuit += defns

circuit.inst(Gates.U3Gate(1.2333979366062962, 0.8994966515664887, 3.0003132360957094)( 1 ))
circuit.inst(Gates.SwapGate( 5, 0 ))
circuit.inst(Gates.CU1Gate(5.8809885406034885, 4, 0 ))
circuit.inst(Gates.CSXGate( 0, 3 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CPhaseGate(4.661904537785083, 4, 6 ))
circuit.inst(Gates.U3Gate(6.161570642375718, 0.7126827811277849, 1.428988687288719)( 5 ))
circuit.inst(Gates.CRZGate(2.777640838880794, 0, 3 ))
circuit.inst(Gates.SwapGate( 0, 4 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.U2Gate(1.9012707343238924, 6.017351377795965)( 3 ))
circuit.inst(Gates.U2Gate(1.3178440304272925, 3.434672943879739)( 3 ))
circuit.inst(Gates.DCXGate( 1, 6 ))
circuit.inst(Gates.U3Gate(2.0260584085672413, 5.46425242678673, 4.443597328220221)( 5 ))
circuit.inst(Gates.DCXGate( 4, 1 ))
circuit.inst(Gates.CXGate( 2, 3 ))
circuit.inst(Gates.CRXGate(0.47168664474085104, 4, 2 ))
circuit.inst(Gates.PhaseGate(5.273838382452584, 3 ))
circuit.inst(Gates.PhaseGate(0.6110285192622922, 5 ))

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





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

