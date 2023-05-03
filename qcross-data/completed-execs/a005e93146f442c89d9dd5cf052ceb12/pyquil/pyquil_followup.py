
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("CCXGate", "CU1Gate", "CRZGate", "CUGate", "RYYGate", "PhaseGate", "RZZGate", "DCXGate", "CXGate", "SXGate", "RZGate", "UGate", "SGate", "SXdgGate", "RCCXGate", "TGate", "ZGate", "C3SXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 2 ))
circuit.inst(Gates.ZGate( 4 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 1, 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 1, 4 ))
circuit.inst(Gates.C3SXGate( 3, 2, 0, 1 ))
circuit.inst(Gates.CCXGate( 3, 5, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.RYYGate(0.5501056885328758)( 1, 0 ))
subcircuit.inst(Gates.SXdgGate( 2 ))
subcircuit.inst(Gates.DCXGate( 3, 1 ))
subcircuit.inst(Gates.RYYGate(0.6724371252296606)( 0, 5 ))
subcircuit.inst(Gates.CXGate( 1, 0 ))
subcircuit.inst(Gates.PhaseGate(5.5146057452272546, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 2, 4, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.RCCXGate( 5, 4, 2 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 3, 5 ))
circuit.inst(Gates.RZGate(4.229610589867865, 3 ))
circuit.inst(Gates.C3SXGate( 0, 1, 3, 4 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 4, 0 ))
circuit.inst(Gates.UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358)( 5 ))
circuit.inst(Gates.RZZGate(5.1829934776392745)( 0, 5 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CRZGate(4.833923139882297, 0, 5 ))
circuit.inst(Gates.CU1Gate(4.028174522740928, 3, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(3, qr[1])
circuit += MEASURE(1, qr[2])
circuit += MEASURE(4, qr[3])
circuit += MEASURE(2, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

