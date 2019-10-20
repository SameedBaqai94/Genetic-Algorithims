#!/usr/bin/python2

from population import Population

if __name__=="__main__":
    population=Population("To be or not to be.",0.01,300)
    while population.is_finished()==False:
        population.calc_fitness()
        population.natural_selection()
        population.generate()
        population.evaluate()

        if population.is_finished():
            break
        print population.get_generations()
        print population.get_average_fitness()
        print population.get_best()
        #print population.all_phrases()