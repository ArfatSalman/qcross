
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program( Pragma('INITIAL_REWIRING', ['"PARTIAL"']) )

qr = circuit.declare("ro", "BIT", 2)



defns = get_custom_get_definitions("XGate", "RYYGate", "CRZGate", "CU1Gate", "RZZGate", "CRXGate", "iSwapGate", "SXGate", "HGate", "ECRGate", "CHGate", "TGate", "CSXGate", "RZGate", "SXdgGate")

circuit += defns

circuit.inst(Gates.RZZGate(6.163759533339787)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(1.977559237989846)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(5.987304452123941, 0, 1 ))

subcircuit = Program()
subcircuit.inst(Gates.HGate( 1 ))
subcircuit.inst(Gates.RZZGate(6.1292830756636185)( 0, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(2.2498881927557752, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(5.320621737498446, 1 ))
circuit.inst(Gates.RZGate(5.512260524440591, 1 ))
circuit.inst(Gates.CU1Gate(1.6723037552953224, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(6.086884486572108)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(3.3705408413231095)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(5.190931186022931, 1 ))
circuit.inst(Gates.XGate( 1 ))

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

