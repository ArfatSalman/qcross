
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 10)



defns = get_custom_get_definitions("ECRGate", "C4XGate", "CSXGate", "RZGate", "CYGate", "CSwapGate", "YGate", "RCCXGate", "PhaseGate", "UGate", "C3XGate", "RZZGate", "U1Gate", "SdgGate", "iSwapGate")

circuit += defns

circuit.inst(Gates.CYGate( 0, 6 ))
circuit.inst(Gates.U1Gate(3.321288277959951, 2 ))
circuit.inst(Gates.YGate( 3 ))
circuit.inst(Gates.ECRGate( 5, 1 ))
circuit.inst(Gates.RZGate(3.0238378046938514, 6 ))
circuit.inst(Gates.iSwapGate( 3, 6 ))
circuit.inst(Gates.ECRGate( 4, 3 ))
circuit.inst(Gates.RCCXGate( 2, 5, 3 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.PhaseGate(0.2289483555541983, 3 ))
circuit.inst(Gates.CYGate( 5, 7 ))
circuit.inst(Gates.PhaseGate(4.268329737032283, 4 ))
circuit.inst(Gates.CSwapGate( 2, 3, 7 ))
circuit.inst(Gates.UGate(0.7278978053151748, 5.145064315568138, 1.7503156588884659)( 2 ))
circuit.inst(Gates.C4XGate( 4, 1, 2, 6, 8 ))
circuit.inst(Gates.RZZGate(6.262915463363716)( 9, 7 ))
circuit.inst(Gates.SdgGate( 3 ))
circuit.inst(Gates.ECRGate( 2, 7 ))
circuit.inst(Gates.RZZGate(2.0261195842682675)( 7, 5 ))
circuit.inst(Gates.U1Gate(0.5870983336064636, 0 ))
circuit.inst(Gates.RZZGate(4.586260430147017)( 7, 9 ))
circuit.inst(Gates.YGate( 1 ))
circuit.inst(Gates.C3XGate( 6, 3, 8, 4 ))
circuit.inst(Gates.C4XGate( 0, 7, 5, 6, 4 ))
circuit.inst(Gates.CSXGate( 9, 4 ))
circuit.inst(Gates.C4XGate( 0, 8, 9, 5, 2 ))

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

