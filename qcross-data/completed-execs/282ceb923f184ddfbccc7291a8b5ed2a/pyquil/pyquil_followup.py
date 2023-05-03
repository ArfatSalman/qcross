
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("CHGate", "RZZGate", "iSwapGate", "CU3Gate", "C3SXGate", "SGate", "CU1Gate", "CUGate", "TGate", "SXdgGate", "CXGate", "HGate", "RYYGate", "CSXGate", "U2Gate", "RZGate", "ECRGate", "RCCXGate", "XGate", "RXXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 2 ))
circuit.inst(Gates.CU1Gate(5.154187354656876, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CU3Gate(4.501598818751339, 3.831363380793745, 0.29379897242098046, 0, 2 ))
subcircuit.inst(Gates.HGate( 1 ))
subcircuit.inst(Gates.CU1Gate(4.229610589867865, 1, 3 ))
subcircuit.inst(Gates.ECRGate( 1, 3 ))
subcircuit.inst(Gates.U2Gate(6.171674001528992, 4.948673314014118)( 0 ))
subcircuit.inst(Gates.SGate( 1 ))
subcircuit.inst(Gates.CXGate( 0, 3 ))
subcircuit.inst(Gates.RXXGate(3.855749700561927)( 1, 3 ))
subcircuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.TGate( 2 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.RCCXGate( 1, 0, 3 ))
circuit.inst(Gates.RYYGate(1.740253089260498)( 2, 0 ))

qr_08b1f4 = circuit.declare("qr_08b1f4", "BIT", 3)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

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

