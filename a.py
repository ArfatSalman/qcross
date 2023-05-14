edges = [
    [0, 1],
    # [0, 6],
    [1, 0],
    [1, 2],
    [2, 1],
    # [2, 5],
    # [3, 1],
    # [4, 5],
    # [5, 2],
    # [5, 4],
    # [5, 6],
    # [6, 0],
    # [6, 5],
]

import cirq
import networkx as nx
from bloqs.ext.cirq.utils import get_qiskit_like_output

q = cirq.LineQubit.range(3)
qc = cirq.Circuit()
qc.append(cirq.H(q[0]))
qc.append(cirq.CNOT(q[2], q[0]))

qc.append(cirq.measure(q[0], key="cr0"))
qc.append(cirq.measure(q[1], key="cr1"))
qc.append(cirq.measure(q[2], key="cr2"))
# qc.append(cirq.measure(q[3], key="cr3"))
# qc.append(cirq.measure(q[4], key="cr4"))
print(qc)


def edge_list_to_cirq_graph(edge_list, nodes=None):
    if nodes is None:
        num_qubits = len(set(item for sublist in edge_list for item in sublist))
        nodes = [cirq.NamedQubit("q" + str(i)) for i in range(num_qubits)]

    graph = nx.Graph()
    for n in nodes:
        graph.add_node(n)

    for e in edge_list:
        graph.add_edge(nodes[e[0]], nodes[e[1]])
    return graph


graph = edge_list_to_cirq_graph(edges)
router = cirq.RouteCQC(graph)
print(router(qc))

simulator = cirq.Simulator()

result = simulator.run(qc, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts_1 = get_qiskit_like_output(result, keys=["cr0", "cr1", "cr2"])

from qcross.utils import display_results


result = simulator.run(router(qc), repetitions=979)
counts = get_qiskit_like_output(result, keys=["cr0", "cr1", "cr2"])

display_results({"cirq": counts_1, "router": counts})
