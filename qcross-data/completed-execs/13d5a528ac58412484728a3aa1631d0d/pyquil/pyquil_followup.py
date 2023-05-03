
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("TGate", "HGate", "UGate", "U3Gate", "SGate", "CPhaseGate", "CHGate", "CSXGate", "U2Gate", "RXGate", "SwapGate", "SXdgGate", "RZXGate", "CRXGate")

circuit += defns

circuit.inst(Gates.SwapGate( 0, 1 ))
circuit.inst(Gates.RZXGate(3.8834807859507263)( 1, 0 ))
circuit.inst(Gates.SwapGate( 1, 0 ))
circuit.inst(Gates.UGate(4.973624404177978, 1.450846828228022, 5.424728583609293)( 0 ))
circuit.inst(Gates.CRXGate(3.510034154259637, 1, 0 ))
circuit.inst(Gates.RZXGate(1.9764943500940788)( 1, 0 ))
circuit.inst(Gates.RXGate(1.444335936996841, 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.UGate(0.7650180880812659, 1.1640465366080328, 3.351987550000961)( 1 ))
circuit.inst(Gates.U2Gate(2.138082427163418, 5.230899032902529)( 1 ))
circuit.inst(Gates.CPhaseGate(0.554577471370062, 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.CHGate( 1, 0 ))
circuit.inst(Gates.U3Gate(0.9335631365840328, 4.520121169686029, 5.198491695816633)( 0 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.HGate( 1 ))
circuit.inst(Gates.CRXGate(3.4913681561376415, 0, 1 ))
circuit.inst(Gates.SXdgGate( 1 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 1, 0 ))

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

