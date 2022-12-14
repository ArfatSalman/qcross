import random
import re
from json import loads, dumps
from typing import List
from pygments import highlight
from pygments.lexers.data import JsonLexer
from pygments.formatters.terminal import TerminalFormatter

from jmetal.algorithm.multiobjective import NSGAII
from jmetal.algorithm.singleobjective.evolution_strategy import EvolutionStrategy
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.core.problem import BinaryProblem, PermutationProblem
from jmetal.core.solution import BinarySolution, PermutationSolution
from jmetal.operator import BestSolutionSelection, BinaryTournamentSelection
from jmetal.operator.crossover import PMXCrossover, SBXCrossover, SPXCrossover
from jmetal.operator.mutation import (
    BitFlipMutation,
    PermutationSwapMutation,
    PolynomialMutation,
)
from jmetal.util.observer import ProgressBarObserver
from jmetal.util.termination_criterion import StoppingByEvaluations
from termcolor import colored

from executor import detect_divergence, execute_single_py_program
from transpiler import CirqCircuit

cs = 0


def get_circuit(program_id: str):
    with open(f"data/qmt_v52/programs/source/{program_id}.py", encoding="utf-8") as f:
        content = f.read()
        instrumented_qiskit_source = re.sub(
            r"qc.append\(C3XGate\(.*\)", "\n", content
        )
        return CirqCircuit(instrumented_qiskit_source)


def get_divergence_from_stored_metadata(program_id: str, given_perm):
    with open(
        f"data/qmt-cirq-permutations/exec-metadata/{program_id}.json", encoding="utf-8"
    ) as f:
        content = loads(f.read())
        subset_metadata = content["subset_metadata"]
        for i, metadata in enumerate(subset_metadata):
            if metadata[str(i)]["perm"] == given_perm:
                return metadata


OPTS = [
    "defer_measurements",
    "merge_k_qubit_unitaries",
    "drop_empty_moments",
    "eject_z",
    "eject_phased_paulis",
    "drop_negligible_operations",
    "stratified_circuit",
    "synchronize_terminal_measurements",
]


def perm_from_encoding(encoding):
    return [OPTS[i] for i in encoding]


class Problem(PermutationProblem):
    def __init__(self, optimizations: List[str], circuit: CirqCircuit):
        super().__init__()

        # Evaluate Once
        self.circuit = circuit
        metadata, source = circuit.get_follow_up({"add_unitary": False})
        # print(metadata)
        result, _ = execute_single_py_program(source)
        self.non_optimized_result = result

        self.optimizations = optimizations

        # jMetal specific-conditions
        self.obj_directions = [self.MAXIMIZE]
        self.number_of_variables: int = len(optimizations)
        self.number_of_objectives: int = 1
        self.number_of_constraints: int = 0

    def create_solution(self) -> PermutationSolution:
        global cs
        cs += 1
        # print("create_solution ", cs)

        new_solution = PermutationSolution(
            number_of_variables=self.number_of_variables,
            number_of_objectives=self.number_of_objectives,
        )
        new_solution.variables = random.sample(
            range(self.number_of_variables), k=self.number_of_variables
        )

        return new_solution

    def evaluate(self, solution: PermutationSolution) -> PermutationSolution:
        # print("evaluate called with ", solution.objectives)
        # Evaluate the current permutation
        # print(self._perm_from_encoding(solution.variables))
        metadata, source = self.circuit.get_follow_up(
            {"transformations": perm_from_encoding(solution.variables)}
        )
        # print(metadata)
        result, _ = execute_single_py_program(source)

        self.divergence_calculated = detect_divergence(
            {"res_A": result, "res_B": self.non_optimized_result}
        )
        # print(divergence["statistic"])

        solution.objectives[0] = -1.0 * self.divergence_calculated["statistic"]

        return result

    def get_name(self):
        return "QSearch"


if __name__ == "__main__":
    program_id = "3b5ad11802e74ddb839ec4bf2f2ad189"
    print(colored(f"Working with Program {program_id}", color="red", attrs=["bold"]))
    problem = Problem(OPTS, get_circuit(program_id))

    max_evaluations = 500
    progress_bar = ProgressBarObserver(max=max_evaluations)

    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=PermutationSwapMutation(probability=1.0 / problem.number_of_variables),
        crossover=PMXCrossover(probability=0.8),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )
    algorithm.observable.register(progress_bar)
    algorithm.run()
    result = algorithm.get_result()
    print(result)
    found_perm = perm_from_encoding(result.variables)
    print(colored("RESULT FROM SEARCH:", color="blue", attrs=["bold"]))
    print(colored(f"Perm: {found_perm}", color="green"))
    print(colored("RESULT FROM SEARCH:", color="blue", attrs=["bold"]))

    given_perm = ["expand_composite"] + found_perm

    metadata = get_divergence_from_stored_metadata(program_id, given_perm)
    json_str = dumps(metadata, indent=4, sort_keys=True)
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))
