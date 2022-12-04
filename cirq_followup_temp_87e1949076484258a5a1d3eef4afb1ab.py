
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from cirq.circuits.qasm_output import QasmUGate
import numpy as np
import math
from cmath import exp
from functools import reduce
        
def apply_transformations(circuit, context=None):
    optimized_circuit = cirq.expand_composite(circuit)

    optimized_circuit = cirq.drop_empty_moments(optimized_circuit)

    optimized_circuit = cirq.defer_measurements(optimized_circuit)

    optimized_circuit = cirq.drop_negligible_operations(optimized_circuit)

    optimized_circuit = cirq.synchronize_terminal_measurements(optimized_circuit)

    optimized_circuit = cirq.eject_z(optimized_circuit, eject_parameterized=True)

    optimized_circuit = cirq.stratified_circuit(optimized_circuit)

    optimized_circuit = cirq.eject_phased_paulis(optimized_circuit, eject_parameterized=True)

    optimized_circuit = cirq.merge_k_qubit_unitaries(
                optimized_circuit, k=2, rewriter=lambda op: op.with_tags("merged"), context=context)

    # Assert the original and optimized circuit are equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(
        circuit, optimized_circuit
    )

    return optimized_circuit

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

    

qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]
circuit = cirq.Circuit(
  cirq.rz(6.163759533339787)(qr[3]), 
  cirq.rz(4.2641612072511235).controlled().on(qr[6], qr[2]), 
  cirq.Z(qr[1]), 
  cirq.CCX( qr[5], qr[9], qr[7]  ), 
  cirq.Z(qr[2]), 
  cirq.X( qr[7] ), 
  RCCXGate()(qr[10], qr[6], qr[8]), 
  cirq.rz(4.229610589867865)(qr[0]), 
  cirq.measure(qr[0], key='cr0'), 
  cirq.measure(qr[1], key='cr1'), 
  cirq.measure(qr[2], key='cr2'), 
  cirq.measure(qr[3], key='cr3'), 
  cirq.measure(qr[4], key='cr4'), 
  cirq.measure(qr[5], key='cr5'), 
  cirq.measure(qr[6], key='cr6'), 
  cirq.measure(qr[7], key='cr7'), 
  cirq.measure(qr[8], key='cr8'), 
  cirq.measure(qr[9], key='cr9'), 
  cirq.measure(qr[10], key='cr10')
)

UNITARY = cirq.unitary(circuit)



circuit = apply_transformations(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=7838)
result_dict = dict(result.multi_measurement_histogram(keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10']))
keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = dict(zip(keys,[value for value in result_dict.values()]))
RESULT = counts
