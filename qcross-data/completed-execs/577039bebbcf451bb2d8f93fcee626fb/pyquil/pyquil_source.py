
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("HGate", "CYGate", "CU3Gate", "CU1Gate", "YGate", "CSwapGate", "CSXGate", "SGate", "TdgGate", "U1Gate", "IGate", "U3Gate", "iSwapGate", "CZGate", "CCXGate", "RYYGate", "RYGate", "SdgGate", "RXGate")

circuit += defns

circuit.inst(Gates.CZGate( 1, 2 ))
circuit.inst(Gates.CCXGate( 2, 1, 0 ))
circuit.inst(Gates.CU3Gate(0.02974191542848892, 1.097684714540871, 0.5523925010367368, 1, 0 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.U1Gate(4.64787760789041, 0 ))
circuit.inst(Gates.iSwapGate( 0, 2 ))
circuit.inst(Gates.YGate( 2 ))
circuit.inst(Gates.CZGate( 1, 2 ))
circuit.inst(Gates.iSwapGate( 1, 2 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.RYYGate(2.3941143994200504)( 1, 0 ))
circuit.inst(Gates.TdgGate( 0 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.RXGate(5.932085825305516, 2 ))
circuit.inst(Gates.CSwapGate( 2, 0, 1 ))
circuit.inst(Gates.SdgGate( 2 ))
circuit.inst(Gates.U3Gate(0.20490217819899895, 0.2844754781181525, 4.8984947281198385)( 2 ))
circuit.inst(Gates.CYGate( 1, 2 ))
circuit.inst(Gates.RYGate(4.64391690767843, 1 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.IGate( 0 ))
circuit.inst(Gates.U1Gate(3.4582628336664856, 0 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CU1Gate(3.1245965108163056, 1, 2 ))
circuit.inst(Gates.RXGate(0.16532103311248328, 1 ))
circuit.inst(Gates.TdgGate( 2 ))
circuit.inst(Gates.RYGate(2.5451656062496135, 1 ))

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

