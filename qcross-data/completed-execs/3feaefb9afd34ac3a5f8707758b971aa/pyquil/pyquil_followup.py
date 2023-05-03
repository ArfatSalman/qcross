
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("U2Gate", "CHGate", "ZGate", "CXGate", "YGate", "C3SXGate", "RZXGate", "HGate", "RYYGate", "U1Gate", "CUGate", "CZGate", "SXdgGate", "UGate", "SXGate")

circuit += defns

circuit.inst(Gates.RZXGate(3.813624597382902)( 1, 7 ))
circuit.inst(Gates.HGate( 3 ))
circuit.inst(Gates.U1Gate(1.7474579084583979, 5 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.CZGate( 1, 2 ))
circuit.inst(Gates.U1Gate(2.3042652898695457, 6 ))
circuit.inst(Gates.UGate(2.879770697683128, 2.335112883423633, 4.1410857855717005)( 0 ))
circuit.inst(Gates.ZGate( 5 ))
circuit.inst(Gates.U2Gate(4.529061112043725, 0.1128558241378929)( 3 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.SXGate( 4 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.CXGate( 2, 3 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.U1Gate(2.0589291173378608, 5 ))
circuit.inst(Gates.C3SXGate( 6, 4, 2, 7 ))
circuit.inst(Gates.CHGate( 1, 7 ))
circuit.inst(Gates.RYYGate(0.1445200040685528)( 2, 6 ))
circuit.inst(Gates.SXdgGate( 4 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CUGate(2.2742238751077037, 5.678583788689636, 5.945356410023023, 1.2692738094959353, 5, 2 ))
circuit.inst(Gates.YGate( 5 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.C3SXGate( 0, 3, 5, 7 ))

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

