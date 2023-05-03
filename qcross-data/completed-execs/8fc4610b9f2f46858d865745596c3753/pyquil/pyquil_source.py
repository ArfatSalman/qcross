
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("SGate", "CRYGate", "SXdgGate", "CRZGate", "U2Gate", "DCXGate", "TGate", "CU3Gate", "TdgGate", "UGate", "RZGate", "RYGate", "XGate")

circuit += defns

circuit.inst(Gates.CRYGate(5.084522291571211, 1, 0 ))
circuit.inst(Gates.CRYGate(0.5214443205823275, 0, 1 ))
circuit.inst(Gates.UGate(5.249389156861369, 5.506136172902856, 5.236656888622806)( 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.CU3Gate(1.3702172143092286, 1.9059592606091926, 5.782626030792982, 1, 0 ))
circuit.inst(Gates.CU3Gate(3.371102520538735, 2.998573490180536, 1.776109337694477, 1, 0 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.UGate(4.284938125077518, 1.0148536455132817, 2.487168338274746)( 0 ))
circuit.inst(Gates.RYGate(3.900848522710214, 0 ))
circuit.inst(Gates.RZGate(2.334985126003777, 1 ))
circuit.inst(Gates.RYGate(1.7484204274088997, 0 ))
circuit.inst(Gates.TdgGate( 0 ))
circuit.inst(Gates.CU3Gate(4.742430815090222, 1.8154225091000729, 3.693501832396555, 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SGate( 1 ))
circuit.inst(Gates.RZGate(5.556271444847221, 1 ))
circuit.inst(Gates.CRZGate(1.6719873041871378, 1, 0 ))
circuit.inst(Gates.DCXGate( 0, 1 ))
circuit.inst(Gates.U2Gate(3.6951879813098216, 4.977624965840704)( 1 ))
circuit.inst(Gates.CU3Gate(5.4144948963161035, 6.127785368788657, 2.137798063823039, 1, 0 ))
circuit.inst(Gates.U2Gate(4.611032125076666, 2.7074003913270643)( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.U2Gate(6.108789748804481, 2.1969367629951018)( 0 ))
circuit.inst(Gates.RYGate(2.811127302481191, 0 ))
circuit.inst(Gates.TGate( 0 ))
circuit.inst(Gates.SGate( 0 ))

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

