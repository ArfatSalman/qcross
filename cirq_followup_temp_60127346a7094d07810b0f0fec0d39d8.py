
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from cirq.circuits.qasm_output import QasmUGate
import numpy as np
import math
from cmath import exp
from functools import reduce
        
def apply_transformations(circuit, context=None):
    optimized_circuit = cirq.expand_composite(circuit)

    optimized_circuit = cirq.eject_z(optimized_circuit, eject_parameterized=True)

    optimized_circuit = cirq.eject_phased_paulis(optimized_circuit, eject_parameterized=True)

    optimized_circuit = cirq.synchronize_terminal_measurements(optimized_circuit)

    optimized_circuit = cirq.stratified_circuit(optimized_circuit)

    optimized_circuit = cirq.drop_empty_moments(optimized_circuit)

    optimized_circuit = cirq.drop_negligible_operations(optimized_circuit)

    optimized_circuit = cirq.defer_measurements(optimized_circuit)

    optimized_circuit = cirq.merge_k_qubit_unitaries(
                optimized_circuit, k=2, rewriter=lambda op: op.with_tags("merged"), context=context)

    # Assert the original and optimized circuit are equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(
        circuit, optimized_circuit
    )

    return optimized_circuit

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
    

qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]
circuit = cirq.Circuit(
  cirq.rz(6.163759533339787)(qr[3]), 
  cirq.rz(4.2641612072511235).controlled().on(qr[6], qr[3]), 
  cirq.rx( 5.987304452123941 ).controlled().on(qr[1], qr[7]), 
  cirq.CCX( qr[5], qr[9], qr[7]  ), 
  cirq.Z(qr[2]), 
  cirq.T( qr[9] ), 
  cirq.X( qr[8] ), 
  cirq.rz(4.167661441102218).controlled().on(qr[1], qr[6]), 
  cirq.rz(4.229610589867865)(qr[1]), 
  SXGate()(qr[2]), 
  CSXGate()(qr[4], qr[8]), 
  cirq.CCX( qr[4], qr[9], qr[5]  ), 
  C3SXGate()(qr[2], qr[4], qr[0], qr[9]), 
  CSXGate()(qr[0], qr[2]), 
  cirq.Z(qr[0]), 
  cirq.H.controlled().on( qr[7], qr[1] ), 
  CSXGate()(qr[2], qr[0]), 
  cirq.rz(2.586208953975239).controlled().on(qr[1], qr[2]), 
  cirq.measure(qr[0], key='cr0'), 
  cirq.measure(qr[1], key='cr1'), 
  cirq.measure(qr[2], key='cr2'), 
  cirq.measure(qr[3], key='cr3'), 
  cirq.measure(qr[4], key='cr4'), 
  cirq.measure(qr[5], key='cr5'), 
  cirq.measure(qr[6], key='cr6'), 
  cirq.measure(qr[7], key='cr7'), 
  cirq.measure(qr[8], key='cr8'), 
  cirq.measure(qr[9], key='cr9')
)

UNITARY = cirq.unitary(circuit)



circuit = apply_transformations(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=5542)
result_dict = dict(result.multi_measurement_histogram(keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
RESULT = counts
