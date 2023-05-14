
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 9)

p_9ec04a = circuit.declare('p_9ec04a', 'REAL')
p_7ba6a3 = circuit.declare('p_7ba6a3', 'REAL')
p_2edc5d = circuit.declare('p_2edc5d', 'REAL')
p_305641 = circuit.declare('p_305641', 'REAL')

defns = get_custom_get_definitions("CSXGate", "CHGate", "SXGate", "RCCXGate", "SGate", "CRXGate", "C3SXGate", "ZGate", "XGate", "U2Gate", "TGate", "CUGate", "iSwapGate", "SdgGate", "RZGate", "CRZGate", "CCXGate", "CU1Gate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(p_305641, 8, 3 ))
circuit.inst(Gates.CRZGate(p_2edc5d, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(p_7ba6a3, 1, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.CCXGate( 0, 6, 1 ))
circuit.inst(Gates.RCCXGate( 4, 0, 1 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.RZGate(5.014941143947427, 1 ))
circuit.inst(Gates.CRXGate(5.970852306777193, 1, 8 ))
circuit.inst(Gates.iSwapGate( 2, 6 ))
circuit.inst(Gates.CU1Gate(1.2497571638956968, 2, 5 ))
circuit.inst(Gates.RZGate(2.862865991712737, 5 ))
circuit.inst(Gates.CU1Gate(p_9ec04a, 2, 5 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_9ec04a": 2.5476776328466872,
    "p_7ba6a3": 2.586208953975239,
    "p_2edc5d": 1.4112277317699358,
    "p_305641": 3.2142159669963557
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

