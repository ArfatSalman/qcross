
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("SXdgGate", "CHGate", "RXXGate", "RXGate", "ZGate", "RYYGate", "XGate", "iSwapGate", "RZXGate", "SXGate", "CYGate", "ECRGate", "CRZGate", "RGate", "SGate")

circuit += defns

circuit.inst(Gates.RYYGate(0.040332757463886044)( 1, 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.RZXGate(2.0199977459798464)( 0, 1 ))
circuit.inst(Gates.RXXGate(3.927829733740478)( 1, 0 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.CRZGate(5.451741496819523, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RXXGate(2.6277753952279403)( 0, 1 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.ZGate( 1 ))
circuit.inst(Gates.CRZGate(3.555542082325973, 0, 1 ))
circuit.inst(Gates.RYYGate(5.488061464125162)( 0, 1 ))
circuit.inst(Gates.RXGate(3.657037356032689, 0 ))
circuit.inst(Gates.RXGate(4.976946713501052, 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RGate(5.88245539296814, 5.313337512106651)( 1 ))
circuit.inst(Gates.RXGate(3.1801000664195067, 1 ))
circuit.inst(Gates.RYYGate(2.60217238429383)( 1, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CYGate( 0, 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.CHGate( 0, 1 ))

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

