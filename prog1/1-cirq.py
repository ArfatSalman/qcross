import cirq
import numpy as np

"""Define a custom single-qubit gate."""

class C3SXGate(cirq.Gate):
    def __init__(self):
        super(C3SXGate, self)

    def _num_qubits_(self):
        return 4

    def _decompose_(self, qubits):
        angle = np.pi / 8
        q = qubits

        yield cirq.H(q[3])
        yield CU1Gate(angle)(q[0], q[3])
        yield cirq.H(q[3])
        yield cirq.X.controlled(q[0], q[1])
        yield cirq.H(q[3])
        yield CU1Gate(-angle)([q[1], q[3]])
        yield cirq.H(q[3])
        yield cirq.X.controlled(q[0], q[1])
        yield cirq.H(q[3])
        yield CU1Gate(angle)(q[1], q[3])
        yield cirq.H(q[3])
        yield cirq.X.controlled(q[1], q[2])
        yield cirq.H(q[3])
        yield CU1Gate(-angle)([q[2], q[3]])
        yield cirq.H(q[3])
        yield cirq.X.controlled(q[0], q[2])
        yield cirq.H(q[3])
        yield CU1Gate(angle)(q[2], q[3])
        yield cirq.H(q[3])
        yield cirq.X.controlled(q[1], q[2])
        yield cirq.H(q[3])
        yield CU1Gate(-angle)([q[2], q[3]])
        yield cirq.H(q[3])
        yield cirq.X.controlled(q[0], q[2])
        yield cirq.H(q[3])
        yield CU1Gate(angle)(q[2], q[3])
        yield cirq.H(q[3])

    def _circuit_diagram_info_(self, args):
        return "C3SX"

class SXdgGate(cirq.Gate):
    def __init__(self):
        super(SXdgGate, self)

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]]) / 2

    def _circuit_diagram_info_(self, args):
        return "SXdg"

class RXGate(cirq.Gate):
    def __init__(self, theta):
        super(RXGate, self)
        self.theta = theta

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        cos = np.cos(self.theta / 2)
        sin = np.sin(self.theta / 2)
        return np.array([[cos, -1j * sin], [-1j * sin, cos]])

    def _circuit_diagram_info_(self, args):
        return f"RX({self.theta:.2f})"

class U1Gate(cirq.Gate):
    def __init__(self, lam):
        super(U1Gate, self)
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        lam = float(self.lam)
        return np.array([[1, 0], [0, np.exp(1j * lam)]])

    def _circuit_diagram_info_(self, args):
        return f"U1({self.lam})"

class CRXGate(cirq.Gate):
    def __init__(self, theta):
        super(CRXGate, self)
        self.theta = theta

    def _num_qubits_(self):
        return 2

    def _unitary_(self):
        half_theta = float(self.theta) / 2
        cos = np.cos(half_theta)
        isin = 1j * np.sin(half_theta)
        return np.array(
                [[1, 0, 0, 0], [0, cos, 0, -isin], [0, 0, 1, 0], [0, -isin, 0, cos]]
            )

    def _circuit_diagram_info_(self, args):
        return f"@", f"CRX({self.theta})"

class CU1Gate(cirq.Gate):
    def __init__(self, eith):
        super(CU1Gate, self)
        self.eith = eith

    def _num_qubits_(self):
        return 2

    def _unitary_(self):
        return np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, np.exp(1j * self.eith)],
            ]
        )

    def _circuit_diagram_info_(self, args):
        return f"CU1({self.eith})", "CU1"


class C4XGate(cirq.Gate):
    def __init__(self):
        super(C4XGate, self)

    def _num_qubits_(self):
        return 5

    def _unitary_(self):
        return np.array([[(1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j)], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j], [0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j]])

    def _circuit_diagram_info_(self, args):
        return (
            "C4X",
            "•",
            "•",
            "•",
            "•",
        )

class RCCXGate(cirq.Gate):
    def __init__(self):
        super(RCCXGate, self)

    def _num_qubits_(self):
        return 3

    def _unitary_(self):
        return np.array(
                [
                    [1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, -1j],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, -1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1j, 0, 0, 0, 0],
                ]
            )

    def _circuit_diagram_info_(self, args):
        return (
            "RCCX",
            "•",
            "•",
        )


CU1 = CU1Gate(5.83674944466042)
C4X = C4XGate()
RCCX = RCCXGate()

# Pick a qubit.
qr = cirq.LineQubit.range(4)

# Create a circuit
circuit = cirq.Circuit(
    cirq.Y(qr[3]),
    cirq.measure(qubit, key="m"),  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)
