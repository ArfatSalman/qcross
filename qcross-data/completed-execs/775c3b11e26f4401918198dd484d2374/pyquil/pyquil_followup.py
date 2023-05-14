
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 3)

p_c99d8f = circuit.declare('p_c99d8f', 'REAL')
p_9cd4bb = circuit.declare('p_9cd4bb', 'REAL')
p_bacf18 = circuit.declare('p_bacf18', 'REAL')
p_a85ee4 = circuit.declare('p_a85ee4', 'REAL')
p_a479d9 = circuit.declare('p_a479d9', 'REAL')
p_85569c = circuit.declare('p_85569c', 'REAL')
p_8880d3 = circuit.declare('p_8880d3', 'REAL')
p_fece30 = circuit.declare('p_fece30', 'REAL')
p_dd152f = circuit.declare('p_dd152f', 'REAL')

defns = get_custom_get_definitions("SdgGate", "RCCXGate", "U3Gate", "CSXGate", "CRXGate", "XGate", "SXGate", "CU3Gate", "IGate", "SXdgGate", "RZGate", "SGate", "CHGate", "U2Gate", "iSwapGate")

circuit += defns

circuit.inst(Gates.RZGate(p_bacf18, 1 ))
circuit.inst(Gates.CHGate( 2, 0 ))

subcircuit = Program()
subcircuit.inst(Gates.U2Gate(p_85569c, p_8880d3)( 2 ))
subcircuit.inst(Gates.IGate( 1 ))
subcircuit.inst(Gates.RCCXGate( 2, 0, 1 ))
subcircuit.inst(Gates.SXGate( 1 ))
subcircuit.inst(Gates.CU3Gate(6.086884486572108, p_a479d9, p_dd152f, 2, 0 ))
subcircuit.inst(Gates.U3Gate(p_fece30, p_a85ee4, p_9cd4bb)( 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.SXdgGate( 2 ))
circuit.inst(Gates.iSwapGate( 2, 1 ))
circuit.inst(Gates.CSXGate( 1, 0 ))
circuit.inst(Gates.XGate( 2 ))
circuit.inst(Gates.SGate( 2 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.CRXGate(p_c99d8f, 0, 2 ))
circuit.inst(Gates.SGate( 2 ))

qr_f02815 = circuit.declare("qr_f02815", "BIT", 7)

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])




circuit.wrap_in_numshots_loop(489)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_c99d8f": 5.987304452123941,
    "p_9cd4bb": 1.2128092629174942,
    "p_bacf18": 6.163759533339787,
    "p_a85ee4": 5.190931186022931,
    "p_a479d9": 3.06538533241841,
    "p_85569c": 0.03501337194718552,
    "p_8880d3": 2.6397681660693015,
    "p_fece30": 5.01836135520768,
    "p_dd152f": 1.7532443887147882
}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        



result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

