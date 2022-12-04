import cirq
from cirq.circuits.qasm_output import QasmUGate
import numpy as np
import math
from cmath import exp
from functools import reduce


class RZZGate(cirq.Gate):
    def __init__(self, theta):
        super(RZZGate, self)
        self.theta = theta

    def _num_qubits_(self):
        return 2

    def _unitary_(self):
        """Return a numpy.array for the RZZ gate."""

        itheta2 = 1j * float(self.theta) / 2
        return np.array(
            [
                [exp(-itheta2), 0, 0, 0],
                [0, exp(itheta2), 0, 0],
                [0, 0, exp(itheta2), 0],
                [0, 0, 0, exp(-itheta2)],
            ]
        )

    def _circuit_diagram_info_(self, args):
        return "@", f"RZZ({self.theta:.2f})"


class ECRGate(cirq.Gate):
    def __init__(self):
        super(ECRGate, self)

    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        pi = np.pi
        q0, q1 = qubits

        yield RZXGate(pi / 4)(q0, q1)
        yield cirq.X(q0)
        yield RZXGate(-pi / 4)(q0, q1)

    def _circuit_diagram_info_(self, args):
        return "@", "ECR"


class RZXGate(cirq.Gate):
    def __init__(self, theta):
        super(RZXGate, self)
        self.theta = theta

    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        # gate rzx(param0) q0,q1 { h q1; cx q0,q1; rz(1) q1; cx q0,q1; h q1; }
        q0, q1 = qubits

        yield cirq.H(q1)
        yield cirq.CX(q0, q1)
        yield cirq.rz(self.theta)(q1)
        yield cirq.CX(q0, q1)
        yield cirq.H(q1)

    def _circuit_diagram_info_(self, args):
        return "@", "RZX"


class SXdgGate(cirq.Gate):
    def __init__(self):
        super(SXdgGate, self)

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]]) / 2

    def _circuit_diagram_info_(self, args):
        return "SXdg"


class iSwapGate(cirq.Gate):
    def __init__(self):
        super(iSwapGate, self)

    def _num_qubits_(self):
        return 2

    def _unitary_(self):
        return np.array([[1, 0, 0, 0], [0, 0, 1j, 0], [0, 1j, 0, 0], [0, 0, 0, 1]])

    def _circuit_diagram_info_(self, args):
        return "@", "iSwap"


class CSXGate(cirq.Gate):
    def __init__(self):
        super(CSXGate, self)

    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        pi = np.pi
        a, b = qubits
        yield cirq.H(b)
        yield CU1Gate(pi / 2)(a, b)
        yield cirq.H(b)

    def _circuit_diagram_info_(self, args):
        return "@", "CSX"


class CU1Gate(cirq.Gate):
    def __init__(self, eith):
        super(CU1Gate, self)
        self.eith = eith

    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        a, b = qubits
        angle = self.eith

        yield U1Gate(angle / 2)(a)
        yield cirq.CX(a, b)
        yield U1Gate(-angle / 2)(b)
        yield cirq.CX(a, b)
        yield U1Gate(angle / 2)(b)

    def _circuit_diagram_info_(self, args):
        return f"CU1({self.eith:.2f})", "CU1"


class U1Gate(cirq.Gate):
    def __init__(self, lam):
        super(U1Gate, self)
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _decompose_(self, qubits):
        (a,) = qubits
        yield PhaseGate(self.lam)(a)

    def _circuit_diagram_info_(self, args):
        return f"U1({self.lam:.2f})"


class PhaseGate(cirq.Gate):
    def __init__(self, lam):
        super(PhaseGate, self)
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        """Return a numpy.array for the Phase gate."""
        lam = float(self.lam)
        return np.array([[1, 0], [0, exp(1j * lam)]])

    def _circuit_diagram_info_(self, args):
        return f"Phase({self.lam:.2f})"


class RYYGate(cirq.Gate):
    def __init__(self, theta):
        super(RYYGate, self)
        self.theta = theta

    def _num_qubits_(self):
        return 2

    def _unitary_(self):
        """Return a numpy.array for the RYY gate."""
        theta = float(self.theta)
        cos = math.cos(theta / 2)
        isin = 1j * math.sin(theta / 2)
        return np.array(
            [
                [cos, 0, 0, isin],
                [0, cos, -isin, 0],
                [0, -isin, cos, 0],
                [isin, 0, 0, cos],
            ],
        )

    def _circuit_diagram_info_(self, args):
        return "@", "RYY"


class SXGate(cirq.Gate):
    def __init__(self):
        super(SXGate, self)

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        """Return a numpy.array for the SX gate."""
        return np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]]) / 2

    def _circuit_diagram_info_(self, args):
        return "SX"


qr = [cirq.NamedQubit("q" + str(i)) for i in range(2)]
circuit = cirq.Circuit(
    RZZGate(6.163759533339787)(qr[1], qr[0]),
    cirq.X(qr[1]),
    ECRGate()(qr[1], qr[0]),
    (cirq.X ** (-1 / 2))(qr[0]),
    cirq.X(qr[0]),
    iSwapGate()(qr[1], qr[0]),
    CSXGate()(qr[0], qr[1]),
    cirq.X(qr[1]),
    RYYGate(1.977559237989846)(qr[0], qr[1]),
    cirq.T(qr[1]),
    SXGate()(qr[1]),
    cirq.rx(5.987304452123941).controlled().on(qr[0], qr[1]),
    cirq.H.controlled().on(qr[0], qr[1]),
    cirq.measure(qr[0], key="cr0"),
    cirq.measure(qr[1], key="cr1"),
)

UNITARY = cirq.unitary(circuit)


simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=346)
result_dict = dict(result.multi_measurement_histogram(keys=["cr0", "cr1"]))
keys = list(
    map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys())
)
counts = dict(zip(keys, [value for value in result_dict.values()]))
RESULT = counts
