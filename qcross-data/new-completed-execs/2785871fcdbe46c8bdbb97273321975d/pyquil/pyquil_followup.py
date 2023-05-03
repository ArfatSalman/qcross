
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 5)



defns = get_custom_get_definitions("SXdgGate", "CHGate", "RXGate", "CXGate", "CSdgGate", "ZGate", "CRXGate", "CPhaseGate", "PhaseGate", "RC3XGate", "CCZGate", "TdgGate", "CSXGate", "DCXGate", "RGate", "RZZGate", "SGate", "SwapGate")

circuit += defns

circuit.inst(Gates.SGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.CCZGate( 4, 1, 0 ))
subcircuit.inst(Gates.RZZGate(1.494768934171475)( 3, 0 ))
subcircuit.inst(Gates.RGate(0.2569619900931398, 2.6199756460968913)( 4 ))
subcircuit.inst(Gates.TdgGate( 3 ))
subcircuit.inst(Gates.SXdgGate( 1 ))
subcircuit.inst(Gates.PhaseGate(4.75198563922302, 0 ))
subcircuit.inst(Gates.RC3XGate( 1, 3, 4, 2 ))
subcircuit.inst(Gates.SGate( 3 ))
subcircuit.inst(Gates.CHGate( 1, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSdgGate( 0, 2 ))
circuit.inst(Gates.RXGate(5.16336000498251, 2 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CRXGate(3.8747797547682863, 0, 1 ))
circuit.inst(Gates.CXGate( 1, 0 ))
circuit.inst(Gates.SwapGate( 3, 1 ))
circuit.inst(Gates.CSXGate( 2, 3 ))
circuit.inst(Gates.CSdgGate( 3, 2 ))
circuit.inst(Gates.DCXGate( 2, 3 ))
circuit.inst(Gates.CPhaseGate(1.6310047821220433, 3, 2 ))
circuit.inst(Gates.ZGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])




circuit.wrap_in_numshots_loop(979)

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

