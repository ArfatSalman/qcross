
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("XGate", "RZGate", "CSXGate", "PhaseGate", "CHGate", "RZZGate", "C3SXGate", "CRYGate", "RXGate", "U1Gate", "TdgGate", "TGate", "CU1Gate", "iSwapGate", "CUGate", "CXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.TdgGate( 2 ))
subcircuit.inst(Gates.U1Gate(5.01836135520768, 1 ))
subcircuit.inst(Gates.CRYGate(4.736752714049485, 0, 3 ))
subcircuit.inst(Gates.RXGate(6.1292830756636185, 2 ))
subcircuit.inst(Gates.CHGate( 2, 3 ))
subcircuit.inst(Gates.CXGate( 2, 0 ))
subcircuit.inst(Gates.RZZGate(3.516607467010828)( 3, 1 ))
subcircuit.inst(Gates.PhaseGate(3.2287759437031154, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 2 ))
circuit.inst(Gates.CU1Gate(5.154187354656876, 3, 0 ))
circuit.inst(Gates.CHGate( 3, 2 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 0, 1, 2 ))
circuit.inst(Gates.C3SXGate( 3, 1, 0, 2 ))
circuit.inst(Gates.TGate( 2 ))

qr_d2b925 = circuit.declare("qr_d2b925", "BIT", 8)

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

