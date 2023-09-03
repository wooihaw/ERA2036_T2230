# The Knapsack Problem is a well-known combinatorial optimization problem commonly used to evaluate the performance of optimization algorithms, including Genetic Algorithms (GA). 
# The problem can be succinctly described as follows:
# Given a set of items, each with a weight and a value, determine the maximum value that can be obtained in a knapsack of fixed carrying capacity.

# Importing necessary modules
import random

# Weights and values of items
weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
values = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
items = ['abacus', 'box', 'candle', 'doll', 'eggs', 'fan', 'guitar', 'hat', 'ice cream', 'jacket']
W = 20  # Maximum weight capacity

# Fitness function to evaluate a solution
def fitness(solution):
    total_weight = total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
    return total_value if total_weight <= W else 0

# Initialization of population
def initialize_population(pop_size, length):
    population = []
    while len(population) < pop_size:
        individual = [random.randint(0, 1) for _ in range(length)]
        if fitness(individual) > 0 and individual not in population:
            population.append(individual)
    return population

# Selection of parents using roulette wheel
def roulette_wheel_selection(population):
    total_fitness = sum(fitness(individual) for individual in population)
    random_selection = random.uniform(0, total_fitness)
    cumulative_fitness = 0
    for individual in population:
        cumulative_fitness += fitness(individual)
        if cumulative_fitness >= random_selection:
            return individual

# Crossover to create offspring
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation to introduce variability
def mutate(child):
    mutation_point = random.randint(0, len(child) - 1)
    child[mutation_point] = 1 - child[mutation_point]

# Genetic algorithm to solve the School Bag Problem
def genetic_algorithm(pop_size, generations):
    population = initialize_population(pop_size, len(weights))
    best_solution = max(population, key=fitness)
    for _ in range(generations):
        new_population = [best_solution]  # Elitism
        while len(new_population) < pop_size:
            parent1 = roulette_wheel_selection(population)
            parent2 = roulette_wheel_selection(population)
            while parent1 == parent2:
                parent2 = roulette_wheel_selection(population)
            child1, child2 = crossover(parent1, parent2)
            if random.random() < 0.1:  # Mutation probability
                mutate(child1)
            if random.random() < 0.1:  # Mutation probability
                mutate(child2)
            if fitness(child1) > 0:
                new_population.append(child1)
            if fitness(child2) > 0:
                new_population.append(child2)
        population = sorted(new_population, key=fitness, reverse=True)[:pop_size]
        best_solution = population[0]
    return best_solution

# Running the genetic algorithm
best_solution = genetic_algorithm(pop_size=10, generations=20)
print("Best solution:", best_solution)
print("Total value:", fitness(best_solution))
print(f"Items included: {[items[i] for i, j in enumerate(best_solution) if j == 1]}")
