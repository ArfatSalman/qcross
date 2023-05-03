
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("CPhaseGate", "ZGate", "CUGate", "RCCXGate", "CHGate", "CRXGate", "SXdgGate", "RZGate", "HGate", "SdgGate", "XGate", "CYGate", "RYYGate", "TdgGate", "CRZGate", "TGate", "YGate", "SGate", "iSwapGate", "CZGate", "ECRGate", "CCXGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 1, 0 ))
circuit.inst(Gates.ZGate( 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CUGate(1.3471739101750193, 3.2142159669963557, 2.852678572380205, 3.5173414605326783, 1, 0 ))
subcircuit.inst(Gates.YGate( 1 ))
subcircuit.inst(Gates.CPhaseGate(1.4112277317699358, 2, 1 ))
subcircuit.inst(Gates.HGate( 0 ))
subcircuit.inst(Gates.CYGate( 2, 0 ))
subcircuit.inst(Gates.CZGate( 0, 1 ))
subcircuit.inst(Gates.CRZGate(5.091930552861214, 0, 2 ))
subcircuit.inst(Gates.SGate( 2 ))
subcircuit.inst(Gates.TdgGate( 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.ECRGate( 2, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RCCXGate( 1, 0, 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.RCCXGate( 0, 2, 1 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 2, 1 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CRZGate(0.05525155902669336, 2, 1 ))
circuit.inst(Gates.RYYGate(3.2287759437031154)( 1, 2 ))
circuit.inst(Gates.RYYGate(5.398622178940033)( 0, 2 ))

qr_1652f1 = circuit.declare("qr_1652f1", "BIT", 2)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

