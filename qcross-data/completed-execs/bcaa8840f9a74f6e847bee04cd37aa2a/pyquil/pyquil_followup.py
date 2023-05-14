
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 2)

p_42891c = circuit.declare('p_42891c', 'REAL')
p_92144e = circuit.declare('p_92144e', 'REAL')
p_cbf8a5 = circuit.declare('p_cbf8a5', 'REAL')
p_9f3b29 = circuit.declare('p_9f3b29', 'REAL')
p_914ffd = circuit.declare('p_914ffd', 'REAL')
p_155411 = circuit.declare('p_155411', 'REAL')
p_4ab831 = circuit.declare('p_4ab831', 'REAL')
p_e5e350 = circuit.declare('p_e5e350', 'REAL')

defns = get_custom_get_definitions("SXGate", "TGate", "U1Gate", "SGate", "CU3Gate", "iSwapGate", "ECRGate", "CRXGate", "SXdgGate", "CRZGate", "RZZGate", "XGate", "RYYGate", "CHGate", "CU1Gate", "RZGate", "CSXGate", "RYGate", "ZGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.SXGate( 1 ))
subcircuit.inst(Gates.SXGate( 1 ))
subcircuit.inst(Gates.RYGate(5.398622178940033, 0 ))
subcircuit.inst(Gates.XGate( 0 ))
subcircuit.inst(Gates.CU3Gate(1.3471739101750193, 3.2142159669963557, 2.852678572380205, 0, 1 ))
subcircuit.inst(Gates.U1Gate(2.3568871696687452, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZZGate(6.163759533339787)( 1, 0 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.ECRGate( 1, 0 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.XGate( 0 ))
circuit.inst(Gates.iSwapGate( 1, 0 ))
circuit.inst(Gates.CSXGate( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_92144e)( 0, 1 ))
circuit.inst(Gates.TGate( 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.CRXGate(p_e5e350, 0, 1 ))
circuit.inst(Gates.CHGate( 0, 1 ))
circuit.inst(Gates.CRZGate(p_4ab831, 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_914ffd, 1 ))
circuit.inst(Gates.RZGate(5.512260524440591, 1 ))
circuit.inst(Gates.CU1Gate(p_155411, 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RZZGate(6.086884486572108)( 0, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.SXdgGate( 0 ))
circuit.inst(Gates.RYYGate(p_42891c)( 0, 1 ))
circuit.inst(Gates.SXGate( 1 ))
circuit.inst(Gates.RZGate(p_9f3b29, 1 ))
circuit.inst(Gates.XGate( 1 ))
circuit.inst(Gates.RYYGate(p_cbf8a5)( 1, 0 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.CRZGate(4.167661441102218, 1, 0 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])




circuit.wrap_in_numshots_loop(346)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_42891c": 3.3705408413231095,
    "p_92144e": 1.977559237989846,
    "p_cbf8a5": 5.167261531657622,
    "p_9f3b29": 5.190931186022931,
    "p_914ffd": 5.320621737498446,
    "p_155411": 1.6723037552953224,
    "p_4ab831": 2.2498881927557752,
    "p_e5e350": 5.987304452123941
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

