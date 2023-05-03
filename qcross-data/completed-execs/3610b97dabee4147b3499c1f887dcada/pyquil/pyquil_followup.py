
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("SXdgGate", "RZGate", "CSXGate", "SGate", "CHGate", "CRXGate", "RYYGate", "CZGate", "UGate", "ECRGate", "DCXGate", "TGate", "CPhaseGate", "CUGate", "CRZGate", "RC3XGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.ECRGate( 3, 2 ))
circuit.inst(Gates.CRXGate(2.0099472182748075, 4, 3 ))
circuit.inst(Gates.SGate( 0 ))

subcircuit = Program()
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.UGate(5.01836135520768, 5.190931186022931, 1.2128092629174942)( 3 ))
subcircuit.inst(Gates.RC3XGate( 4, 0, 3, 1 ))
subcircuit.inst(Gates.DCXGate( 2, 3 ))
subcircuit.inst(Gates.CZGate( 1, 0 ))
subcircuit.inst(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547, 0, 1 ))
subcircuit.inst(Gates.CPhaseGate(4.63837786161633, 0, 2 ))
subcircuit.inst(Gates.ECRGate( 3, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CRZGate(1.0296448789776642, 3, 4 ))
circuit.inst(Gates.CHGate( 1, 4 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 0, 2 ))

qr_95bd5e = circuit.declare("qr_95bd5e", "BIT", 4)

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

