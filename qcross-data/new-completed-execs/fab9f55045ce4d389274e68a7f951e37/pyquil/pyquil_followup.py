
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 7)

p_57577b = circuit.declare('p_57577b', 'REAL')
p_68346f = circuit.declare('p_68346f', 'REAL')
p_92d853 = circuit.declare('p_92d853', 'REAL')
p_8852a5 = circuit.declare('p_8852a5', 'REAL')
p_86d3c5 = circuit.declare('p_86d3c5', 'REAL')
p_877ff6 = circuit.declare('p_877ff6', 'REAL')
p_a29d5d = circuit.declare('p_a29d5d', 'REAL')
p_03605d = circuit.declare('p_03605d', 'REAL')
p_f61ac5 = circuit.declare('p_f61ac5', 'REAL')
p_9d2b67 = circuit.declare('p_9d2b67', 'REAL')
p_a10a46 = circuit.declare('p_a10a46', 'REAL')
p_aa393d = circuit.declare('p_aa393d', 'REAL')
p_17cd9d = circuit.declare('p_17cd9d', 'REAL')
p_8a5847 = circuit.declare('p_8a5847', 'REAL')
p_ec60d4 = circuit.declare('p_ec60d4', 'REAL')
p_4c3455 = circuit.declare('p_4c3455', 'REAL')
p_0783a3 = circuit.declare('p_0783a3', 'REAL')
p_655fcc = circuit.declare('p_655fcc', 'REAL')
p_169d88 = circuit.declare('p_169d88', 'REAL')
p_6773c4 = circuit.declare('p_6773c4', 'REAL')
p_b5202c = circuit.declare('p_b5202c', 'REAL')
p_fa03ad = circuit.declare('p_fa03ad', 'REAL')
p_823d76 = circuit.declare('p_823d76', 'REAL')

defns = get_custom_get_definitions("CSwapGate", "RC3XGate", "CSGate", "CU1Gate", "ECRGate", "RXGate", "HGate", "SwapGate", "CCXGate", "UGate", "U2Gate", "CRYGate", "RYGate", "PhaseGate", "RYYGate", "CUGate")

circuit += defns

circuit.inst(Gates.RYYGate(p_86d3c5)( 0, 5 ))
circuit.inst(Gates.PhaseGate(p_03605d, 6 ))
circuit.inst(Gates.RYGate(p_a29d5d, 2 ))
circuit.inst(Gates.CU1Gate(p_823d76, 4, 1 ))
circuit.inst(Gates.CCXGate( 4, 3, 2 ))
circuit.inst(Gates.ECRGate( 0, 6 ))
circuit.inst(Gates.CSwapGate( 0, 6, 4 ))
circuit.inst(Gates.ECRGate( 2, 0 ))
circuit.inst(Gates.SwapGate( 3, 5 ))
circuit.inst(Gates.CSwapGate( 3, 6, 1 ))
circuit.inst(Gates.RC3XGate( 6, 1, 4, 0 ))
circuit.inst(Gates.HGate( 2 ))
circuit.inst(Gates.UGate(p_68346f, p_fa03ad, p_92d853)( 2 ))
circuit.inst(Gates.U2Gate(p_8852a5, p_4c3455)( 4 ))
circuit.inst(Gates.CSGate( 2, 5 ))
circuit.inst(Gates.U2Gate(p_0783a3, p_169d88)( 6 ))
circuit.inst(Gates.RYYGate(p_6773c4)( 1, 5 ))
circuit.inst(Gates.RC3XGate( 3, 1, 4, 5 ))
circuit.inst(Gates.UGate(p_aa393d, p_8a5847, p_655fcc)( 3 ))
circuit.inst(Gates.CUGate(p_877ff6, p_ec60d4, p_f61ac5, p_b5202c, 3, 5 ))
circuit.inst(Gates.U2Gate(p_17cd9d, p_a10a46)( 6 ))
circuit.inst(Gates.RC3XGate( 1, 3, 2, 0 ))
circuit.inst(Gates.RXGate(p_57577b, 0 ))
circuit.inst(Gates.CRYGate(p_9d2b67, 6, 1 ))

qr_9287f2 = circuit.declare("qr_9287f2", "BIT", 4)

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



params = {
    "p_57577b": 5.129266867572668,
    "p_68346f": 5.066050249739578,
    "p_92d853": 2.5510590709018732,
    "p_8852a5": 4.9702527118009066,
    "p_86d3c5": 1.7892872835005398,
    "p_877ff6": 5.814210499839879,
    "p_a29d5d": 3.6138974545836176,
    "p_03605d": 3.7964394792576885,
    "p_f61ac5": 5.986977817617511,
    "p_9d2b67": 2.998268232293747,
    "p_a10a46": 2.4524844691285543,
    "p_aa393d": 0.8822742453157227,
    "p_17cd9d": 4.95448520957096,
    "p_8a5847": 3.4849606070943584,
    "p_ec60d4": 2.2396990253899713,
    "p_4c3455": 3.5114983819004046,
    "p_0783a3": 1.6924855892819173,
    "p_655fcc": 4.713462039096519,
    "p_169d88": 6.035455549292343,
    "p_6773c4": 3.0928548495797905,
    "p_b5202c": 6.091448724065051,
    "p_fa03ad": 3.676251393433825,
    "p_823d76": 4.877167017151953
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

