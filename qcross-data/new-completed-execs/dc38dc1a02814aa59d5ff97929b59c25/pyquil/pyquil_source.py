
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("SXdgGate", "CSGate", "RXGate", "RYGate", "SdgGate", "HGate", "RZGate", "CPhaseGate", "RYYGate", "UGate", "SwapGate", "RCCXGate", "CSXGate", "U3Gate", "U1Gate", "TGate")

circuit += defns

circuit.inst(Gates.SdgGate( 9 ))
circuit.inst(Gates.HGate( 6 ))
circuit.inst(Gates.U3Gate(6.248539137506652, 3.0437559890158274, 3.877040016955039)( 3 ))
circuit.inst(Gates.TGate( 8 ))
circuit.inst(Gates.RYGate(2.4289944643648695, 2 ))
circuit.inst(Gates.SwapGate( 9, 1 ))
circuit.inst(Gates.RYYGate(2.092741391579245)( 6, 3 ))
circuit.inst(Gates.RZGate(2.184568031539945, 9 ))
circuit.inst(Gates.RZGate(0.6748073587752819, 4 ))
circuit.inst(Gates.U1Gate(1.4687935154189555, 9 ))
circuit.inst(Gates.UGate(2.4455568111156785, 3.2132129187211773, 5.7839656565594115)( 3 ))
circuit.inst(Gates.U1Gate(2.6497338339327143, 9 ))
circuit.inst(Gates.SXdgGate( 9 ))
circuit.inst(Gates.RXGate(0.6137530841617304, 0 ))
circuit.inst(Gates.CSGate( 9, 4 ))
circuit.inst(Gates.HGate( 4 ))
circuit.inst(Gates.RCCXGate( 8, 2, 3 ))
circuit.inst(Gates.CSXGate( 9, 7 ))
circuit.inst(Gates.CPhaseGate(4.048113620213937, 5, 9 ))
circuit.inst(Gates.HGate( 3 ))
circuit.inst(Gates.HGate( 0 ))
circuit.inst(Gates.CSXGate( 7, 2 ))

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




circuit.wrap_in_numshots_loop(5542)

qc = get_qc("10q-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

