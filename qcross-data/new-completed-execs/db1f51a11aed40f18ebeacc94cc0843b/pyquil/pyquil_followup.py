
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("CU1Gate", "RYGate", "CPhaseGate", "YGate", "CRXGate", "CRYGate", "CUGate", "CSXGate", "U1Gate", "RGate", "CSGate", "CXGate", "SdgGate", "U3Gate", "CCXGate", "RXXGate", "iSwapGate", "XGate", "TdgGate", "CYGate", "ECRGate")

circuit += defns

circuit.inst(Gates.CSGate( 1, 3 ))
circuit.inst(Gates.CU1Gate(2.7516388630934165, 2, 0 ))
circuit.inst(Gates.CPhaseGate(4.526280604536298, 0, 1 ))
circuit.inst(Gates.CRYGate(2.8957147333760322, 4, 2 ))
circuit.inst(Gates.ECRGate( 1, 3 ))
circuit.inst(Gates.iSwapGate( 0, 5 ))
circuit.inst(Gates.RYGate(5.218542100413873, 0 ))
circuit.inst(Gates.CYGate( 4, 0 ))
circuit.inst(Gates.CUGate(4.0589886937440705, 5.489841527329702, 5.349444809703235, 0.0076492699425670645, 3, 5 ))
circuit.inst(Gates.CCXGate( 1, 5, 3 ))
circuit.inst(Gates.CCXGate( 1, 4, 0 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.CCXGate( 3, 5, 4 ))
circuit.inst(Gates.CSXGate( 4, 1 ))
circuit.inst(Gates.CRXGate(1.7239239743720898, 2, 0 ))
circuit.inst(Gates.CSGate( 4, 0 ))
circuit.inst(Gates.SdgGate( 0 ))

subcircuit = Program()
subcircuit.inst(Gates.YGate( 0 ))
subcircuit.inst(Gates.RXXGate(5.748731119826895)( 1, 4 ))
subcircuit.inst(Gates.XGate( 3 ))
subcircuit.inst(Gates.TdgGate( 4 ))
subcircuit.inst(Gates.RGate(1.0099433123573884, 3.399529081072497)( 5 ))
subcircuit.inst(Gates.U3Gate(5.953737875506177, 2.168117657673707, 5.952071466550862)( 3 ))
subcircuit.inst(Gates.CU1Gate(4.560443955770688, 3, 1 ))
subcircuit.inst(Gates.CXGate( 0, 5 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.U1Gate(3.6101582139068564, 2 ))

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

