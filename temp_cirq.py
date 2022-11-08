
import cirq
from cirq.circuits.qasm_output import QasmUGate
import numpy as np
import math
from cmath import exp
from functools import reduce
        
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

    


class SXdgGate(cirq.Gate):
    def __init__(self):
        super(SXdgGate, self)

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([[1 - 1j, 1 + 1j], [1 + 1j, 1 - 1j]]) / 2

    def _circuit_diagram_info_(self, args):
        return "SXdg"
        


class SdgGate(cirq.Gate):
    def __init__(self):
        super(SdgGate, self)
    
    def _num_qubits_(self):
        return 1
    
    def _unitary_(self):
        return np.array([[1, 0], [0, -1j]])
    
    def _circuit_diagram_info_(self, args):
        return "Sdg"
    


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
    


class iSwapGate(cirq.Gate):
    def __init__(self):
        super(iSwapGate, self)
    
    def _num_qubits_(self):
        return 2
    
    def _unitary_(self):
        return np.array([[1, 0, 0, 0], [0, 0, 1j, 0], [0, 1j, 0, 0], [0, 0, 0, 1]])
    
    def _circuit_diagram_info_(self, args):
        return "@", "iSwap"
    


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
    

qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]
circuit = cirq.Circuit(
  RZXGate(3.4148838654876075)(qr[0], qr[1]), 
  U1Gate(3.916311088799146)(qr[2]), 
  CSXGate()(qr[2], qr[3]), 
  cirq.ry( 0.30914088102270665 )(qr[1]), 
  CPhaseGate(2.05519166016469)(qr[1], qr[2]), 
  cirq.Y( qr[2] ), 
  U1Gate(2.19375409896333)(qr[2]), 
  (cirq.X**(-1/2))(qr[2]), 
  SdgGate()(qr[3]), 
  cirq.H( qr[1] ), 
  cirq.CX( qr[2], qr[0]  ), 
  RXXGate(0.6958411378279826)(qr[1], qr[3]), 
  iSwapGate()( qr[2], qr[0]  ), 
  U1Gate(2.5118976499714747)(qr[2]), 
  RC3XGate()(qr[2], qr[1], qr[3], qr[0]), 
  U1Gate(5.406194560026072)(qr[3]), 
  cirq.H( qr[3] ), 
  RZZGate(4.385627314003304)(qr[1], qr[0]), 
  (cirq.T**(-1))(qr[3]), 
  cirq.ry( 6.139804541076739 )(qr[3]), 
  RC3XGate()(qr[1], qr[3], qr[0], qr[2]), 
  UGate(2.7159856050146742, 2.4635653656106844, 5.909205091787408)(qr[3]), 
  RYYGate(2.730791138901111)(qr[1], qr[2]), 
  RXXGate(5.4691544369544545)(qr[3], qr[2]), 
  iSwapGate()( qr[2], qr[0]  ), 
  cirq.S( qr[0] ), 
  UGate(1.2541495406941519, 3.6300156777625117, 0.8739290527186184)(qr[3]), 
  (cirq.X**(-1/2))(qr[1]), 
  cirq.measure(qr[0], key='cr0'), 
  cirq.measure(qr[1], key='cr1'), 
  cirq.measure(qr[2], key='cr2'), 
  cirq.measure(qr[3], key='cr3')
)

UNITARY = cirq.unitary(circuit)



simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=692)
result_dict = dict(result.multi_measurement_histogram(keys=['cr0', 'cr1', 'cr2', 'cr3']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
RESULT = counts

