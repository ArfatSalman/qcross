import cirq

qr = [cirq.NamedQubit("q_" + str(i)) for i in range(2)]

circuit = cirq.Circuit()

circuit.append(cirq.rz(3)(qr[0]))

# As per the docs, qubits are "A list of qubits that the value is being applied to."
qasm = cirq.qasm(
    circuit, args=cirq.QasmArgs(qubit_id_map={qr[1]: "q1"}), qubits=[qr[1]]
)

print(qasm)
# TypeError: AbstractCircuit._qasm_() got an unexpected keyword argument 'qubits'
