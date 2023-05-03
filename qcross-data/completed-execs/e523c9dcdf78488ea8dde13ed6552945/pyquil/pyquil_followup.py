
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("CHGate", "CRZGate", "PhaseGate", "CCXGate", "ZGate", "ECRGate", "UGate", "SwapGate", "CUGate", "RCCXGate", "TGate", "XGate", "CSXGate", "RZGate", "C3SXGate", "SXGate", "CSwapGate", "CRXGate", "iSwapGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 3 ))
circuit.inst(Gates.CRZGate(4.2641612072511235, 6, 3 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 1, 7 ))
circuit.inst(Gates.CCXGate( 5, 9, 7 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.XGate( 8 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 6 ))
circuit.inst(Gates.RZGate(4.229610589867865, 1 ))
circuit.inst(Gates.SXGate( 2 ))
circuit.inst(Gates.CSXGate( 4, 8 ))
circuit.inst(Gates.CCXGate( 4, 9, 5 ))
circuit.inst(Gates.C3SXGate( 2, 4, 0, 9 ))
circuit.inst(Gates.CSXGate( 0, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CSwapGate( 0, 4, 1 ))
subcircuit.inst(Gates.iSwapGate( 6, 5 ))
subcircuit.inst(Gates.UGate(2.438459595578943, 3.326780904591333, 3.4232119351142516)( 3 ))
subcircuit.inst(Gates.PhaseGate(0.4827903095199283, 8 ))
subcircuit.inst(Gates.ECRGate( 1, 8 ))
subcircuit.inst(Gates.SwapGate( 1, 7 ))
subcircuit.inst(Gates.iSwapGate( 2, 7 ))
subcircuit.inst(Gates.RCCXGate( 2, 0, 5 ))
subcircuit.inst(Gates.CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004, 3, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CHGate( 7, 1 ))
circuit.inst(Gates.CSXGate( 2, 0 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 1, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])
circuit += MEASURE(9, qr[9])




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

