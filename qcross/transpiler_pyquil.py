from lib import metamorph
from functools import partial
import re
import random
from json import dumps
from termcolor import colored
from qcross.utils import fix_cx3, convert_morphq_metadata, display_results
import itertools


def random_derangement(orig):
    for s in itertools.permutations(orig):
        if not any(a == b for a, b in zip(s, orig)):
            yield list(s)


class GateDefinition:
    pass


class PyQuilCircuit:
    def __init__(
        self, qiskit_source, skip_imports=False, result="RESULT", main_circuit="circuit"
    ):
        self.mutation = 0
        self.skip_imports = skip_imports
        self.result = result
        self.main_circuit = main_circuit

        self.qiskit_source = qiskit_source
        self.gates_to_import = set()

        if isinstance(qiskit_source, str):
            registers = metamorph.get_registers_used(qiskit_source)
            self.registers = registers
            self.instructions = metamorph.get_instructions(qiskit_source)
        else:
            self.registers = qiskit_source["registers"]
            self.instructions = qiskit_source["instructions"]
            self.shots = qiskit_source["shots"]

        for register in self.registers:
            if register["type"] == "QuantumRegister":
                self.qubits = register["size"]
                self.qubit_id = register["name"]
                break

        for register in self.registers:
            if register["type"] == "QuantumRegister" and register["name"].startswith(
                "qr_"
            ):
                self.unused_qubits = register["size"]
                self.unused_qubit_id = register["name"]
                break
        else:
            self.unused_qubits = None
            self.unused_qubit_id = None

        self.subcircuit = {
            "instructions": [
                el for el in self.instructions if el["circuit_id"] == "subcircuit"
            ],
            "start_index": 0,
        }

        for i, el in enumerate(self.instructions):
            if el["circuit_id"] == "subcircuit":
                self.subcircuit["start_index"] = i

        self.followup_config = {}

        # self.qubits = qubits
        # self.qubit_id = qubit_id
        self.gates_defined = {}
        self.followup_metadata = {}

    @staticmethod
    def find_independent_circuits(qiskit_source):
        registers = metamorph.get_registers_used(qiskit_source)
        instructions = metamorph.get_instructions(qiskit_source)

        def process(el):
            el["circuit_id"] = "qc"
            return el

        qc_1 = [process(el) for el in instructions if el["circuit_id"] == "qc_1"]
        qc_2 = [process(el) for el in instructions if el["circuit_id"] == "qc_2"]

        if len(qc_1) > 0 or len(qc_2) > 0:
            return [
                {
                    "circuit_name": "qc_1",
                    "registers": [el for el in registers if el["name"] == "qr_1"],
                    "instructions": qc_1,
                },
                {
                    "circuit_name": "qc_2",
                    "registers": [el for el in registers if el["name"] == "qr_2"],
                    "instructions": qc_2,
                },
            ]

    def _qubits_args(self, qubits_pos):
        res = []
        for i in qubits_pos:
            res.append(f"{i}")
        return ", ".join(res)

    def generic_gate(self, gate_name, qubit_pos, args):
        self.gates_to_import.add(gate_name)
        if gate_name == "C3XGate" and len(args) == 1:
            args = []
        if args is None or args == []:
            return f"Gates.{gate_name}( {self._qubits_args(qubit_pos)} )"

        if gate_name in [
            "RXGate",
            "RYGate",
            "RZGate",
            "PhaseGate",
            "U1Gate",
            "CPhaseGate",
            "CRXGate",
            "CRYGate",
            "CRZGate",
            "CU1Gate",
            "CUGate",
            "CU3Gate",
            "C3XGate",
        ]:
            return f'Gates.{gate_name}({", ".join(map(str, args))}, {self._qubits_args(qubit_pos)} )'
        return f'Gates.{gate_name}({", ".join(map(str, args))})( {self._qubits_args(qubit_pos)} )'

    def subcircuit_creator(self):
        out = ["\nsubcircuit = Program()"]

        subcircuit, defns = self.construct_circuit(
            self.subcircuit["instructions"], circuit_name="subcircuit"
        )

        out += subcircuit

        out.append(f"{self.main_circuit}.inst(subcircuit)")
        out.append(f"{self.main_circuit}.inst(subcircuit.dagger())\n")

        return out, defns

    def independent_circuit_creator(self):
        """s"""
        qc1_map, qc2_map = self.followup_config.get("independent_circuits")
        qc1_map = {v: int(k) for k, v in qc1_map.items()}
        qc2_map = {v: int(k) for k, v in qc2_map.items()}

        independent_circuits = PyQuilCircuit.find_independent_circuits(
            self.qiskit_source
        )
        count = 0

        ins_1 = independent_circuits[0]["instructions"]
        for i in ins_1:
            i["circuit_id"] = "qc"
            for j, qbit in enumerate(i["qbits"]):
                i["qbits"][j] = qc1_map[qbit]
        count += independent_circuits[0]["regs"][0]["size"]

        ins_2 = independent_circuits[1]["instructions"]
        for i in ins_2:
            i["circuit_id"] = "qc"
            for j, qbit in enumerate(i["qbits"]):
                i["qbits"][j] = qc2_map[qbit]
        count += independent_circuits[1]["regs"][0]["size"]

        self.qubit_id = "qr"
        self.instructions = ins_1 + ins_2
        self.qubits = count

    def get_change_opt_level(self):
        if not self.followup_config.get("opt_level"):
            return ""
        self.log(
            f"changing opt level to  {self.followup_config['opt_level']['new_level']}"
        )
        opt_level = self.followup_config["opt_level"]["new_level"]
        if opt_level == 0:
            return ""
        if opt_level == 1:
            return """ Pragma('INITIAL_REWIRING', ['"NAIVE"']) """
        if opt_level == 2:
            return """ Pragma('INITIAL_REWIRING', ['"PARTIAL"']) """
        if opt_level == 3:
            return """ Pragma('INITIAL_REWIRING', ['"GREEDY"']) """

        return ""

    def construct_circuit(self, instructions, circuit_name="circuit"):
        for i in reversed(instructions):
            if self.followup_config.get("qubit_mutation", 0) > self.mutation:
                if i["gate"].startswith("C"):
                    self.mutation += 1
                    self.log(f"changing this {i['gate']} {i['qbits']} to ")
                    i["qbits"] = next(random_derangement(i["qbits"]))
                    self.log(f"deranged form {i['qbits']}-")
            else:
                break

        gates_defined = {}

        res = []

        all_defns = []

        for i in instructions:
            gate_name = i["gate"]
            gate_params = i["params"]
            gate_qubits = i["qbits"]

            try:
                generate_instruction = getattr(self, gate_name)
            except AttributeError:
                generate_instruction = partial(self.generic_gate, gate_name)

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
                    else:
                        all_defns.append(gate_source)

            while len(gate_deps_to_add) > 0:
                gate_name = gate_deps_to_add.pop()

                if gates_defined.get(gate_name) is not True:
                    gates_defined[gate_name] = True
                    gate_source = getattr(GateDefinition, gate_name)
                    if isinstance(gate_source, tuple):
                        all_defns.append(gate_source[0])
                        gate_deps_to_add.extend(gate_source[1])
                    else:
                        all_defns.append(gate_source)

            res.append(f"{circuit_name}.inst({out})")

        return res, all_defns

    def log(self, text, color="yellow"):
        print(colored(f"transpiler:: {text}", color))

    def get_inject_parameters_symbols(self):
        params = self.followup_config.get("inject_params")
        if not params:
            return ""
        self.log("INJECTING params")
        symbols = [
            f"{name} = {self.main_circuit}.declare('{name}', 'REAL')" for name in params
        ]
        return "\n".join(symbols)

    def get_inject_parameters_end(self):
        params = self.followup_config.get("inject_params")
        if not params:
            return ""

        return f"""

params = {dumps(params, indent=4)}

for param, value in params.items():
    executable.write_memory(region_name=param, value=value)
        """

    def construct_all_circuits(self):
        if self.followup_config.get("independent_circuits", None):
            self.log("INDEPENDENT CIRCUITS")
            self.independent_circuit_creator()

        main_circuit, defns = self.construct_circuit(
            [el for el in self.instructions if el["circuit_id"] == "qc"],
            circuit_name=self.main_circuit,
        )

        if len(self.subcircuit["instructions"]) > 0:
            self.log("Generating SUB-CIRCUIT")
            subcircuit, sub_defns = self.subcircuit_creator()
            subcircuit_pos = (
                self.subcircuit["start_index"]
                - len(self.subcircuit["instructions"])
                + 1
            )
            main_circuit = (
                main_circuit[0:subcircuit_pos]
                + subcircuit
                + main_circuit[subcircuit_pos:]
                + self.get_measurement_gates()
            )
            dedup = list(set(defns + sub_defns))
        else:
            main_circuit = main_circuit + self.get_measurement_gates()
            dedup = defns

        cirq_instructions = "\n".join(main_circuit)

        return (
            f"""

{self.main_circuit} = Program({self.get_change_opt_level()})

{self.generate_qubit_registers()}

{self.get_inject_parameters_symbols()}

defns = get_custom_get_definitions({', '.join([f'"{el}"' for el in self.gates_to_import ])})

{self.main_circuit} += defns

{cirq_instructions}

""",
            dedup,
        )

    def get_changed_qubit_order(self):
        order = self.followup_config.get("qubit_order")
        if not order:
            return

    def get_measurement_gates(self):
        if self.followup_config.get("add_unitary", False):
            return []
        res = []
        res.append(self.get_unused_registers())
        order = self.followup_config.get("qubit_order")
        if order:
            self.log("CHANGE QUBIT order")
            for i, el in enumerate(order):
                res.append(
                    f"{self.main_circuit} += MEASURE({str(order[el])}, {self.qubit_id}[{str(el)}])"
                )
        else:
            for i in range(self.qubits):
                res.append(
                    f"{self.main_circuit} += MEASURE({str(i)}, {self.qubit_id}[{str(i)}])"
                )

        return res

    def prologue(self):
        nl = ",\n\t"
        if self.skip_imports:
            return ""
        return f"""
from pyquil import Program, get_qc
from pyquil.gates import MEASURE
from pyquil.quil import Pragma
from pyquil.parser import parse_program

from bloqs.ext.pyquil import Gates, get_custom_get_definitions
from bloqs.ext.pyquil.utils import get_qiskit_like_output
        """

    def epilogue(self, shots):
        if self.followup_config.get("add_unitary", False):
            return f"""
{ self.add_unitary() }
"""
        measurement_keys = []
        for i in range(self.qubits):
            measurement_keys.append(f"'cr{str(i)}'")

        return f"""
{ self.add_unitary() if self.followup_config.get('add_unitary', False) else ''}

{self.main_circuit}.wrap_in_numshots_loop({shots})

{self.backend_selection()}

executable = qc.compile({self.main_circuit}, protoquil=True)

{ self.get_inject_parameters_end()  }

{ self.qasm_roundtrip() if self.followup_config.get('qasm_roundtrip') else ''}

{'result' if self.result == 'RESULT' else self.result.lower() } = qc.run(executable).readout_data.get('ro')

counts = get_qiskit_like_output({'result' if self.result == 'RESULT' else self.result.lower()})
{self.result} = counts

{self.get_print_result()}
"""

    def get_print_result(self):
        if self.result == "RESULT":
            return f"""
if __name__ == '__main__':
    from utils import display_results
    display_results( {{"result": {self.result} }})
"""
        if self.result == "RESULT_2":
            return """
RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from utils import display_results
    for i in RESULT:
        display_results( {"result": i })

"""
        return ""

    def add_unitary(self):
        return f"""
from pyquil.simulation.tools import program_unitary
UNITARY = program_unitary({self.main_circuit}, {self.qubits})
"""

    def generate_named_qubit_registers(self):
        return f"{self.qubit_id} = [cirq.NamedQubit('q' + str(i)) for i in range({self.qubits})]"

    def generate_line_qubit_registers(self):
        return f"{self.qubit_id} = cirq.LineQubit.range({self.qubits})"

    def generate_grid_qubit_registers(self):
        return f"""
qubits_num = math.ceil({self.qubits} ** 1/2)
lattice = cirq.GridQubit.square(qubits_num + 1 if qubits_num == 1 else qubits_num)
{self.qubit_id} = [lattice[i] for i in range({self.qubits})]
        """

    def generate_qubit_registers(self):
        if self.followup_config.get("add_unitary"):
            return ""
        return (
            f'{self.qubit_id} = {self.main_circuit}.declare("ro", "BIT", {self.qubits})'
        )

    def backend_selection(self):
        selected_backend = self.followup_config.get("backend")

        if selected_backend is None:
            selected_backend = "Simulator"
        else:
            self.log("CHANGING backend")
            backends = ["Simulator", "DensityMatrixSimulator"]
            if selected_backend not in backends:
                raise ValueError(f"{selected_backend} is not a valid backend")
        seed = self.followup_config.get("seed", "np.random.RandomState()")
        return f'qc = get_qc("{"9q-square-qvm" if self.qubits <= 9 else f"{self.qubits}q-qvm" }", execution_timeout=60, compiler_timeout=60)'

    def null_ciruit_injector_prologue(self):
        return f"""
from cirq.testing import random_circuit
rand_cirq = random_circuit(qubits={self.qubits}, n_moments=10, op_density=0.75)
"""

    def null_circuit(self):
        return """
rand_cirq,
cirq.inverse(rand_cirq)
"""

    def get_transformations(self):
        transformation_order = self.followup_config.get("transformations")

        if transformation_order is None:
            return ""

        self.log("ADDING optimization pipeline")

        transformations_map = {
            "expand_composite": "optimized_circuit = cirq.expand_composite(circuit)",
            "defer_measurements": "optimized_circuit = cirq.defer_measurements(optimized_circuit)",
            "merge_k_qubit_unitaries": """optimized_circuit = cirq.merge_k_qubit_unitaries(
                optimized_circuit, k=2, rewriter=lambda op: op.with_tags("merged"), context=context)""",
            "eject_phased_paulis": "optimized_circuit = cirq.eject_phased_paulis(optimized_circuit, eject_parameterized=True)",
            "drop_negligible_operations": "optimized_circuit = cirq.drop_negligible_operations(optimized_circuit)",
            "drop_empty_moments": "optimized_circuit = cirq.drop_empty_moments(optimized_circuit)",
            "synchronize_terminal_measurements": "optimized_circuit = cirq.synchronize_terminal_measurements(optimized_circuit)",
            "eject_z": "optimized_circuit = cirq.eject_z(optimized_circuit, eject_parameterized=True)",
            "stratified_circuit": "optimized_circuit = cirq.stratified_circuit(optimized_circuit)",
        }

        transformations = []

        transformations.insert(0, "expand_composite")
        transformations.extend(transformation_order)

        self.followup_metadata["transformations_order"] = transformations

        optimizations = "\n\n    ".join(
            [transformations_map[key] for key in transformations]
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

    def get_unused_registers(self):
        if self.followup_config.get("unused_registers") is None:
            return ""
        if self.unused_qubits is None or self.unused_qubit_id is None:
            raise ValueError("unused_registers is set but no unused qubits found")
        self.log("ADDING unused registers")
        return f"""
{self.unused_qubit_id} = {self.main_circuit}.declare("{self.unused_qubit_id}", "BIT", {self.unused_qubits})
"""

    def get_shots(self):
        try:
            return self.shots
        except Exception:
            match = re.search(r"shots=([0-9]+)", self.qiskit_source)
            if not match:
                raise ValueError("no shots found")
            return match.group(1)

    def qasm_roundtrip(self):
        return f"""
quil_out = {self.main_circuit}.out()
{self.main_circuit} = parse_program(quil_out) # new circuit
"""

    def _get_equivalent(self, shots=None):
        circuit, defns = self.construct_all_circuits()

        cirq_source = self.prologue()

        cirq_source += self.get_transformations()

        cirq_source += "\n\n".join(defns)

        cirq_source += "\n\n"

        if self.followup_config.get("null_circuit"):
            cirq_source += self.null_ciruit_injector_prologue()

        cirq_source += circuit

        shots = self.get_shots()
        cirq_source += self.epilogue(shots)

        return cirq_source

    def get_follow_up(self, config):
        self.followup_config = config
        self.followup_metadata = {}

        if self.followup_config.get("independent_circuits", None):
            self.log("INDENTED CIRCUITS FOUND - SPLITTING")
            out = ""
            del config["independent_circuits"]
            shots = self.get_shots()

            independent_circuits = PyQuilCircuit.find_independent_circuits(
                self.qiskit_source
            )

            independent_circuits[0].update({"shots": shots})
            independent_circuits[1].update({"shots": shots})

            _, qc_1_out = PyQuilCircuit(
                independent_circuits[0],
                main_circuit="qc_1",
                result="RESULT_1",
            ).get_follow_up(config)
            _, qc_2_out = PyQuilCircuit(
                independent_circuits[1],
                skip_imports=True,
                result="RESULT_2",
                main_circuit="qc_2",
            ).get_follow_up(config)

            out += (
                qc_1_out
                + """

# Circuit 2

            """
                + qc_2_out
            )
            return _, out

        else:
            source = self._get_equivalent()
            metadata = self.followup_metadata

        self.followup_config = {}
        self.followup_metadata = {}
        return metadata, source

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

        cirq_ciruit = PyQuilCircuit(qubit_size)

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
    import sys

    # program_id = sys.argv[1]
    data = {}
    data = convert_morphq_metadata(
        "data/qmt_v53/programs/metadata/0a41cd2d8c8d4a2683ae7700d707d275.json"
    )

    with open(
        f"data/qmt_v53/programs/followup/0a41cd2d8c8d4a2683ae7700d707d275.py",
        encoding="utf-8",
    ) as f:
        content = fix_cx3(f.read())
        a, b = PyQuilCircuit(content).get_follow_up(data)
        print(b)
