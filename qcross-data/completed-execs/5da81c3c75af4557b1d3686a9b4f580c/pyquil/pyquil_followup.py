
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_85e5ed = circuit.declare('p_85e5ed', 'REAL')

defns = get_custom_get_definitions("SXdgGate", "XGate", "CSXGate", "RZZGate", "RYYGate", "ECRGate", "TGate", "iSwapGate")

circuit += defns

circuit.inst(Gates.RZZGate(6.163759533339787)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_85e5ed)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))

qr_04a3f1 = circuit.declare("qr_04a3f1", "BIT", 9)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_85e5ed": 1.977559237989846
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        


quil_out = circuit.out()
circuit = parse_program(quil_out) # new circuit


result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })
