
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        



circuit = Program()

qr = circuit.declare("ro", "BIT", 9)



defns = get_custom_get_definitions("CRZGate", "C3SXGate", "CU3Gate", "CU1Gate", "CUGate", "SGate", "RZGate", "CXGate", "XGate", "CSXGate", "PhaseGate", "ZGate", "SdgGate", "CSwapGate", "RXGate", "SXGate", "CHGate")

circuit += defns

circuit.inst(Gates.RZGate(6.163759533339787, 8 ))
circuit.inst(Gates.CSXGate( 2, 4 ))
circuit.inst(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941, 0, 6 ))
circuit.inst(Gates.SdgGate( 1 ))
circuit.inst(Gates.C3SXGate( 0, 8, 7, 5 ))
circuit.inst(Gates.ZGate( 2 ))
circuit.inst(Gates.XGate( 5 ))
circuit.inst(Gates.SGate( 0 ))
circuit.inst(Gates.SGate( 8 ))
circuit.inst(Gates.C3SXGate( 1, 3, 2, 0 ))
circuit.inst(Gates.SXGate( 0 ))
circuit.inst(Gates.CU1Gate(3.2142159669963557, 8, 3 ))
circuit.inst(Gates.CRZGate(1.4112277317699358, 5, 8 ))
circuit.inst(Gates.ZGate( 2 ))

subcircuit = Program()
subcircuit.inst(Gates.CSwapGate( 0, 1, 6 ))
subcircuit.inst(Gates.CXGate( 2, 0 ))
subcircuit.inst(Gates.PhaseGate(1.7897858384938228, 0 ))
subcircuit.inst(Gates.CU3Gate(3.950837470808744, 0.31862897237472254, 0.35592835823340635, 4, 0 ))
subcircuit.inst(Gates.PhaseGate(5.336667571035288, 0 ))
subcircuit.inst(Gates.CRZGate(4.747288222618085, 1, 5 ))
subcircuit.inst(Gates.RXGate(2.4205260581208594, 5 ))
subcircuit.inst(Gates.CUGate(4.722103101046168, 5.3924725338944945, 4.88987246261121, 1.2497571638956968, 2, 5 ))
subcircuit.inst(Gates.CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004, 3, 1 ))
circuit.inst(subcircuit)
circuit.inst(subcircuit.dagger())

circuit.inst(Gates.CSXGate( 0, 2 ))
circuit.inst(Gates.ZGate( 7 ))
circuit.inst(Gates.CHGate( 6, 1 ))
circuit.inst(Gates.CSXGate( 3, 0 ))
circuit.inst(Gates.CRZGate(2.586208953975239, 1, 2 ))

circuit += MEASURE(0, qr[0])
circuit += MEASURE(1, qr[1])
circuit += MEASURE(2, qr[2])
circuit += MEASURE(3, qr[3])
circuit += MEASURE(4, qr[4])
circuit += MEASURE(5, qr[5])
circuit += MEASURE(6, qr[6])
circuit += MEASURE(7, qr[7])
circuit += MEASURE(8, qr[8])




circuit.wrap_in_numshots_loop(3919)

qc = get_qc("9q-square-qvm", execution_timeout=60, compiler_timeout=60)

executable = qc.compile(circuit, protoquil=True)





result = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == '__main__':
    from utils import display_results
    display_results( {"result": RESULT })

