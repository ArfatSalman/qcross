"""Generators for Python source code representing fuzzed circuits.

This API could support multiple platforms. We start with Qiskit.
"""


import uuid


from abc import ABC
from abc import abstractmethod
from typing import List, Dict, Any, Tuple
import numpy as np
import math
import random


class Fuzzer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate_circuit_via_atomic_ops(
        self,
        gate_set: List[Dict[str, Any]],
        n_qubits: int,
        n_ops: int,
        force_circuit_identifier: str,
        force_classical_reg_identifier: str,
        force_quantum_reg_identifier: str,
        only_circuit: bool,
    ) -> Tuple[str, Dict[str, str]]:
        pass

    def generate_file(
        self,
        gate_set: List[Dict[str, Any]],
        n_qubits: int,
        n_ops: int,
        optimizations: List[str],
        backend: str,
        shots: int,
        level_auto_optimization: int,
        target_gates: List[str],
    ):
        py_file = ""
        py_file += self.circuit_prologue()
        circuit, metadata_circuit = self.generate_circuit_via_atomic_ops(
            gate_set=gate_set,
            n_qubits=n_qubits,
            n_ops=n_ops,
            force_circuit_identifier="qc",
            force_classical_reg_identifier="cr",
            force_quantum_reg_identifier="qr",
        )
        py_file += circuit
        py_file += self.register_measure(
            id_target_circuit=metadata_circuit["circuit_id"],
            id_quantum_reg=metadata_circuit["id_quantum_reg"],
            id_classical_reg=metadata_circuit["id_classical_reg"],
        )
        # py_file += self.circuit_optimization_passes(
        #     id_target_circuit=metadata_circuit["circuit_id"],
        #     optimizations=optimizations)
        py_file += self.circuit_optimization_levels(
            id_target_circuit=metadata_circuit["circuit_id"],
            level=level_auto_optimization,
            target_gate_set=target_gates,
        )
        py_file += self.circuit_execution(
            id_target_circuit=metadata_circuit["circuit_id"],
            backend=backend,
            shots=shots,
        )
        return py_file, metadata_circuit

    @abstractmethod
    def circuit_prologue(self):
        pass

    # @abstractmethod
    # def circuit_optimization_passes(self, id_target_circuit: str, optimizations: List[str]):
    #     pass

    @abstractmethod
    def circuit_optimization_levels(
        self, id_target_circuit: str, level: int, target_gate_set: List[str] = None
    ):
        pass

    @abstractmethod
    def register_measure(
        self, id_target_circuit: str, id_quantum_reg: str, id_classical_reg: str
    ):
        pass

    @abstractmethod
    def circuit_execution(self, id_target_circuit: str, backend: str, shots: int):
        pass


class QiskitFuzzer(Fuzzer):
    def circuit_prologue(self):
        prologue = "\n# SECTION\n# NAME: PROLOGUE\n\n"
        prologue += "import qiskit\n"
        prologue += (
            "from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister\n"
        )
        prologue += "from qiskit.circuit.library.standard_gates import *\n"
        prologue += "from qiskit.circuit.library import RVGate\n"
        prologue += "from qiskit.circuit import Parameter\n"
        return prologue

    # def circuit_optimization_passes(self, id_target_circuit: str, optimizations: List[str]):
    #     optimization = "\n# SECTION\n# NAME: OPTIMIZATION_PASSES\n\n"
    #     optimization += "from qiskit.transpiler import PassManager\n"
    #     optimization += "from qiskit.transpiler.passes import *\n"
    #     optimization += "passmanager = PassManager()\n"
    #     for opt in optimizations:
    #         optimization += f"passmanager.append({opt}())\n"
    #     optimization += f"{id_target_circuit} = passmanager.run({id_target_circuit})\n"
    #     return optimization

    def circuit_optimization_levels(
        self, id_target_circuit: str, level: int, target_gate_set: List[str] = None
    ):
        optimization = "\n# SECTION\n# NAME: OPTIMIZATION_LEVEL\n\n"
        optimization += "from qiskit import transpile\n"
        optimization += f"{id_target_circuit} = transpile({id_target_circuit}, basis_gates={target_gate_set}, optimization_level={level}, coupling_map=None)\n"
        return optimization

    def register_measure(
        self, id_target_circuit: str, id_quantum_reg: str, id_classical_reg: str
    ):
        measurement = f"\n# SECTION\n# NAME: MEASUREMENT\n\n"
        measurement += (
            f"{id_target_circuit}.measure({id_quantum_reg}, {id_classical_reg})\n"
        )
        return measurement

    def circuit_execution(self, id_target_circuit: str, backend: str, shots: int):
        execution = "\n# SECTION\n# NAME: EXECUTION\n\n"
        execution += "from qiskit import Aer, transpile, execute\n"
        id_backend = "backend_" + str(uuid.uuid4().hex)
        execution += f"{id_backend} = Aer.get_backend('{backend}')\n"
        execution += f"counts = execute({id_target_circuit}, backend={id_backend}, shots={shots}).result().get_counts({id_target_circuit})\n"
        execution += f"RESULT = counts"
        return execution

    def _generate_n_params(self, n_params: int):
        numeric_prams = np.random.uniform(low=0, high=2 * math.pi, size=n_params)
        str_params = [str(e) for e in numeric_prams]
        return ",".join(str_params)

    def _generate_n_qubits(self, register_name: str, n_qubits: int, total_qubits: int):
        if total_qubits == 0:
            return ""
        numeric_qubits = np.random.choice(
            np.arange(total_qubits), n_qubits, replace=False
        )
        str_qubits = [f"{register_name}[{e}]" for e in numeric_qubits]
        return ", ".join(str_qubits)

    def generate_circuit_via_atomic_ops(
        self,
        gate_set: List[Dict[str, Any]],
        n_qubits: int,
        n_ops: int,
        force_circuit_identifier: str = None,
        force_classical_reg_identifier: str = None,
        force_quantum_reg_identifier: str = None,
        only_circuit: bool = False,
        disable_section_header: bool = False,
    ) -> Tuple[str, Dict[str, str]]:
        """Generate a random circuit in qiskit based on the given gateset.

        The circuit is generated by randomly choosing a gate from the gateset.
        qr_0 = QuantumRegister(2, name="qr_0")
        qc_0 = ClassicalRegister(2, name="qc_0")
        c_0 = QuantumCircuit(qr_0, qc_0, name="c_0")


        c_0.append(HGate(), qargs=[qr_0[0]], cargs=[])
        c_0.append(CRZGate(1.25), qargs=[qr_0[0], qr_0[1]], cargs=[])
        c_0.append(UGate(1.25, 2.22, 1.33), qargs=[qr_0[1]], cargs=[])

        """
        # DISABLED BECAUSE IT IS FIXED AT OBJECT INITIALIZATION TIME
        # np.random.seed(self.random_seed)
        if disable_section_header:
            source_code = ""
        else:
            source_code = "\n# SECTION\n# NAME: CIRCUIT\n\n"

        id_quantum_reg = "qr_" + uuid.uuid4().hex
        id_classical_reg = "cr_" + uuid.uuid4().hex
        id_circuit = "c_" + uuid.uuid4().hex
        if force_circuit_identifier is not None:
            id_circuit = force_circuit_identifier
        if force_quantum_reg_identifier is not None:
            id_quantum_reg = force_quantum_reg_identifier
        if force_classical_reg_identifier is not None:
            id_classical_reg = force_classical_reg_identifier

        if not only_circuit:
            source_code += f"{id_quantum_reg} = QuantumRegister({n_qubits}, name='{id_quantum_reg}')\n"
            source_code += f"{id_classical_reg} = ClassicalRegister({n_qubits}, name='{id_classical_reg}')\n"
        source_code += f"{id_circuit} = QuantumCircuit({id_quantum_reg}, {id_classical_reg}, name='{id_circuit}')\n"

        # on very small circuits some gates cannot be used because we do not
        # have enough qubits
        compatible_gate_set = [g for g in gate_set if n_qubits >= g["n_bits"]]

        gates_in_circuit = set()

        if n_qubits > 0:
            # we add operations only if we have at least one qubit
            for i_op in range(n_ops):
                op = np.random.choice(compatible_gate_set, 1)[0]
                i_instr = f'{id_circuit}.append({op["name"]}('
                gates_in_circuit.add(op["name"])
                if op["n_params"] > 0:
                    list_params: str = self._generate_n_params(n_params=op["n_params"])
                    i_instr += f"{list_params}"
                list_involved_qubits: str = self._generate_n_qubits(
                    register_name=id_quantum_reg,
                    n_qubits=op["n_bits"],
                    total_qubits=n_qubits,
                )
                i_instr += f"), qargs=[{list_involved_qubits}], cargs=[])\n"

                source_code += i_instr

        metadata = {
            "circuit_id": id_circuit,
            "id_quantum_reg": id_quantum_reg,
            "id_classical_reg": id_classical_reg,
            "gate_set": compatible_gate_set,
            "gates_in_circuit": list(gates_in_circuit),
        }

        return source_code, metadata


class QiskitSeparableFuzzer(QiskitFuzzer):
    def generate_circuit_via_atomic_ops(
        self,
        gate_set: List[Dict[str, Any]],
        n_qubits: int,
        n_ops: int,
        force_circuit_identifier: str = None,
        force_classical_reg_identifier: str = None,
        force_quantum_reg_identifier: str = None,
        only_circuit: bool = False,
    ) -> Tuple[str, Dict[str, str]]:
        """Generate a circuit composed of 2 untangled qubits partitions."""
        if n_qubits < 2:
            raise ValueError("n_qubits must be >= 2 to have separable circuits")

        size_partition_1 = random.randint(1, n_qubits - 1)
        size_partition_2 = n_qubits - size_partition_1

        partition_1, metadata_1 = QiskitFuzzer.generate_circuit_via_atomic_ops(
            self,
            gate_set=gate_set,
            n_qubits=size_partition_1,
            n_ops=n_ops,
            force_circuit_identifier="qc_1",
            force_classical_reg_identifier="cr_1",
            force_quantum_reg_identifier="qr_1",
            disable_section_header=True,
        )
        partition_2, metadata_2 = QiskitFuzzer.generate_circuit_via_atomic_ops(
            self,
            gate_set=gate_set,
            n_qubits=size_partition_2,
            n_ops=n_ops,
            force_circuit_identifier="qc_2",
            force_classical_reg_identifier="cr_2",
            force_quantum_reg_identifier="qr_2",
            disable_section_header=True,
        )
        main_cir, metadata_main = QiskitFuzzer.generate_circuit_via_atomic_ops(
            self,
            gate_set=gate_set,
            n_qubits=n_qubits,
            n_ops=0,
            force_circuit_identifier="qc_main",
            force_classical_reg_identifier="cr_main",
            force_quantum_reg_identifier="qr_main",
        )
        source_code = f"{main_cir}\n{partition_1}\n{partition_2}\n"
        source_code += f"qc_main.append(qc_1, qargs=qr_main[:{size_partition_1}], cargs=cr_main[:{size_partition_1}])\n"
        source_code += f"qc_main.append(qc_2, qargs=qr_main[{size_partition_1}:], cargs=cr_main[{size_partition_1}:])\n"
        metadata = {
            **metadata_main,
            **{"partition_1_" + k: v for k, v in metadata_1.items()},
            **{"partition_2_" + k: v for k, v in metadata_2.items()},
        }
        metadata["gates_in_circuit"] = list(set(metadata_1).union(set(metadata_2)))
        return source_code, metadata
