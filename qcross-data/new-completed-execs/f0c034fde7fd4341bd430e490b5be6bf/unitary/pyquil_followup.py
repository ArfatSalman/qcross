
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()





defns = get_custom_get_definitions("CZGate", "CU3Gate", "RXGate", "SwapGate", "CCXGate", "DCXGate", "RZXGate", "CRZGate", "YGate", "C3SXGate", "CSwapGate", "RZZGate", "XGate", "SdgGate", "ECRGate", "HGate", "CRYGate", "U3Gate", "SXdgGate")

circuit += defns

circuit.inst(Gates.YGate( 8 ))
circuit.inst(Gates.CU3Gate(1.137265035582176, 1.9191341652886187, 2.035659400824786, 2, 5 ))
circuit.inst(Gates.ECRGate( 4, 1 ))
circuit.inst(Gates.HGate( 8 ))
circuit.inst(Gates.CRZGate(5.5072773697390085, 5, 0 ))
circuit.inst(Gates.RXGate(4.368068524516866, 9 ))
circuit.inst(Gates.CZGate( 6, 1 ))
circuit.inst(Gates.SdgGate( 7 ))
circuit.inst(Gates.CRYGate(4.03209544447551, 1, 4 ))
circuit.inst(Gates.SwapGate( 9, 2 ))
circuit.inst(Gates.YGate( 9 ))
circuit.inst(Gates.SwapGate( 0, 8 ))
circuit.inst(Gates.SXdgGate( 3 ))
circuit.inst(Gates.ECRGate( 3, 7 ))
circuit.inst(Gates.DCXGate( 9, 1 ))
circuit.inst(Gates.CCXGate( 8, 2, 3 ))
circuit.inst(Gates.YGate( 7 ))
circuit.inst(Gates.C3SXGate( 7, 3, 5, 1 ))
circuit.inst(Gates.U3Gate(1.6951114914418934, 5.599301713249363, 3.1864266503972143)( 4 ))
circuit.inst(Gates.RXGate(5.528457770513217, 7 ))
circuit.inst(Gates.C3SXGate( 2, 6, 1, 7 ))
circuit.inst(Gates.CSwapGate( 9, 3, 1 ))
circuit.inst(Gates.RZZGate(3.5190638597992265)( 8, 5 ))
circuit.inst(Gates.SXdgGate( 6 ))
circuit.inst(Gates.HGate( 6 ))
circuit.inst(Gates.RZXGate(3.656646631785722)( 0, 9 ))
circuit.inst(Gates.HGate( 3 ))
circuit.inst(Gates.XGate( 7 ))



from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary(circuit, 10)

