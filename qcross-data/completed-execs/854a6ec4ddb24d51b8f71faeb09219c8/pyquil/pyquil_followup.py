
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 6)

p_5a7038 = circuit.declare('p_5a7038', 'REAL')
p_7d6e79 = circuit.declare('p_7d6e79', 'REAL')
p_9f724d = circuit.declare('p_9f724d', 'REAL')
p_e94aea = circuit.declare('p_e94aea', 'REAL')
p_52b317 = circuit.declare('p_52b317', 'REAL')
p_320da9 = circuit.declare('p_320da9', 'REAL')
p_2b203d = circuit.declare('p_2b203d', 'REAL')
p_334c70 = circuit.declare('p_334c70', 'REAL')
p_94dcf5 = circuit.declare('p_94dcf5', 'REAL')

defns = get_custom_get_definitions("C3SXGate", "CCXGate", "ZGate", "RZXGate", "RZGate", "TGate", "CRZGate", "RCCXGate", "CUGate")

circuit += defns


subcircuit = Program()
subcircuit.inst(Gates.RZGate(p_2b203d, 2 ))
subcircuit.inst(Gates.TGate( 1 ))
subcircuit.inst(Gates.CUGate(p_320da9, p_52b317, 5.631160518436971, p_7d6e79, 0, 3 ))
subcircuit.inst(Gates.TGate( 2 ))
subcircuit.inst(Gates.RZXGate(p_334c70)( 4, 0 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.RZGate(6.163759533339787, 4 ))
circuit.inst(Gates.ZGate( 3 ))
circuit.inst(Gates.CRZGate(p_94dcf5, 2, 4 ))
circuit.inst(Gates.CUGate(p_9f724d, p_e94aea, p_5a7038, 5.987304452123941, 2, 3 ))
circuit.inst(Gates.C3SXGate( 1, 4, 0, 2 ))
circuit.inst(Gates.CCXGate( 1, 5, 0 ))
circuit.inst(Gates.C3SXGate( 4, 3, 5, 0 ))
circuit.inst(Gates.ZGate( 0 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.TGate( 4 ))
circuit.inst(Gates.RCCXGate( 5, 3, 4 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])




circuit.wrap_in_numshots_loop(1385)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)



params = {
    "p_5a7038": 2.3864521352475245,
    "p_7d6e79": 2.9151388486514547,
    "p_9f724d": 0.5112149185250571,
    "p_e94aea": 5.897054719225356,
    "p_52b317": 2.696266694818697,
    "p_320da9": 4.229610589867865,
    "p_2b203d": 3.672121211148789,
    "p_334c70": 4.563562108824195,
    "p_94dcf5": 4.2641612072511235
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

