
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)



defns = get_custom_get_definitions("CRYGate", "ECRGate", "RZXGate", "U2Gate", "DCXGate", "TGate", "CZGate", "CU3Gate", "SdgGate", "RXGate", "SwapGate", "CU1Gate", "YGate", "UGate", "CPhaseGate", "RYYGate", "IGate", "U3Gate")

circuit += defns

circuit.inst(Gates.RZXGate(5.294170317838349)( 2, 4 ))
circuit.inst(Gates.SwapGate( 1, 5 ))
circuit.inst(Gates.U3Gate(5.951221312078038, 5.377869177229497, 4.13307667574035)( 2 ))
circuit.inst(Gates.ECRGate( 4, 1 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.YGate( 4 ))
circuit.inst(Gates.U3Gate(3.127390581057496, 0.8951620930728853, 2.9211253533322705)( 4 ))
circuit.inst(Gates.CPhaseGate(3.2345621726383063, 3, 0 ))
circuit.inst(Gates.CRYGate(1.5739612232900921, 4, 0 ))
circuit.inst(Gates.ECRGate( 1, 2 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.RXGate(2.1921350525840335, 1 ))
circuit.inst(Gates.CRYGate(4.81139250369156, 0, 3 ))
circuit.inst(Gates.CU3Gate(0.5792738051909873, 5.615330906310357, 2.660875175684596, 5, 0 ))
circuit.inst(Gates.IGate( 0 ))
circuit.inst(Gates.U2Gate(4.245494087381378, 0.35899282563221724)( 0 ))
circuit.inst(Gates.UGate(1.0608924835540103, 2.415674942808992, 0.8187346879786549)( 3 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.RXGate(5.956960136241147, 3 ))
circuit.inst(Gates.DCXGate( 4, 5 ))
circuit.inst(Gates.U3Gate(1.5683345978951369, 1.4287408195765756, 2.3460687004856973)( 1 ))
circuit.inst(Gates.CU1Gate(1.9757038692524151, 3, 1 ))
circuit.inst(Gates.U3Gate(0.4602821600746163, 5.414451003251248, 4.293440251468374)( 4 ))
circuit.inst(Gates.CZGate( 4, 3 ))
circuit.inst(Gates.TGate( 3 ))
circuit.inst(Gates.RYYGate(4.463598643942479)( 1, 5 ))
circuit.inst(Gates.CU3Gate(3.8745722202781416, 3.2737382848299332, 3.2686683844993465, 5, 0 ))
circuit.inst(Gates.SdgGate( 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(2, qr[1])
circuit += MEASURE(4, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(5, qr[4])
circuit += MEASURE(1, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

