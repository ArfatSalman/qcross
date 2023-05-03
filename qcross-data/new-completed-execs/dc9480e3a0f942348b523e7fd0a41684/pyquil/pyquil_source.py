
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 11)



defns = get_custom_get_definitions("CRYGate", "SGate", "RXGate", "RC3XGate", "HGate", "TGate", "RZXGate", "XGate", "RXXGate", "C3SXGate", "RCCXGate", "RYYGate", "CUGate", "U1Gate", "CYGate", "RVGate", "UGate")

circuit += defns

circuit.inst(Gates.TGate( 9 ))
circuit.inst(Gates.CRYGate(1.852579362704606, 4, 7 ))
circuit.inst(Gates.CYGate( 9, 0 ))
circuit.inst(Gates.RXGate(5.276411432143827, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.U1Gate(2.825051590836995, 1 ))
circuit.inst(Gates.RC3XGate( 8, 9, 1, 5 ))
circuit.inst(Gates.RYYGate(0.7867209387701732)( 7, 9 ))
circuit.inst(Gates.UGate(4.576754367736335, 5.4109147050480955, 1.7256413064705036)( 7 ))
circuit.inst(Gates.RC3XGate( 3, 5, 1, 4 ))
circuit.inst(Gates.RVGate(5.6896213477612445, 6.047339853997451, 5.623943529608011)( 7 ))
circuit.inst(Gates.UGate(3.0132549867885063, 6.182661801638049, 5.885160602032744)( 7 ))
circuit.inst(Gates.HGate( 4 ))
circuit.inst(Gates.RVGate(4.1249177878170915, 6.0745761147209345, 2.4099754200724317)( 0 ))
circuit.inst(Gates.CYGate( 10, 2 ))
circuit.inst(Gates.HGate( 8 ))
circuit.inst(Gates.UGate(2.169150328031207, 1.7114617170345237, 2.307521863987498)( 2 ))
circuit.inst(Gates.UGate(5.430643357287303, 0.6530454683497888, 3.836596788250059)( 10 ))
circuit.inst(Gates.RZXGate(5.431264813579931)( 1, 3 ))
circuit.inst(Gates.CUGate(2.9821700362780588, 1.3852421816440175, 4.785976176026314, 1.3657070275541772, 4, 2 ))
circuit.inst(Gates.SGate( 5 ))
circuit.inst(Gates.RCCXGate( 9, 3, 6 ))
circuit.inst(Gates.RC3XGate( 10, 8, 9, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RVGate(5.050073208732572, 2.867190134610833, 1.0118283033144115)( 2 ))
circuit.inst(Gates.RXXGate(1.2634039528117698)( 1, 6 ))
circuit.inst(Gates.RVGate(0.5734726823505982, 3.854641723491838, 1.0422555828622841)( 7 ))
circuit.inst(Gates.C3SXGate( 9, 10, 2, 8 ))

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





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

