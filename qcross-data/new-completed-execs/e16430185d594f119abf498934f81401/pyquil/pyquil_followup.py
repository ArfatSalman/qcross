
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 8)



defns = get_custom_get_definitions("CU1Gate", "RYGate", "CPhaseGate", "IGate", "DCXGate", "RCCXGate", "CUGate", "RZXGate", "RGate", "SwapGate", "SdgGate", "CCXGate", "TGate", "CSwapGate", "RXGate", "RXXGate", "RC3XGate", "CSdgGate", "iSwapGate", "XGate", "YGate", "ECRGate")

circuit += defns

circuit.inst(Gates.ECRGate( 1, 7 ))
circuit.inst(Gates.RC3XGate( 1, 0, 5, 6 ))
circuit.inst(Gates.CPhaseGate(0.7207706407070019, 4, 3 ))
circuit.inst(Gates.DCXGate( 3, 4 ))
circuit.inst(Gates.RCCXGate( 2, 1, 4 ))
circuit.inst(Gates.SwapGate( 6, 5 ))

subcircuit = Program()
subcircuit.inst(Gates.CCXGate( 2, 5, 3 ))
subcircuit.inst(Gates.RCCXGate( 5, 0, 1 ))
subcircuit.inst(Gates.CSdgGate( 2, 5 ))
subcircuit.inst(Gates.CPhaseGate(0.37327159055448994, 2, 3 ))
subcircuit.inst(Gates.CUGate(5.603364910525811, 0.5779107198193537, 1.1120816789855388, 4.149916491769281, 3, 2 ))
subcircuit.inst(Gates.RZXGate(1.264637581124353)( 7, 1 ))
subcircuit.inst(Gates.SdgGate( 2 ))
subcircuit.inst(Gates.YGate( 3 ))
subcircuit.inst(Gates.RGate(3.026082456028544, 4.216289330198313)( 6 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.iSwapGate( 4, 7 ))
circuit.inst(Gates.RXGate(4.802467793465571, 0 ))
circuit.inst(Gates.iSwapGate( 0, 5 ))
circuit.inst(Gates.CU1Gate(3.4625444838065618, 0, 6 ))
circuit.inst(Gates.CSwapGate( 0, 3, 6 ))
circuit.inst(Gates.RGate(5.104156300804455, 6.227137798959555)( 0 ))
circuit.inst(Gates.TGate( 5 ))
circuit.inst(Gates.RXXGate(6.256338963756067)( 1, 5 ))
circuit.inst(Gates.DCXGate( 7, 6 ))
circuit.inst(Gates.RYGate(2.803631472128793, 3 ))
circuit.inst(Gates.RC3XGate( 4, 3, 1, 2 ))
circuit.inst(Gates.CU1Gate(1.5456697172063534, 7, 6 ))
circuit.inst(Gates.RYGate(4.278284783932528, 7 ))
circuit.inst(Gates.RCCXGate( 7, 2, 0 ))
circuit.inst(Gates.RGate(0.2852105385229711, 5.142516617776941)( 2 ))
circuit.inst(Gates.RXXGate(2.2028067729502347)( 1, 6 ))
circuit.inst(Gates.RXGate(1.732522506962926, 7 ))
circuit.inst(Gates.CCXGate( 5, 1, 6 ))
circuit.inst(Gates.XGate( 3 ))
circuit.inst(Gates.IGate( 3 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])




circuit.wrap_in_numshots_loop(2771)

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

