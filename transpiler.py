from lib import metamorph
import re
import random
from json import dumps


class GateDefinition:
    U1Gate = """
class U1Gate(cirq.Gate):
    def __init__(self, lam):
        super(U1Gate, self)
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _decompose_(self, qubits):
        a, = qubits
        yield PhaseGate(self.lam)(a)

    def _circuit_diagram_info_(self, args):
        return f"U1({self.lam:.2f})"
    """, [
        "PhaseGate"
    ]

    SXdgGate = """
class SXdgGate(cirq.Gate):
    def __init__(self):
        super(SXdgGate, self)

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]]) / 2

    def _circuit_diagram_info_(self, args):
        return "SXdg"
        """

    CU1Gate = """
class CU1Gate(cirq.Gate):
    def __init__(self, eith):
        super(CU1Gate, self)
        self.eith = eith

    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        a, b = qubits
        angle = self.eith

        yield U1Gate(angle/2)(a)
        yield cirq.CX(a, b)
        yield U1Gate(-angle/2)(b)
        yield cirq.CX(a, b)
        yield U1Gate(angle/2)(b)

    def _circuit_diagram_info_(self, args):
        return f"CU1({self.eith:.2f})", "CU1"
    """, [
        "U1Gate"
    ]

    C3SXGate = """
class C3SXGate(cirq.Gate):
    def __init__(self):
        '''QASM -> c3sqrtx'''
        super(C3SXGate, self)

    def _num_qubits_(self):
        return 4

    def _decompose_(self, qubits):
        pi = np.pi
        a, b, c, d = qubits

        yield cirq.H(d)
        yield CU1Gate(pi/8)(a, d)
        yield cirq.H(d)
        yield cirq.CX(a, b)
        yield cirq.H(d)
        yield CU1Gate(-pi/8)(b, d)
        yield cirq.H(d)
        yield cirq.CX(a, b)
        yield cirq.H(d)
        yield CU1Gate(pi/8)(b, d)
        yield cirq.H(d)
        yield cirq.CX(b, c)
        yield cirq.H(d)
        yield CU1Gate(-pi/8)(c, d)
        yield cirq.H(d)
        yield cirq.CX(a,c)
        yield cirq.H(d)
        yield CU1Gate(pi/8)(c, d)
        yield cirq.H(d)
        yield cirq.CX(b, c)
        yield cirq.H(d)
        yield CU1Gate(-pi/8)(c, d)
        yield cirq.H(d)
        yield cirq.CX(a, c)
        yield cirq.H(d)
        yield CU1Gate(pi/8)(c, d)
        yield cirq.H(d)

    def _circuit_diagram_info_(self, args):
        return "@", '@', '@', 'C3SX'
    """, [
        "CU1Gate"
    ]

    C4XGate = """
class C4XGate(cirq.Gate):
    def __init__(self):
        super(C4XGate, self)

    def _num_qubits_(self):
        return 5

    def _decompose_(self, qubits):
        a, b, c, d, e = qubits
        pi = np.pi

        yield cirq.H(e)
        yield CU1Gate(pi/2)(d, e)
        yield cirq.H(e)
        yield RC3XGate()(a,b,c,d)
        yield cirq.H(e)
        yield CU1Gate(-pi/2)(d, e)
        yield cirq.H(e)
        yield RC3XGate_inv()(a,b,c,d)
        yield C3SXGate()(a,b,c,e)

    def _circuit_diagram_info_(self, args):
        return '@', "@", '@', '@', 'C3SX'
    """, [
        "RC3XGate",
        "C3SXGate",
        "RC3XGate_inv",
    ]

    UGate = """
class UGate(cirq.Gate):
    def __init__(self, theta, phi, lam):
        super(UGate, self)
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        ''' Return a numpy.array for the U gate. '''
        theta, phi, lam = self.theta, self.phi, self.lam
        cos = math.cos(theta / 2)
        sin = math.sin(theta / 2)
        return np.array(
            [
                [cos, -exp(1j * lam) * sin],
                [exp(1j * phi) * sin, exp(1j * (phi + lam)) * cos],
            ],
            dtype=complex,
        )

    def _circuit_diagram_info_(self, args):
        return "U"
    """

    U3Gate = UGate

    U2Gate = """
class U2Gate(cirq.Gate):
    def __init__(self, phi, lam):
        super(U2Gate, self)
        self.theta = np.pi / 2
        self.phi = phi
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        '''Return a Numpy.array for the U2 gate.'''
        isqrt2 = 1 / math.sqrt(2)
        phi, lam = self.phi, self.lam
        phi, lam = float(phi), float(lam)
        return np.array(
            [
                [isqrt2, -exp(1j * lam) * isqrt2],
                [exp(1j * phi) * isqrt2, exp(1j * (phi + lam)) * isqrt2],
            ]
        )

    def _circuit_diagram_info_(self, args):
        return "U2"
    """

    RYYGate = """
class RYYGate(cirq.Gate):
    
    def __init__(self, theta):
        super(RYYGate, self)
        self.theta = theta
    
    def _num_qubits_(self):
        return 2
    
    def _unitary_(self):
        '''Return a numpy.array for the RYY gate.'''
        theta = float(self.theta)
        cos = math.cos(theta / 2)
        isin = 1j * math.sin(theta / 2)
        return np.array(
            [[cos, 0, 0, isin], [0, cos, -isin, 0], [0, -isin, cos, 0], [isin, 0, 0, cos]],
        )
    
    def _circuit_diagram_info_(self, args):
        return "@", "RYY"
    """

    SXGate = """
class SXGate(cirq.Gate):
    def __init__(self):
        super(SXGate, self)
    
    def _num_qubits_(self):
        return 1
    
    def _unitary_(self):
        '''Return a numpy.array for the SX gate.'''
        return np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]]) / 2
    
    def _circuit_diagram_info_(self, args):
        return "SX"
    """

    CSXGate = """
class CSXGate(cirq.Gate):
    def __init__(self):
        super(CSXGate, self)
    
    def _num_qubits_(self):
        return 2
    
    def _decompose_(self, qubits):
        pi = np.pi
        a, b = qubits
        yield cirq.H(b)
        yield CU1Gate(pi/2)(a, b)
        yield cirq.H(b)

    def _circuit_diagram_info_(self, args):
        return '@', "CSX"
    """, [
        "CU1Gate"
    ]

    PhaseGate = """
class PhaseGate(cirq.Gate):
    def __init__(self, lam):
        super(PhaseGate, self)
        self.lam = lam
    
    def _num_qubits_(self):
        return 1
    
    def _unitary_(self):
        '''Return a numpy.array for the Phase gate.'''
        lam = float(self.lam)
        return np.array([[1, 0], [0, exp(1j * lam)]])
    
    def _circuit_diagram_info_(self, args):
        return f"Phase({self.lam:.2f})"

    """

    CPhaseGate = """
class CPhaseGate(cirq.Gate):
    def __init__(self, eith):
        super(CPhaseGate, self)
        self.eith = eith
    
    def _num_qubits_(self):
        return 2
    
    def _unitary_(self):
        '''Return a numpy.array for the CPhase gate.'''
        eith = exp(1j * float(self.eith))
        return np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, eith]]
            )
    
    def _circuit_diagram_info_(self, args):
        return "@", f"CPhase({self.eith:.2f})"

    """

    DCXGate = """
class DCXGate(cirq.Gate):
    def __init__(self):
        super(DCXGate, self)
    
    def _num_qubits_(self):
        return 2
    
    def _decompose_(self, qubits):
        a, b = qubits
        yield cirq.CX(a, b)
        yield cirq.CX(b, a)

    def _circuit_diagram_info_(self, args):
        return "@", "DCX"
    """

    RZXGate = """
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
        yield cirq.CX(q0,q1)
        yield cirq.rz(self.theta)(q1)
        yield cirq.CX(q0,q1)
        yield cirq.H(q1)

    def _circuit_diagram_info_(self, args):
        return '@', "RZX"
    """

    SdgGate = """
class SdgGate(cirq.Gate):
    def __init__(self):
        super(SdgGate, self)
    
    def _num_qubits_(self):
        return 1
    
    def _unitary_(self):
        return np.array([[1, 0], [0, -1j]])
    
    def _circuit_diagram_info_(self, args):
        return "Sdg"
    """

    RXXGate = """
class RXXGate(cirq.Gate):
    def __init__(self, theta):
        super(RXXGate, self)
        self.theta = theta
    
    def _num_qubits_(self):
        return 2
    
    def _unitary_(self):
        '''Return a Numpy.array for the RXX gate.'''
        theta2 = float(self.theta) / 2
        cos = math.cos(theta2)
        isin = 1j * math.sin(theta2)
        return np.array(
            [[cos, 0, 0, -isin], [0, cos, -isin, 0], [0, -isin, cos, 0], [-isin, 0, 0, cos]]
        )

    
    def _circuit_diagram_info_(self, args):
        return '@', f"RXX({self.theta:.2f})"
    """

    iSwapGate = """
class iSwapGate(cirq.Gate):
    def __init__(self):
        super(iSwapGate, self)
    
    def _num_qubits_(self):
        return 2
    
    def _unitary_(self):
        return np.array([[1, 0, 0, 0], [0, 0, 1j, 0], [0, 1j, 0, 0], [0, 0, 0, 1]])
    
    def _circuit_diagram_info_(self, args):
        return "@", "iSwap"
    """

    RC3XGate = """
class RC3XGate(cirq.Gate):
    def __init__(self):
        super(RC3XGate, self)
    
    def _num_qubits_(self):
        return 4
    
    def _decompose_(self, qubits):
        pi = np.pi
        a, b, c, d = qubits
        yield U2Gate(0,pi)(d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(c,d)
        yield U1Gate(-pi/4)(d)
        yield U2Gate(0,pi)(d)
        yield cirq.CX(a,d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(b,d)
        yield U1Gate(-pi/4)(d)
        yield cirq.CX(a,d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(b,d)
        yield U1Gate(-pi/4)(d)
        yield U2Gate(0,pi)(d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(c,d)
        yield U1Gate(-pi/4)(d)
        yield U2Gate(0,pi)(d)
    
    def _circuit_diagram_info_(self, args):
        return '@', '@', '@', 'RC3X'
    """, [
        "U1Gate",
        "U2Gate",
    ]

    RC3XGate_inv = """
class RC3XGate_inv(cirq.Gate):
    def __init__(self):
        super(RC3XGate_inv, self)
    
    def _num_qubits_(self):
        return 4
    
    def _decompose_(self, qubits):
        pi = np.pi
        a, b, c, d = qubits

        yield U2Gate(-2*pi,pi)(d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(c,d)
        yield U1Gate(-pi/4)(d)
        yield U2Gate(-2*pi,pi)(d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(b,d)
        yield U1Gate(-pi/4)(d)
        yield cirq.CX(a,d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(b,d)
        yield U1Gate(-pi/4)(d)
        yield cirq.CX(a,d)
        yield U2Gate(-2*pi,pi)(d)
        yield U1Gate(pi/4)(d)
        yield cirq.CX(c,d)
        yield U1Gate(-pi/4)(d)
        yield U2Gate(-2*pi,pi)(d)

    def _circuit_diagram_info_(self, args):
        return '@', '@', '@', 'RC3X_inv'
"""

    RCCXGate = """
class RCCXGate(cirq.Gate):
    def __init__(self):
        super(RCCXGate, self)

    def _num_qubits_(self):
        return 3

    def _decompose_(self, qubits):
        pi = np.pi
        a,b,c = qubits

        yield U2Gate(0,pi)(c)
        yield U1Gate(pi/4)(c)
        yield cirq.CX(b, c)
        yield U1Gate(-pi/4)(c)
        yield cirq.CX(a, c)
        yield U1Gate(pi/4)(c)
        yield cirq.CX(b, c)
        yield U1Gate(-pi/4)(c)
        yield U2Gate(0,pi)(c)

    def _circuit_diagram_info_(self, args):
        return '@', '@', 'RC3X'
    """, [
        "U1Gate",
        "U2Gate",
    ]

    RZZGate = """
class RZZGate(cirq.Gate):
    def __init__(self, theta):
        super(RZZGate, self)
        self.theta = theta
    
    def _num_qubits_(self):
        return 2
    
    def _unitary_(self):
        '''Return a numpy.array for the RZZ gate.'''

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
        return '@', f"RZZ({self.theta:.2f})"

    """

    CUGate = """
class CUGate(cirq.Gate):
    def __init__(self, theta, phi, lam, gamma):
        super(CUGate, self)
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.gamma = gamma
    
    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        theta, phi, lam, gamma = self.theta, self.phi, self.lam, self.gamma
        c, t = qubits
        yield PhaseGate(gamma)(c)
        yield PhaseGate((lam+phi)/2)(c)
        yield PhaseGate((lam-phi)/2)(t)
        yield cirq.CX(c, t)
        yield UGate(-theta/2, 0, -(phi+lam)/2)(t)
        yield cirq.CX(c, t)
        yield UGate(theta/2, phi, 0)(t)

    def _circuit_diagram_info_(self, args):
        return  '@', f"CU"

    """, [
        "PhaseGate",
        "UGate",
    ]

    ECRGate = """
class ECRGate(cirq.Gate):
    def __init__(self):
        super(ECRGate, self)
    
    def _num_qubits_(self):
        return 2
    
    def _decompose_(self, qubits):
        pi = np.pi
        q0, q1 = qubits

        yield RZXGate(pi/4)(q0,q1)
        yield cirq.X(q0)
        yield RZXGate(-pi/4)(q0,q1)

    def _circuit_diagram_info_(self, args):
        return  '@', "ECR"
    """, [
        "RZXGate"
    ]


class CirqCircuit:
    def __init__(self, qiskit_source):
        self.qiskit_source = qiskit_source

        registers = metamorph.get_registers_used(qiskit_source)

        for register in registers:
            if register["type"] == "QuantumRegister":
                self.qubits = register["size"]
                self.qubit_id = register["name"]
                break

        self.instructions = metamorph.get_instructions(qiskit_source)
        self.is_follow_up = False

        # self.qubits = qubits
        # self.qubit_id = qubit_id
        self.gates_defined = {}
        self.followup_metadata = {}

    def generic_gate_creator(self, gate_name):
        return ""

    def _qubits_args(self, qubits_pos):
        res = []
        for i in qubits_pos:
            res.append(f"{self.qubit_id}[{str(i)}]")
        return ", ".join(res)

    def IGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"cirq.I( {self._qubits_args(qubit_pos)} )"

    def TGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"cirq.T( {self._qubits_args(qubit_pos)} )"

    def XGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"cirq.X( {self._qubits_args(qubit_pos)} )"

    def HGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"cirq.H( {self._qubits_args(qubit_pos)} )"

    def CHGate(self, qubit_pos, args=None):
        return f"cirq.H.controlled().on( {self._qubits_args(qubit_pos)} )"

    def SGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"cirq.S( {self._qubits_args(qubit_pos)} )"

    def PhaseGate(self, qubit_pos, args):
        assert len(qubit_pos) == 1
        assert len(args) == 1
        return f'PhaseGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def CPhaseGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1
        return f'CPhaseGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def iSwapGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        return f"iSwapGate()( {self._qubits_args(qubit_pos)}  )"

    def UGate(self, qubit_pos, args):
        assert len(qubit_pos) == 1
        assert len(args) == 3
        return f'UGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def CUGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 4
        return f'CUGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def CXGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        return f"cirq.CX( {self._qubits_args(qubit_pos)}  )"

    def YGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"cirq.Y( {self._qubits_args(qubit_pos)} )"

    def ZGate(self, qubit_pos, args):
        assert len(qubit_pos) == 1

        return f"cirq.Z({self._qubits_args(qubit_pos)})"

    def CCXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 3
        return f"cirq.CCX( {self._qubits_args(qubit_pos)}  )"

    def DCXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        return f"DCXGate()({self._qubits_args(qubit_pos)})"

    def SwapGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        return f"cirq.SWAP( { self._qubits_args(qubit_pos)} )"

    def CSwapGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 3
        return f"cirq.SWAP.controlled().on( { self._qubits_args(qubit_pos)} )"

    def CYGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        return f"cirq.Y.controlled().on({ self._qubits_args(qubit_pos)})"

    def RYGate(self, qubit_pos, args):
        assert len(qubit_pos) == 1
        assert len(args) == 1

        return (
            f'cirq.ry( {", ".join(map(str, args))} )({ self._qubits_args(qubit_pos) })'
        )

    def CRYGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1
        return f'cirq.ry( {", ".join(map(str, args))} ).controlled().on({ self._qubits_args(qubit_pos) })'

    def RXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        assert len(args) == 1
        return f'cirq.rx({", ".join(map(str, args))})({ self._qubits_args(qubit_pos) })'

    def RXXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        assert len(args) == 1
        return f'RXXGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def RCCXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 3
        return f"RCCXGate()({ self._qubits_args(qubit_pos) })"

    def ECRGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        return f"ECRGate()({ self._qubits_args(qubit_pos) })"

    def CRXGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1
        return f'cirq.rx( {", ".join(map(str, args))} ).controlled().on({ self._qubits_args(qubit_pos) })'

    def RZGate(self, qubit_pos, args):
        return f'cirq.rz({", ".join(map(str, args))})({ self._qubits_args(qubit_pos) })'

    def CRZGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1
        return f'cirq.rz({", ".join(map(str, args))}).controlled().on({ self._qubits_args(qubit_pos) })'

    def CZGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        return f"cirq.CZ({ self._qubits_args(qubit_pos) })"

    def U1Gate(self, qubit_pos, args):
        assert len(qubit_pos) == 1
        assert len(args) == 1

        return f'U1Gate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def U2Gate(self, qubit_pos, args):
        assert len(qubit_pos) == 1
        assert len(args) == 2
        return f'U2Gate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'
        # return f'QasmUGate(np.pi/2, {", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def U3Gate(self, qubit_pos, args):
        # assert len(qubit_pos) == 1
        # assert len(args) == 3
        # return f'UGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'
        return self.UGate(qubit_pos, args)
        # args = [ f'{arg}/np.pi' for arg in map(str, args) ]
        # return f'QasmUGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def CU1Gate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1

        return f'CU1Gate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def SXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"SXGate()({self._qubits_args(qubit_pos)})"

    def CSXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 2
        return f"CSXGate()({self._qubits_args(qubit_pos)})"

    def SdgGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"SdgGate()({self._qubits_args(qubit_pos)})"

    def TdgGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1
        return f"(cirq.T**(-1))({self._qubits_args(qubit_pos)})"

    def SXdgGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 1

        return f"(cirq.X**(-1/2))({self._qubits_args(qubit_pos)})"

    def RYYGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1

        return f'RYYGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def RZZGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1

        return f'RZZGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def RZXGate(self, qubit_pos, args):
        assert len(qubit_pos) == 2
        assert len(args) == 1

        return f'RZXGate({", ".join(map(str,args))})({self._qubits_args(qubit_pos)})'

    def C3SXGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 4
        return f"C3SXGate()({self._qubits_args(qubit_pos)})"

    def C4XGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 5
        return f"C4XGate()({self._qubits_args(qubit_pos)})"

    def RC3XGate(self, qubit_pos, args=None):
        assert len(qubit_pos) == 4
        return f"RC3XGate()({self._qubits_args(qubit_pos)})"

    def construct_circuit(self, instructions):

        gates_defined = {}

        res = []

        all_defns = []

        for i in instructions:
            gate_name = i["gate"]
            gate_params = i["params"]
            gate_qubits = i["qbits"]

            generate_instruction = getattr(self, gate_name)
            out = generate_instruction(gate_qubits, gate_params)

            custom_gate = hasattr(GateDefinition, gate_name)
            gate_deps_to_add = []

            if custom_gate:
                gate_needs_defn = gates_defined.get(gate_name) is not True
                if gate_needs_defn:
                    gate_source = getattr(GateDefinition, gate_name)
                    gates_defined[gate_name] = True
                    if isinstance(gate_source, tuple):
                        defn, dependencies = gate_source
                        all_defns.append(defn)
                        gate_deps_to_add.extend(dependencies)
                        # for gate in dependencies:
                        #     if not gates_defined[gate]:
                        #         gates_defined[gate] = True
                        #         all_defns.append(getattr(GateDefinition, gate))
                    else:
                        all_defns.append(gate_source)

            while len(gate_deps_to_add):
                gate_name = gate_deps_to_add.pop()

                if gates_defined.get(gate_name) is not True:
                    gates_defined[gate_name] = True
                    gate_source = getattr(GateDefinition, gate_name)
                    if isinstance(gate_source, tuple):
                        all_defns.append(gate_source[0])
                        gate_deps_to_add.extend(gate_source[1])
                    else:
                        all_defns.append(gate_source)
            res.append(out)

        res += self.get_measurement_gates()

        ins = ", \n  ".join(res)

        return (
            f"""
circuit = cirq.Circuit(
  {ins}
)
""",
            all_defns,
        )

    def get_measurement_gates(self):
        res = []
        for i in range(self.qubits):
            res.append(f"cirq.measure({self.qubit_id}[{str(i)}], key='cr{str(i)}')")
        return res

    def prologue(self):
        return f"""
import cirq
from cirq.circuits.qasm_output import QasmUGate
import numpy as np
import math
from cmath import exp
from functools import reduce
        """

    def epilogue(self, shots):
        opt = True
        if opt:
            pass

        measurement_keys = []
        for i in range(self.qubits):
            measurement_keys.append(f"'cr{str(i)}'")

        return f"""
UNITARY = cirq.unitary(circuit)

{ "circuit = apply_transformations(circuit)" if self.is_follow_up else '' }

{self.backend_selection()}
result = simulator.run(circuit, repetitions={shots})
result_dict = dict(result.multi_measurement_histogram(keys=[{', '.join(measurement_keys)}]))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
RESULT = counts
"""

    def generate_named_qubit_registers(self):
        return f"{self.qubit_id} = [cirq.NamedQubit('q' + str(i)) for i in range({self.qubits})]"

    def generate_line_qubit_registers(self):
        return f"{self.qubit_id} = cirq.LineQubit.range({self.qubits})"

    def generate_grid_qubit_registers(self):
        return f"""
lattice = cirq.GridQubit.square(math.ceil({self.qubits} ** 1/2))
{self.qubit_id} = [lattice[i] for i in range({self.qubits})]
        """

    def generate_qubit_registers(self):
        qubits = [
            self.generate_named_qubit_registers,
            self.generate_line_qubit_registers,
            self.generate_grid_qubit_registers,
        ]
        if self.is_follow_up:
            fn = random.choice(qubits)
            self.followup_metadata["qubit_type"] = fn.__name__
            return fn()

        return self.generate_named_qubit_registers()

    def backend_selection(self):
        backends = ["Simulator", "DensityMatrixSimulator"]
        sim = backends[0]
        if self.is_follow_up:
            sim = random.choice(backends)
            self.followup_metadata['backend'] = sim
        return f"simulator = cirq.{sim}()"

    def get_transformations(self):

        transformations_map = {
            "expand_composite": "optimized_circuit = cirq.expand_composite(circuit)",
            "defer_measurements": "optimized_circuit = cirq.defer_measurements(optimized_circuit)",
            "merge_k_qubit_unitaries": """optimized_circuit = cirq.merge_k_qubit_unitaries(
                optimized_circuit, k=2, rewriter=lambda op: op.with_tags("merged"), context=context)""",
            "eject_phased_paulis": "cirq.eject_phased_paulis(optimized_circuit, eject_parameterized=True)",
            "drop_negligible_operations": "cirq.drop_negligible_operations(optimized_circuit)",
            "drop_empty_moments": "optimized_circuit = cirq.drop_empty_moments(optimized_circuit)",
            "synchronize_terminal_measurements": "optimized_circuit = cirq.synchronize_terminal_measurements(optimized_circuit)",
            "eject_z": "optimized_circuit = cirq.eject_z(optimized_circuit, eject_parameterized=True)",
            "stratified_circuit": "optimized_circuit = cirq.stratified_circuit(optimized_circuit)",
        }

        transformations = list(transformations_map.keys())
        transformations.remove('expand_composite')

        random.shuffle(transformations)

        transformations.insert(0, 'expand_composite')

        self.followup_metadata['transformations_order'] = transformations

        optimizations = "\n\n    ".join(
            [transformations_map[key] for key in transformations_map]
        )

        return f"""
def apply_transformations(circuit, context=None):
    {optimizations}

    # Assert the original and optimized circuit are equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(
        circuit, optimized_circuit
    )

    return optimized_circuit
"""

    def get_equivalent(self):
        cirq_source = self.prologue()
        if self.is_follow_up:
            cirq_source += self.get_transformations()

        circuit, defns = self.construct_circuit(self.instructions)

        cirq_source += "\n\n".join(defns)

        cirq_source += "\n\n"

        cirq_source += self.generate_qubit_registers()

        cirq_source += circuit

        match = re.search(r"shots=([0-9]+)", self.qiskit_source)
        if not match:
            raise ValueError("no shots found")
        shots = match.group(1)
        cirq_source += self.epilogue(shots)

        return cirq_source

    def get_follow_up(self):
        self.is_follow_up = True
        source = self.get_equivalent()
        self.is_follow_up = False
        return self.followup_metadata, source

    @staticmethod
    def from_qiskit_source(qiskit_source: str):

        registers = metamorph.get_registers_used(qiskit_source)
        qubit_size = None
        qubit_name = None
        for register in registers:
            if register["type"] == "QuantumRegister":
                qubit_size = register["size"]
                qubit_name = register["name"]
                break

        instructions = metamorph.get_instructions(qiskit_source)

        cirq_ciruit = CirqCircuit(qubit_size, qubit_name)

        cirq_source = cirq_ciruit.prologue()

        cirq_source += cirq_ciruit.get_transformations()

        circuit, defns = cirq_ciruit.construct_circuit(instructions)

        cirq_source += "\n\n".join(defns)

        cirq_source += "\n\n"

        cirq_source += cirq_ciruit.generate_qubit_registers()

        cirq_source += circuit

        match = re.search(r"shots=([0-9]+)", qiskit_source)
        if not match:
            raise ValueError("no shots found")
        shots = match.group(1)
        cirq_source += cirq_ciruit.epilogue(shots)

        return cirq_source


if __name__ == "__main__":
    code = """
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZXGate(3.4148838654876075), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U1Gate(3.916311088799146), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(RYGate(0.30914088102270665), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(2.05519166016469), qargs=[qr[1], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[2]], cargs=[])
qc.append(U1Gate(2.19375409896333), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXXGate(0.6958411378279826), qargs=[qr[1], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U1Gate(2.5118976499714747), qargs=[qr[2]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[2], qr[1], qr[3], qr[0]], cargs=[])
qc.append(U1Gate(5.406194560026072), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(4.385627314003304), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[3]], cargs=[])
qc.append(RYGate(6.139804541076739), qargs=[qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[3], qr[0], qr[2]], cargs=[])
qc.append(UGate(2.7159856050146742, 2.4635653656106844, 5.909205091787408), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(2.730791138901111), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RXXGate(5.4691544369544545), qargs=[qr[3], qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(UGate(1.2541495406941519, 3.6300156777625117, 0.8739290527186184), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e1e30142c35d4d72a6e6051b22e81691 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e1e30142c35d4d72a6e6051b22e81691, shots=692).result().get_counts(qc)
RESULT = counts
"""
    c = CirqCircuit(code)
    a, b = c.get_follow_up()
    print(b)
    print(a)


class QuantumCircuit:
    pass
