
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("RYGate", "CPhaseGate", "IGate", "U2Gate", "CHGate", "CRXGate", "CRYGate", "RCCXGate", "RZXGate", "U1Gate", "RGate", "CSGate", "CCZGate", "U3Gate", "CZGate", "RXXGate", "CU3Gate", "RC3XGate", "RZGate", "iSwapGate", "CYGate", "SGate")

circuit += defns

circuit.inst(Gates.CRXGate(4.905634676582973, 4, 1 ))
circuit.inst(Gates.RGate(4.591350839465064, 1.2679876620814976)( 5 ))
circuit.inst(Gates.CZGate( 4, 10 ))

subcircuit = Program()
subcircuit.inst(Gates.SGate( 6 ))
subcircuit.inst(Gates.CPhaseGate(0.8912299955175988, 10, 9 ))
subcircuit.inst(Gates.RXXGate(6.202385428323795)( 9, 2 ))
subcircuit.inst(Gates.CU3Gate(0.17275929115190944, 3.979025542935018, 1.5894459673585912, 2, 8 ))
subcircuit.inst(Gates.RZGate(5.22819431699873, 3 ))
subcircuit.inst(Gates.IGate( 4 ))
subcircuit.inst(Gates.RYGate(5.90619537594574, 6 ))
subcircuit.inst(Gates.CU3Gate(3.688151163878286, 4.727514924286728, 4.075756946750543, 7, 6 ))
subcircuit.inst(Gates.U1Gate(5.472976168291315, 3 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.U3Gate(4.438175883374682, 5.014778227242978, 0.395105964485411)( 9 ))
circuit.inst(Gates.IGate( 10 ))
circuit.inst(Gates.CRXGate(2.8176864996575204, 3, 4 ))
circuit.inst(Gates.CHGate( 0, 2 ))
circuit.inst(Gates.IGate( 4 ))
circuit.inst(Gates.SGate( 9 ))
circuit.inst(Gates.CRXGate(6.06720431582227, 0, 8 ))
circuit.inst(Gates.U2Gate(3.8396484521920486, 5.389605086705323)( 0 ))
circuit.inst(Gates.CYGate( 0, 9 ))
circuit.inst(Gates.CRXGate(0.6410834959357722, 1, 2 ))
circuit.inst(Gates.CRXGate(3.152773209785367, 5, 2 ))
circuit.inst(Gates.CSGate( 2, 3 ))
circuit.inst(Gates.RC3XGate( 0, 8, 6, 4 ))
circuit.inst(Gates.iSwapGate( 3, 6 ))
circuit.inst(Gates.CRYGate(3.8184925395522673, 7, 1 ))
circuit.inst(Gates.RZXGate(5.0844543693921445)( 9, 0 ))
circuit.inst(Gates.RCCXGate( 4, 3, 2 ))
circuit.inst(Gates.U2Gate(0.5232088988285076, 1.5882644602699434)( 7 ))
circuit.inst(Gates.CCZGate( 5, 2, 6 ))
circuit.inst(Gates.IGate( 10 ))
circuit.inst(Gates.iSwapGate( 6, 10 ))

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
circuit += MEASURE(10, qr[10])




circuit.wrap_in_numshots_loop(7838)

qc = get_qc("11q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)




quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

