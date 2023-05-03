
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)



defns = get_custom_get_definitions("CSwapGate", "RC3XGate", "CSGate", "CU1Gate", "ECRGate", "RXGate", "HGate", "SwapGate", "CCXGate", "UGate", "U2Gate", "CRYGate", "RYGate", "PhaseGate", "RYYGate", "CUGate")

circuit += defns

circuit.inst(Gates.RYYGate(1.7892872835005398)( 0, 5 ))
circuit.inst(Gates.PhaseGate(3.7964394792576885, 6 ))
circuit.inst(Gates.RYGate(3.6138974545836176, 2 ))
circuit.inst(Gates.CU1Gate(4.877167017151953, 4, 1 ))
circuit.inst(Gates.CCXGate( 4, 3, 2 ))
circuit.inst(Gates.ECRGate( 0, 6 ))
circuit.inst(Gates.CSwapGate( 0, 6, 4 ))
circuit.inst(Gates.ECRGate( 2, 0 ))
circuit.inst(Gates.SwapGate( 3, 5 ))
circuit.inst(Gates.CSwapGate( 3, 6, 1 ))
circuit.inst(Gates.RC3XGate( 6, 1, 4, 0 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.UGate(5.066050249739578, 3.676251393433825, 2.5510590709018732)( 2 ))
circuit.inst(Gates.U2Gate(4.9702527118009066, 3.5114983819004046)( 4 ))
circuit.inst(Gates.CSGate( 2, 5 ))
circuit.inst(Gates.U2Gate(1.6924855892819173, 6.035455549292343)( 6 ))
circuit.inst(Gates.RYYGate(3.0928548495797905)( 1, 5 ))
circuit.inst(Gates.RC3XGate( 3, 1, 4, 5 ))
circuit.inst(Gates.UGate(0.8822742453157227, 3.4849606070943584, 4.713462039096519)( 3 ))
circuit.inst(Gates.CUGate(5.814210499839879, 2.2396990253899713, 5.986977817617511, 6.091448724065051, 3, 5 ))
circuit.inst(Gates.U2Gate(4.95448520957096, 2.4524844691285543)( 6 ))
circuit.inst(Gates.RC3XGate( 1, 3, 2, 0 ))
circuit.inst(Gates.RXGate(5.129266867572668, 0 ))
circuit.inst(Gates.CRYGate(2.998268232293747, 6, 1 ))

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

