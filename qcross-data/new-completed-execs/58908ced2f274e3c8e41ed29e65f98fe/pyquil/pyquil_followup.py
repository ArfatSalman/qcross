
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("RVGate", "RYGate", "UGate", "DCXGate", "YGate", "ZGate", "CSXGate", "RZXGate", "SXdgGate", "CSGate", "CXGate", "RYYGate", "CCZGate", "CZGate", "SXGate", "CCXGate", "TGate", "RXGate", "RZGate", "XGate", "CYGate", "ECRGate")

circuit += defns

circuit.inst(Gates.CYGate( 4, 0 ))
circuit.inst(Gates.RYGate(5.393489737839679, 0 ))
circuit.inst(Gates.CXGate( 4, 2 ))
circuit.inst(Gates.CYGate( 2, 0 ))
circuit.inst(Gates.RVGate(0.2694018871971584, 3.6610185603230327, 1.6717980794833396)( 0 ))
circuit.inst(Gates.CXGate( 1, 2 ))
circuit.inst(Gates.RYGate(3.6367004709817228, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.RVGate(2.2068682001004865, 0.10969098183159173, 1.8129273219934456)( 3 ))
circuit.inst(Gates.RYGate(2.187038626448052, 4 ))
circuit.inst(Gates.CSGate( 3, 1 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.CZGate( 0, 1 ))
circuit.inst(Gates.CCXGate( 4, 1, 3 ))
circuit.inst(Gates.RZGate(4.342933255918919, 1 ))
circuit.inst(Gates.UGate(5.780988845560674, 1.3228348249163877, 4.617489460561287)( 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.ECRGate( 1, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.CCZGate( 2, 3, 0 ))
subcircuit.inst(Gates.RXGate(1.3936743262403044, 0 ))
subcircuit.inst(Gates.XGate( 3 ))
subcircuit.inst(Gates.RZXGate(5.062431030267896)( 3, 0 ))
subcircuit.inst(Gates.YGate( 4 ))
subcircuit.inst(Gates.CZGate( 4, 2 ))
subcircuit.inst(Gates.CSXGate( 3, 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RYYGate(4.555588798234122)( 1, 2 ))
circuit.inst(Gates.RYYGate(4.914511027415462)( 1, 2 ))
circuit.inst(Gates.CSGate( 4, 0 ))
circuit.inst(Gates.RZGate(3.3907281434225625, 4 ))
circuit.inst(Gates.CSXGate( 1, 4 ))
circuit.inst(Gates.DCXGate( 2, 3 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

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

