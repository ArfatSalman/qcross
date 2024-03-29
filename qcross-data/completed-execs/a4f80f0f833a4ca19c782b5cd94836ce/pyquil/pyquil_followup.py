
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"GREEDY"']) )

qr = circuit.declare("ro", "BIT", 3)



defns = get_custom_get_definitions("CCXGate", "XGate", "RZGate", "SdgGate", "CRXGate", "RYYGate", "SXdgGate", "CHGate", "CSXGate", "SGate", "ZGate", "U1Gate", "iSwapGate", "U3Gate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.ZGate( 1 ))
subcircuit.inst(Gates.U1Gate(4.654977034583802, 2 ))
subcircuit.inst(Gates.U3Gate(5.01836135520768, 5.190931186022931, 1.2128092629174942)( 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.CCXGate( 1, 0, 2 ))
circuit.inst(Gates.CHGate( 2, 0 ))
circuit.inst(Gates.CHGate( 1, 2 ))
circuit.inst(Gates.RYYGate(1.6723037552953224)( 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

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

