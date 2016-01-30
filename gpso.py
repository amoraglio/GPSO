#
# Geometric Particle Swarm Optimisation
#

import random, copy

### POPULATION LEVEL ###

def gpso_search():
    population = create_pop()
    personal_best_population = copy.copy(population)
    global_best, global_best_fitness = get_best_pop(personal_best_population)
    print global_best_fitness
    for _ in range(NUM_GENERATIONS):
        population = convex_combination_pop(population, personal_best_population, [global_best]*POPULATION_SIZE)
        population = mutation_pop(population)
        personal_best_population = selection_pop(personal_best_population, population)
        global_best, global_best_fitness = get_best_pop(personal_best_population)
        print global_best_fitness
    return (global_best, global_best_fitness) 

### INDIVIDUAL LEVEL ###

def create_pop():
    return [ create_ind() for _ in range(POPULATION_SIZE) ]

def get_best_pop(population):
    best_ind = max(population, key=evaluate_ind)
    return best_ind, evaluate_ind(best_ind)

def convex_combination_pop(pop1, pop2, pop3):
    return [ convex_combination_ind([ind1, ind2, ind3]) for (ind1, ind2, ind3) in zip(pop1, pop2, pop3) ]

def mutation_pop(population):
    return [ mutation_ind(individual) for individual in population ]

def selection_pop(pop1, pop2):
    return [ max(ind1, ind2, key=evaluate_ind) for (ind1, ind2) in zip(pop1, pop2) ]

### REPRESENTATION LEVEL ###

def create_ind():
    return [ random.randint(0, 1) for _ in range(INDIVIDUAL_SIZE) ]

def evaluate_ind(individual): #one_max
    return sum(individual)

def convex_combination_ind(mating_pool):
    transposed_mating_pool=zip(*mating_pool)
    return map(random.choice, transposed_mating_pool)

def mutation_ind(individual):
    return [ 1-bit if random.random()<1.0/INDIVIDUAL_SIZE else bit for bit in individual ]

### EXPERIMENTS ###

NUM_GENERATIONS = 100
POPULATION_SIZE = 25
INDIVIDUAL_SIZE = 100

print gpso_search()
