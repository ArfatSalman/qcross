from cirq.contrib.qasm_import import circuit_from_qasm

qasm = open("a.qasm").read()

c = circuit_from_qasm(qasm)

print(len(c))
