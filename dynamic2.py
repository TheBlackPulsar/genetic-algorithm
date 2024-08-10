import random
import numpy as np
from function_code import dynamic2

def create_population(bounds, population_size):
    population = []
    for _ in range(population_size):
        individual = [random.uniform(bounds[0][0], bounds[0][1]), random.uniform(bounds[1][0], bounds[1][1])]
        population.append(individual)
    return population

def evaluate_population(population, random_number):
    evaluations = []
    for individual in population:
        evaluations.append(dynamic2(individual, random_number))
    return evaluations

def select_parents(population, evaluations, num_parents):
    parents = np.array(population)[np.argsort(evaluations)[:num_parents]].tolist()
    return parents

def crossover(parent1, parent2):
    child = [
        (parent1[0] + parent2[0]) / 2,
        (parent1[1] + parent2[1]) / 2
    ]
    return child

def mutate(individual, bounds, mutation_rate):
    if random.random() < mutation_rate:
        individual[0] += random.uniform(-1, 1)
        individual[1] += random.uniform(-1, 1)
        individual[0] = max(bounds[0][0], min(bounds[0][1], individual[0]))
        individual[1] = max(bounds[1][0], min(bounds[1][1], individual[1]))
    return individual

def genetic_algorithm(bounds, population_size, generations, mutation_rate, random_number):
    population = create_population(bounds, population_size)
    best_individual = None
    best_evaluation = float('inf')
    
    for generation in range(generations):
        evaluations = evaluate_population(population, random_number)
        
        for i, evaluation in enumerate(evaluations):
            if evaluation < best_evaluation:
                best_individual = population[i]
                best_evaluation = evaluation
        
        parents = select_parents(population, evaluations, population_size // 2)
        next_population = parents[:]
        
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, bounds, mutation_rate)
            next_population.append(child)
        
        population = next_population
        # (Optional) Print generations
        #print(f"Generation {generation}, Best individual: {best_individual}, Value: {best_evaluation}")
    
    return best_individual, best_evaluation

if __name__ == "__main__":
    # Set a random number atleast 6 digits long
    random_number = 12128551

    # Define the bounds of the search space
    bounds = [(-100, 100), (-100, 100)]
    # Define the population size
    population_size = 50
    # Define the number of generations
    generations = 100
    # Define the mutation rate
    mutation_rate = 0.1
    
    # Perform genetic algorithm optimization
    best_candidate, best_value = genetic_algorithm(bounds, population_size, generations, mutation_rate, random_number)
    print(f"Best candidate: {best_candidate}, Best value: {best_value}")