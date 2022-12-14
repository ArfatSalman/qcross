import random

from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.algorithm.singleobjective.evolution_strategy import EvolutionStrategy
from jmetal.algorithm.multiobjective import NSGAII
from jmetal.core.problem import PermutationProblem, BinaryProblem
from jmetal.core.solution import PermutationSolution, BinarySolution
from jmetal.operator import BestSolutionSelection, BinaryTournamentSelection
from jmetal.operator.crossover import PMXCrossover, SBXCrossover, SPXCrossover
from jmetal.operator.mutation import (
    PermutationSwapMutation,
    PolynomialMutation,
    BitFlipMutation,
)
from jmetal.util.termination_criterion import StoppingByEvaluations

from transpiler import CirqCircuit

c = 0
class SubsetSum(BinaryProblem):
    def __init__(self, C: int, W: list):
        super(SubsetSum, self).__init__()
        self.C = C
        self.W = W

        self.number_of_bits = len(self.W)
        self.number_of_objectives = 1
        self.number_of_variables = 1
        self.number_of_constraints = 0

        self.obj_directions = [self.MAXIMIZE]
        self.obj_labels = ["Sum"]

    def evaluate(self, solution: BinarySolution) -> BinarySolution:
        total_sum = 0.0

        for index, bits in enumerate(solution.variables[0]):
            if bits:
                total_sum += self.W[index]

        if total_sum > self.C:
            total_sum = self.C - total_sum * 0.1

            if total_sum < 0.0:
                total_sum = 0.0

        solution.objectives[0] = -1.0 * total_sum

        return solution

    def create_solution(self) -> BinarySolution:
        new_solution = BinarySolution(
            number_of_variables=self.number_of_variables,
            number_of_objectives=self.number_of_objectives,
        )
        new_solution.variables[0] = [
            True if random.randint(0, 1) == 0 else False
            for _ in range(self.number_of_bits)
        ]
        global c
        c+=1
        print('craete sol', c)

        return new_solution

    def get_name(self) -> str:
        return "Subset Sum"


problem = SubsetSum(50, [3, 34, 4, 12, 5, 2])

algorithm = GeneticAlgorithm(
    problem=problem,
    population_size=100,
    offspring_population_size=1,
    mutation=BitFlipMutation(probability=0.1),
    crossover=SPXCrossover(probability=0.8),
    selection=BinaryTournamentSelection(),
    termination_criterion=StoppingByEvaluations(max_evaluations=250),
)

algorithm.run()
subset = algorithm.get_result()
print(subset)

# class Problem(PermutationProblem):
#     def __init__(self):
#         super().__init__()

#         # number of optimizations
#         self.number_of_variables: int = 8
#         self.number_of_objectives: int = 1
#         self.number_of_constraints: int = 0

#     def create_solution(self) -> PermutationSolution:
#         print("create solution called")
#         new_solution = PermutationSolution(
#             number_of_variables=self.number_of_variables,
#             number_of_objectives=self.number_of_objectives,
#         )
#         new_solution.variables = random.sample(range(0, 9), 8)
#         return new_solution

#     def evaluate(self, solution):
#         print("evaluate called with ", solution)
#         result = PermutationSolution(
#             self.number_of_variables,
#             self.number_of_objectives,
#             self.number_of_constraints,
#         )
#         return result
#         # return sum()

#     def get_name(self):
#         return "QSearch"


# problem = Problem()

# algorithm = GeneticAlgorithm(
#     problem,
#     population_size=10,
#     offspring_population_size=10,
#     mutation=PermutationSwapMutation(probability=1),
#     crossover=PMXCrossover(probability=1.0),
#     selection=BestSolutionSelection(),
#     termination_criterion=StoppingByEvaluations(max_evaluations=5000),
# )

# algorithm.run()
