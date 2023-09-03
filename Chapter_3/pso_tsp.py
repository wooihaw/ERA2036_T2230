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

# Refined PSO function with further corrections
def pso_refined(cities, num_particles=30, num_iterations=500, w=0.5, c1=1.5, c2=1.5):
    # Initialize particles and velocities
    particles = [random.sample(range(len(cities)), len(cities)) for _ in range(num_particles)]
    
    # Initialize personal best and global best
    pbest_positions = particles.copy()
    pbest_scores = [fitness(route, cities) for route in particles]
    gbest_position = min(pbest_positions, key=lambda x: fitness(x, cities))
    gbest_score = fitness(gbest_position, cities)
    
    for iteration in range(num_iterations):
        for i in range(num_particles):
            # Update particle using a variant of PSO designed for combinatorial problems
            new_particle = particles[i][:]
            if random.random() < w:
                # Swap two cities in the route
                idx1, idx2 = random.sample(range(len(cities)), 2)
                new_particle[idx1], new_particle[idx2] = new_particle[idx2], new_particle[idx1]
            
            if random.random() < c1:
                # Use personal best to influence the route
                idx1, idx2 = random.sample(range(len(cities)), 2)
                a, b = new_particle.index(pbest_positions[i][idx1]), new_particle.index(pbest_positions[i][idx2])
                new_particle[a], new_particle[b] = new_particle[b], new_particle[a]
            
            if random.random() < c2:
                # Use global best to influence the route
                idx1, idx2 = random.sample(range(len(cities)), 2)
                a, b = new_particle.index(gbest_position[idx1]), new_particle.index(gbest_position[idx2])
                new_particle[a], new_particle[b] = new_particle[b], new_particle[a]
            
            # Update personal best
            current_score = fitness(new_particle, cities)
            if current_score < pbest_scores[i]:
                pbest_positions[i] = new_particle
                pbest_scores[i] = current_score
                
                # Update global best
                if current_score < gbest_score:
                    gbest_position = new_particle
                    gbest_score = current_score
            
            particles[i] = new_particle
    
    return gbest_position, gbest_score

# Sample cities as a list of (x,y) coordinates
cities = [(0,0), (1,5), (5,2), (8,4), (6, 5), (4,7), (3, 3), (5, 4)]

# Run the refined PSO algorithm and get the result
best_route_pso_refined, best_distance_pso_refined = pso_refined(cities, num_particles=50)

# Plotting the refined results
x_coords_pso_refined = [cities[i][0] for i in best_route_pso_refined]
y_coords_pso_refined = [cities[i][1] for i in best_route_pso_refined]

# Closing the loop in the plot
x_coords_pso_refined.append(x_coords_pso_refined[0])
y_coords_pso_refined.append(y_coords_pso_refined[0])

plt.figure(figsize=(10, 6))
plt.scatter(x_coords_pso_refined, y_coords_pso_refined, c='blue', label='Cities')
plt.plot(x_coords_pso_refined, y_coords_pso_refined, c='orange', label=f'Best Route (Distance = {best_distance_pso_refined:.2f})')
plt.title('Optimized Traveling Salesman Route using Refined PSO')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.show()

best_route_pso_refined, best_distance_pso_refined
