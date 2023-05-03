
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 4)



defns = get_custom_get_definitions("U2Gate", "IGate", "CRXGate", "CSXGate", "U1Gate", "RZZGate", "CSGate", "CXGate", "RYYGate", "CCZGate", "CCXGate", "TGate", "RXXGate", "RXGate", "RC3XGate", "CSdgGate", "RZGate", "iSwapGate", "XGate", "TdgGate", "CYGate", "SGate")

circuit += defns

circuit.inst(Gates.TdgGate( 3 ))

subcircuit = Program()
subcircuit.inst(Gates.TGate( 0 ))
subcircuit.inst(Gates.XGate( 3 ))
subcircuit.inst(Gates.CSdgGate( 1, 2 ))
subcircuit.inst(Gates.RXGate(3.585933838237832, 3 ))
subcircuit.inst(Gates.RZGate(4.327708900759496, 2 ))
subcircuit.inst(Gates.CSdgGate( 1, 2 ))
subcircuit.inst(Gates.CSdgGate( 2, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RC3XGate( 3, 2, 0, 1 ))
circuit.inst(Gates.CRXGate(3.8220531708356265, 2, 3 ))
circuit.inst(Gates.RYYGate(0.706851892491546)( 0, 3 ))
circuit.inst(Gates.SGate( 3 ))
circuit.inst(Gates.CCXGate( 2, 3, 0 ))
circuit.inst(Gates.U2Gate(4.244731333359949, 5.111240623114551)( 1 ))
circuit.inst(Gates.U1Gate(6.038142598726985, 3 ))
circuit.inst(Gates.RZZGate(4.711366793785529)( 0, 3 ))
circuit.inst(Gates.CCZGate( 1, 2, 3 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.CXGate( 2, 3 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.U1Gate(3.792448958077701, 3 ))
circuit.inst(Gates.RZZGate(0.34163860688651065)( 1, 0 ))
circuit.inst(Gates.iSwapGate( 2, 3 ))
circuit.inst(Gates.RXXGate(0.5068226496124109)( 0, 1 ))
circuit.inst(Gates.RYYGate(2.3758586345554287)( 2, 0 ))
circuit.inst(Gates.RXGate(1.4237342865387943, 0 ))
circuit.inst(Gates.U1Gate(6.094655700711693, 2 ))
circuit.inst(Gates.CSGate( 0, 1 ))
circuit.inst(Gates.CYGate( 0, 2 ))
circuit.inst(Gates.CYGate( 1, 0 ))
circuit.inst(Gates.IGate( 3 ))
circuit.inst(Gates.CSGate( 2, 0 ))
circuit.inst(Gates.U2Gate(4.750593946827152, 1.9165638225080148)( 0 ))
circuit.inst(Gates.RXXGate(2.141645891766187)( 1, 2 ))
circuit.inst(Gates.RXGate(5.97814280452802, 3 ))
circuit.inst(Gates.CSXGate( 3, 1 ))
circuit.inst(Gates.CSGate( 2, 0 ))

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

