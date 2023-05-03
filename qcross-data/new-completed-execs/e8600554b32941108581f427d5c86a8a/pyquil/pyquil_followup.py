
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"PARTIAL"']) )

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("IGate", "CPhaseGate", "iSwapGate", "SXGate", "RZZGate", "UGate", "SwapGate", "CSXGate", "TdgGate", "RYGate", "CRXGate", "PhaseGate", "DCXGate", "RYYGate")

circuit += defns

circuit.inst(Gates.IGate( 1 ))
circuit.inst(Gates.SwapGate( 0, 1 ))
circuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(Gates.RYGate(1.1002993512000188, 1 ))
circuit.inst(Gates.CPhaseGate(1.9632220362422863, 1, 0 ))
circuit.inst(Gates.RYYGate(1.9181567063153306)( 1, 0 ))
circuit.inst(Gates.CRXGate(2.4590168324579773, 0, 1 ))
circuit.inst(Gates.PhaseGate(0.7665475532378738, 0 ))
circuit.inst(Gates.RYYGate(1.153606269131821)( 1, 0 ))
circuit.inst(Gates.CPhaseGate(1.1100132636552245, 1, 0 ))
circuit.inst(Gates.iSwapGate( 0, 1 ))
circuit.inst(Gates.UGate(3.8572757475580413, 1.8831270698344038, 5.011779985191158)( 1 ))
circuit.inst(Gates.CRXGate(2.1827683748032527, 0, 1 ))
circuit.inst(Gates.IGate( 0 ))
circuit.inst(Gates.RYGate(0.5934420994921776, 0 ))
circuit.inst(Gates.RYGate(0.5479105491667954, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.UGate(6.2496149710424405, 5.8205761472087545, 5.829068520224341)( 1 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.RZZGate(4.338194291975017)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CPhaseGate(1.7974397830964004, 1, 0 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.IGate( 0 ))
circuit.inst(Gates.CRXGate(4.404558705198131, 0, 1 ))
circuit.inst(Gates.TdgGate( 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

