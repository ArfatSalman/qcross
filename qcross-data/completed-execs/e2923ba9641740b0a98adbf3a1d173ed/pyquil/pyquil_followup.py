
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("CHGate", "U2Gate", "CRZGate", "CUGate", "SGate", "ZGate", "SwapGate", "RZGate", "C3SXGate", "CSXGate", "XGate", "RCCXGate", "CU1Gate", "RZXGate", "DCXGate", "SXGate", "TGate", "CXGate", "iSwapGate", "SdgGate", "CCXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 6 ))

subcircuit = Program()
subcircuit.inst(Gates.CU1Gate(2.0685963035149753, 5, 0 ))
subcircuit.inst(Gates.RZXGate(1.1412693567569159)( 1, 8 ))
subcircuit.inst(Gates.SwapGate( 1, 6 ))
subcircuit.inst(Gates.iSwapGate( 2, 6 ))
subcircuit.inst(Gates.RCCXGate( 2, 5, 8 ))
subcircuit.inst(Gates.CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004, 3, 1 ))
subcircuit.inst(Gates.CXGate( 3, 8 ))
subcircuit.inst(Gates.CHGate( 1, 4 ))
subcircuit.inst(Gates.DCXGate( 4, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 8, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 1, 2 ))
circuit.inst(Gates.U2Gate(2.5163050709890156, 2.1276323672732023)( 2 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.CCXGate( 0, 6, 1 ))

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





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

