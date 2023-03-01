from pytket import Circuit

circ = Circuit(2, 2)  # define a circuit with 2 qubits and 2 bits
circ.H(0)  # add a Hadamard gate to qubit 0
circ.Rz(0.25, 0)  # add an Rz gate of angle 0.25*pi to qubit 0
circ.CX(1, 0)  # add a CX gate with control qubit 1 and target qubit 0
circ.measure_all()

print(circ)

from pytket.extensions.qiskit import AerBackend

backend = AerBackend()                                 # connect to the backend
compiled_circ = backend.get_compiled_circuit(circ)           # compile the circuit to satisfy the backend's requirements
handle = backend.process_circuit(compiled_circ, 100)   # submit the job to run the circuit 100 times
counts = backend.get_result(handle).get_counts()       # retrieve and summarise the results
print(counts)