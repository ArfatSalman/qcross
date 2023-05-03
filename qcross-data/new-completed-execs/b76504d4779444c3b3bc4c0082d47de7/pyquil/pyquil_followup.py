
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("RVGate", "CPhaseGate", "IGate", "U2Gate", "DCXGate", "ZGate", "HGate", "SwapGate", "SXdgGate", "CXGate", "SdgGate", "CCZGate", "U3Gate", "RXGate", "RXXGate", "RC3XGate", "CU3Gate", "iSwapGate", "TdgGate", "CYGate", "ECRGate")

circuit += defns

circuit.inst(Gates.RXGate(0.6650027350645848, 5 ))
circuit.inst(Gates.SdgGate( 0 ))
circuit.inst(Gates.CYGate( 0, 4 ))
circuit.inst(Gates.RVGate(4.207878413680952, 0.3009231473653096, 1.580343691421699)( 4 ))
circuit.inst(Gates.CPhaseGate(3.9206722628490542, 5, 2 ))
circuit.inst(Gates.CPhaseGate(3.397598873029434, 2, 3 ))
circuit.inst(Gates.IGate( 4 ))
circuit.inst(Gates.U2Gate(4.855299131904333, 3.1272609413923482)( 3 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.RXXGate(0.7249247820191558)( 3, 4 ))
circuit.inst(Gates.TdgGate( 5 ))
circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.CXGate( 4, 1 ))
circuit.inst(Gates.IGate( 5 ))
circuit.inst(Gates.RC3XGate( 5, 2, 4, 3 ))
circuit.inst(Gates.RC3XGate( 5, 2, 4, 0 ))
circuit.inst(Gates.RXXGate(2.6498953828086473)( 2, 4 ))
circuit.inst(Gates.CYGate( 5, 2 ))
circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 0, 2 ))
circuit.inst(Gates.HGate( 4 ))

subcircuit = Program()
subcircuit.inst(Gates.SwapGate( 1, 0 ))
subcircuit.inst(Gates.CYGate( 0, 5 ))
subcircuit.inst(Gates.CCZGate( 4, 3, 5 ))
subcircuit.inst(Gates.DCXGate( 0, 2 ))
subcircuit.inst(Gates.RXGate(5.981830878165426, 2 ))
subcircuit.inst(Gates.U3Gate(2.693422775984842, 0.5067499290735414, 2.096989391777038)( 5 ))
subcircuit.inst(Gates.SwapGate( 0, 3 ))
subcircuit.inst(Gates.CU3Gate(2.0053149876729552, 5.072178584377088, 2.2962625668816754, 1, 3 ))
subcircuit.inst(Gates.RXXGate(4.1874527696058825)( 0, 4 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.ECRGate( 0, 5 ))
circuit.inst(Gates.ZGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

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

