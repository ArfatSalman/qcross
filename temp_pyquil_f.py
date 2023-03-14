from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output


circuit = Program()

qr = circuit.declare("ro", "BIT", 11)


defns = get_custom_get_definitions(
    "YGate",
    "CZGate",
    "TdgGate",
    "ECRGate",
    "U3Gate",
    "RZXGate",
    "CRXGate",
    "RC3XGate",
    "CU1Gate",
    "IGate",
    "SGate",
    "TGate",
    "RYYGate",
)

circuit += defns

circuit.inst(Gates.TGate(1))
circuit.inst(Gates.CU1Gate(5.713694233620641, 2, 9))
circuit.inst(Gates.RC3XGate(1, 0, 7, 9))
circuit.inst(Gates.ECRGate(6, 7))
circuit.inst(Gates.SGate(10))
circuit.inst(Gates.CZGate(0, 6))
circuit.inst(Gates.IGate(10))
circuit.inst(Gates.RC3XGate(0, 2, 10, 3))
circuit.inst(Gates.CZGate(6, 5))
circuit.inst(Gates.TdgGate(3))
circuit.inst(Gates.U3Gate(2.045080945478978, 5.634627019822432, 3.620571135922558)(2))
circuit.inst(Gates.SGate(5))
circuit.inst(Gates.RZXGate(2.051069421056634)(0, 3))
circuit.inst(Gates.RZXGate(2.702546578238335)(3, 5))
circuit.inst(Gates.YGate(0))
circuit.inst(Gates.RYYGate(3.964915686973349)(2, 3))
circuit.inst(Gates.RC3XGate(1, 2, 3, 0))
circuit.inst(Gates.CRXGate(0.48340507240790564, 7, 10))

circuit += Pragma("INITIAL_REWIRING", ['"PARTIAL"'])

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


result = qc.run(executable).readout_data.get("ro")

counts = get_qiskit_like_output(result)
RESULT = counts


if __name__ == "__main__":
    from utils import display_results

    display_results({"result": RESULT})
