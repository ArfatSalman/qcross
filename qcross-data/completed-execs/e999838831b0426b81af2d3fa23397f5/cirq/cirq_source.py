import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output


qr = [cirq.NamedQubit("q" + str(i)) for i in range(3)]


circuit = cirq.Circuit()

circuit.append(
    Gates.U3Gate(4.655749679598676, 2.7381706999194857, 2.740795817289426)(qr[0])
)
circuit.append(Gates.RYYGate(5.171156764260811)(qr[2], qr[1]))
circuit.append(Gates.DCXGate(qr[2], qr[0]))
circuit.append(Gates.U1Gate(4.660569462447812)(qr[1]))
circuit.append(Gates.CPhaseGate(5.442036812415247)(qr[1], qr[0]))
circuit.append(Gates.RYGate(3.1620892961233205)(qr[2]))
circuit.append(Gates.RZGate(2.816396898940768)(qr[2]))
circuit.append(Gates.HGate(qr[0]))

circuit.append(cirq.measure(qr[0], key="cr0"))
circuit.append(cirq.measure(qr[1], key="cr1"))
circuit.append(cirq.measure(qr[2], key="cr2"))


simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=["cr0", "cr1", "cr2"])
RESULT = counts

if __name__ == "__main__":
    import json

    print(json.dumps(RESULT, sort_keys=True))
