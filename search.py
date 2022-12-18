import random
from datetime import datetime
import re
import os
from pathlib import Path
from json import loads, dumps

from typing import List
from pygments import highlight
from pygments.lexers.data import JsonLexer
from pygments.formatters.terminal import TerminalFormatter

from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.core.problem import PermutationProblem
from jmetal.core.solution import PermutationSolution
from jmetal.operator import BinaryTournamentSelection
from jmetal.operator.crossover import PMXCrossover
from jmetal.operator.mutation import (
    PermutationSwapMutation,
)
from jmetal.util.observer import ProgressBarObserver
from jmetal.util.termination_criterion import StoppingByEvaluations
from termcolor import colored

from executor import detect_divergence, execute_single_py_program
from transpiler import CirqCircuit


def get_circuit(program_id: str):
    for i in range(2):
        try:
            with open(
                f"data/qmt_v5{i+2}/programs/source/{program_id}.py", encoding="utf-8"
            ) as f:
                content = f.read()
                instrumented_qiskit_source = re.sub(
                    r"qc.append\(C3XGate\(.*\)", "\n", content
                )
                return CirqCircuit(instrumented_qiskit_source)
        except Exception:
            continue


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


class OptimizationProblem(PermutationProblem):
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
        metadata, source = self.circuit.get_follow_up(
            {"transformations": perm_from_encoding(solution.variables)}
        )
        # print(metadata)
        result, _ = execute_single_py_program(source)

        solution.divergence_calculated = detect_divergence(
            {"res_A": result, "res_B": self.non_optimized_result}
        )

        # Maximize
        solution.objectives[0] = -1.0 * solution.divergence_calculated["statistic"]

        return result

    def toJSON(self):
        return "OptimizationSearch"

    def get_name(self):
        return "QSearch"


def run_algorithm(program_id: str):
    print(colored(f"STARTING {program_id}", "green"))
    problem = OptimizationProblem(OPTS, get_circuit(program_id))

    max_evaluations = 4000
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
    found_perm = perm_from_encoding(result.variables)
    
    given_perm = ["expand_composite"] + found_perm

    metadata = get_divergence_from_stored_metadata(program_id, given_perm)
    data = algorithm.get_observable_data()
    solution_stats = data['SOLUTIONS'].divergence_calculated
    del data['PROBLEM']
    out = {
        "program_id": program_id,
        "timestamp": str(datetime.now()),
        "jmetal": {
            "result": str(result),
            "found_perm": found_perm,
            "algo_name": algorithm.get_name(),
            "total_compute_time": algorithm.total_computing_time,
            "data": str(data),
            "solution_stats": solution_stats
        },
        "stored_perm_info": metadata,
    }
    return out


def run_for_files(lb):
    dir_path = "data/qmt-cirq-permutations/exec-metadata/"
    files = os.listdir(dir_path)
    files = list(map(lambda x: x.split(".")[0], files))
    output_path = "data/jmetal-search-data/"
    # files = files[lb:ub]

    Path(output_path).mkdir(parents=True, exist_ok=True)
    prog_id = files[lb]

    with open(f"{output_path}{prog_id}.json", "a", encoding="utf-8") as f:
        data = run_algorithm(prog_id)
        f.write('\n')
        f.write(dumps(data, indent=4))
        print(colored(f"DONE {prog_id}", "red"))


if __name__ == "__main__":
    import sys

    args = sys.argv[1]
    # lb, ub = args.split(":")
    run_for_files(int(args))

    # found_perm = result['found_perm']
    # print(colored("RESULT FROM SEARCH:", color="blue", attrs=["bold"]))
    # print(colored(f"Perm: {found_perm}", color="green"))
    # print(colored("Store Result:", color="blue", attrs=["bold"]))

    # json_str = dumps(result['stored_perm_info'], indent=4, sort_keys=True)
    # print(highlight(json_str, JsonLexer(), TerminalFormatter()))
