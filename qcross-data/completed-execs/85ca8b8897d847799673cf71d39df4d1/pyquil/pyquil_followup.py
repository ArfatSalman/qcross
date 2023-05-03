
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("CRYGate", "U2Gate", "CHGate", "DCXGate", "RZZGate", "TGate", "CZGate", "CU3Gate", "RXGate", "SwapGate", "RZGate", "RYYGate", "RYGate", "CUGate", "U3Gate")

circuit += defns

circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CUGate(2.0087468885271504, 5.883811190278971, 5.864947219205212, 5.7446598664897115, 1, 0 ))
circuit.inst(Gates.RXGate(5.794504209717704, 1 ))
circuit.inst(Gates.RZZGate(2.1663122372864825)( 1, 0 ))
circuit.inst(Gates.DCXGate( 1, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.U2Gate(3.615801062466814, 0.8936944779843444)( 1 ))
circuit.inst(Gates.RYGate(2.2562188139100248, 1 ))
circuit.inst(Gates.RYYGate(6.060522892419086)( 1, 0 ))
circuit.inst(Gates.SwapGate( 0, 1 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SwapGate( 0, 1 ))
circuit.inst(Gates.U3Gate(3.8927238245726374, 2.0377807006749333, 4.064217417062462)( 0 ))
circuit.inst(Gates.RZGate(2.414915889738904, 1 ))
circuit.inst(Gates.CRYGate(2.594321777907923, 1, 0 ))
circuit.inst(Gates.RXGate(2.3571868764276998, 1 ))
circuit.inst(Gates.RZZGate(0.3644709100093532)( 0, 1 ))
circuit.inst(Gates.RXGate(2.5276999718154167, 1 ))
circuit.inst(Gates.CZGate( 1, 0 ))
circuit.inst(Gates.RZZGate(3.41477281916325)( 1, 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.U3Gate(5.170631856240322, 2.9463190555168968, 2.269493738638121)( 0 ))
circuit.inst(Gates.U3Gate(2.481557449187282, 3.06771330185138, 2.2732733996544363)( 1 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.CUGate(0.8725199162352276, 2.0033484721527364, 1.6015864357317902, 4.9684596562340495, 1, 0 ))
circuit.inst(Gates.RYGate(5.8249335523617525, 0 ))
circuit.inst(Gates.RZGate(4.757508594558637, 0 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(Gates.CU3Gate(3.137732232950496, 2.9454453048301827, 2.754468708884141, 0, 1 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

