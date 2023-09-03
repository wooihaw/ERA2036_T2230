# The Drone Problem is a hypothetical scenario often employed to demonstrate the efficacy of Particle Swarm Optimization (PSO) algorithms. 
# The problem can be framed as follows:
# In the context of drone design, the objective is to optimize the ratio of various materials, such as aluminum and plastic, to minimize aerodynamic drag and wobble during flight. 
# The drone's performance is evaluated using a fitness function that takes into account these factors.

# Importing necessary modules
import random

# Define the fitness function to evaluate the quality of a particle's position
def fitness_function(position):
    x, y = position
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

# Function to set up initial particles
def set_up_particles(n_particles):
    # Initialize particles with random positions and velocities
    particles = [{'position': [random.uniform(-10, 10), random.uniform(-10, 10)]} for _ in range(n_particles)]
    for particle in particles:
        # Assign random initial velocity
        particle['velocity'] = [random.uniform(-1, 1), random.uniform(-1, 1)]
        # Initialize best position and best score for each particle
        particle['best_position'] = particle['position'][:]
        particle['best_score'] = fitness_function(particle['best_position'])
    return particles

# Function to calculate the global best position and score among all particles
def calculate_fitness_of_particles(particles):
    global_best = min(particles, key=lambda x: x['best_score'])
    return global_best['best_position'][:], global_best['best_score']

# Function to update the positions and velocities of particles
def update_positions_of_particles(particles, global_best_position, global_best_score, w, c1, c2):
    for particle in particles:
        # Update velocity using inertia, cognitive, and social components
        for i in range(2):
            particle['velocity'][i] = w * particle['velocity'][i] + c1 * random.random() * (particle['best_position'][i] - particle['position'][i]) + c2 * random.random() * (global_best_position[i] - particle['position'][i])
        
        # Update position based on new velocity
        for i in range(2):
            particle['position'][i] += particle['velocity'][i]
        
        # Evaluate the fitness of the new position
        current_score = fitness_function(particle['position'])
        
        # Update personal best if current score is better
        if current_score < particle['best_score']:
            particle['best_position'] = particle['position'][:]
            particle['best_score'] = current_score
        
        # Update global best if current score is better
        if current_score < global_best_score:
            global_best_position = particle['position'][:]
            global_best_score = current_score
    return global_best_position, global_best_score

# Initialize parameters for PSO
n_particles = 50
n_iterations = 100
w = 0.2  # Inertia weight
c1 = 0.35  # Cognitive constant
c2 = 0.45  # Social constant

# Initialize particles
particles = set_up_particles(n_particles)

# Calculate initial global best position and score
global_best_position, global_best_score = calculate_fitness_of_particles(particles)

# Main loop for PSO algorithm
for iteration in range(n_iterations):
    global_best_position, global_best_score = update_positions_of_particles(particles, global_best_position, global_best_score, w, c1, c2)

# Output the final global best position and score
print(f"The global best position is {global_best_position}, with a score of {global_best_score}.")
