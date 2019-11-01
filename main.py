#!/usr/bin/python2

from population import Population

ENCRYPTED= "mvazmjlgwzlfdqgmjltikshkrblapwegmshxlrniuychdmzwwfv"

TOTAL_POP=500
TOTAL_GEN=100
CROSSOVER_RATE=.9
MUTATION_RATE=0.1

if __name__=="__main__":
    population=Population(500,26,ENCRYPTED)
    population.calc_fitness()
"""    while population.is_finished()==False:
        population.natural_selection()
        population.generate()
        population.calc_fitness()
        population.evaluate()

        if population.is_finished()==True:
            break

        print population.get_generations()
        print population.get_average_fitness()
        print population.get_best()
        #print population.all_phrases()
"""
