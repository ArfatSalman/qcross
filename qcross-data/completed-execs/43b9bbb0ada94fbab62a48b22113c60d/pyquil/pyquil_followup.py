
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("CUGate", "TdgGate", "RZZGate", "RZGate", "iSwapGate", "CU1Gate", "SwapGate", "XGate", "CSXGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.RZZGate(4.066449154047175)( 2, 3 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))

subcircuit = Program()
subcircuit.inst(Gates.CUGate(5.320621737498446, 3.427505621225153, 5.512260524440591, 1.350257477660173, 3, 0 ))
subcircuit.inst(Gates.SwapGate( 1, 0 ))
subcircuit.inst(Gates.CU1Gate(6.086884486572108, 3, 0 ))
subcircuit.inst(Gates.TdgGate( 2 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])




circuit.wrap_in_numshots_loop(692)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

