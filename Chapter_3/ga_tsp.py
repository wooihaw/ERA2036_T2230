# The Traveling Salesman Problem (TSP) is a classic optimization problem in the field of computer science and operations research. 
# It serves as a benchmark problem for various optimization algorithms, including Genetic Algorithms (GA) and Particle Swarm Optimization (PSO).
# The problem can be formally stated as follows:
# Given a list of cities and the distances between each pair of cities, the task is to find the shortest possible route that visits each city exactly once and returns to the original city.

# Importing necessary modules
import random
import math
import matplotlib.pyplot as plt

# Define the function to calculate distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the function to evaluate the fitness of a single route
def fitness(route, cities):
    return sum(calculate_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route) - 1))

# Define the function to perform ordered crossover
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    pointer = 0
    for item in parent2:
        if item not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = item
    return child

# Define the function to perform swap mutation
def mutate(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]

# Define the main function to run Genetic Algorithm
def genetic_algorithm_no_numpy(cities, pop_size=100, generations=500, mutation_rate=0.2):
    # Initialize population
    population = [random.sample(range(len(cities)), len(cities)) for _ in range(pop_size)]
    
    for generation in range(generations):
        # Evaluate fitness
        fitnesses = [fitness(route, cities) for route in population]
        fittest = min(fitnesses)
        
        # Selection
        prob_select = [fittest / f for f in fitnesses]
        total_prob = sum(prob_select)
        prob_select = [p/total_prob for p in prob_select]
        selected_indices = random.choices(range(len(population)), weights=prob_select, k=pop_size//2)
        selected_parents = [population[i] for i in selected_indices]
        
        # Crossover and mutation
        children = []
        for i in range(0, len(selected_parents), 2):
            child = crossover(selected_parents[i], selected_parents[i+1])
            if random.random() < mutation_rate:
                mutate(child)
            children.append(child)
            
        # Next generation
        population = selected_parents + children

    # Return the best route
    best_route = min(population, key=lambda route: fitness(route, cities))
    return best_route, fitness(best_route, cities)

# Sample cities as a list of (x,y) coordinates
cities = [(0,0), (1,5), (5,2), (8,4), (6, 5), (4,7), (3, 3), (5, 4)]

# Run the Genetic Algorithm without numpy and get the result
best_route_no_numpy, best_distance_no_numpy = genetic_algorithm_no_numpy(cities)

# Plotting the results
x_coords = [cities[i][0] for i in best_route_no_numpy]
y_coords = [cities[i][1] for i in best_route_no_numpy]

# Closing the loop in the plot
x_coords.append(x_coords[0])
y_coords.append(y_coords[0])

plt.figure(figsize=(10, 6))
plt.scatter(x_coords, y_coords, c='blue', label='Cities')
plt.plot(x_coords, y_coords, c='red', label=f'Best Route (Distance = {best_distance_no_numpy:.2f})')
plt.title('Optimized Traveling Salesman Route')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.show()

print(best_route_no_numpy, best_distance_no_numpy)
