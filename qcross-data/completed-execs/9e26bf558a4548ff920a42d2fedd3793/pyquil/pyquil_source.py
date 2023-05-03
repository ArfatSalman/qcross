
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("CCXGate", "CSXGate", "RYYGate", "CU1Gate", "CSwapGate", "RC3XGate", "XGate", "iSwapGate", "CRYGate", "IGate", "CPhaseGate", "CZGate", "U2Gate")

circuit += defns

circuit.inst(Gates.CSXGate( 2, 3 ))
circuit.inst(Gates.CCXGate( 0, 1, 4 ))
circuit.inst(Gates.RYYGate(3.630000846740864)( 4, 0 ))
circuit.inst(Gates.XGate( 4 ))
circuit.inst(Gates.RC3XGate( 4, 2, 1, 3 ))
circuit.inst(Gates.CU1Gate(2.3801704973111244, 1, 3 ))
circuit.inst(Gates.RYYGate(2.26249791419463)( 3, 2 ))
circuit.inst(Gates.IGate( 4 ))
circuit.inst(Gates.U2Gate(0.024205049091638117, 3.6641337073605276)( 4 ))
circuit.inst(Gates.CRYGate(0.5432436418208648, 3, 2 ))
circuit.inst(Gates.CPhaseGate(2.5556929743025827, 0, 2 ))
circuit.inst(Gates.IGate( 3 ))
circuit.inst(Gates.CZGate( 3, 2 ))
circuit.inst(Gates.CU1Gate(2.849292498056443, 3, 0 ))
circuit.inst(Gates.CSwapGate( 0, 3, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.iSwapGate( 4, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

