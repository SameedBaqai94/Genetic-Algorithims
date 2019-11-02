#!/usr/bin/python2
from indivisual_dna import Indivisual_DNA
import copy
import random

ENCRYPTED= ("xbwdesmhihslwhkktefvktkktcwfpiibihwmosfilojvooegvefwno"+
           "ichsuuspsureifakbnlalzsrsroiejwzgfpjczldokrceoahzshpbdw"+
           "pcjstacgbarfwifwohylckafckzwwomlalghrtafchfetcgfpfrgxc"+
           "lwzocdctmjebx")

TOTAL_POP=None
TOTAL_GEN=None
CROSSOVER_RATE=None
MUTATION_RATE=None
CHROMOSONE_LEN=None

class Selection:
    
    def __init__(self,pop,chromosone_len):
        self.pop=pop
        self.chromosone_len=chromosone_len

    def tournament(self,selected_parents,i):
        for j in range(i):
            selected_parents.append(self.pop.population[int(random.random()*len(self.pop.population)-1)])
            return min(selected_parents)

class Crossover:

    def __init__(self,parents,chromosone_len):
        self.parents=parents
        self.chromosone_len=chromosone_len

    def one_point(self):
        children=[]
        for i in range(2):
            children.insert(i,Indivisual_DNA(CHROMOSONE_LEN))
        split=int(random.random()*CHROMOSONE_LEN-1)
        for j in range(split,CHROMOSONE_LEN):
            swap=children[0].genes[j]
            children[0].genes[j]=children[1].genes[j]
            children[1].genes[j]=swap
        return children

class Mutation:

    def __init__(self,chromosone,chromosone_len):
        self.chromosone=chromosone
        self.chromosone_len=chromosone_len
    
    def inversion(self):
        a=int(random.random()*len(self.chromosone.genes))-1
        b=int(random.random()*len(self.chromosone.genes))-1

        strt=min(a,b)
        end=max(a,b)

        stack=[]
        for i in range(end-strt):
            stack.append(self.chromosone.genes[strt+i])
        for j in range(end-strt):
            self.chromosone.genes[strt+j]=stack.pop()


class Population:

    def __init__(self,pop_len,dna_len,text,cross_rate,mutation_rate):


        self.population=[]
        self.pop_fitness=0
        self.pop_len=pop_len
        self.dna_len=dna_len
        self.text=text
        self.parents=[]
        self.cross_rate=cross_rate
        self.mutation_rate=mutation_rate

        for i in range(pop_len):
            self.population.insert(i,Indivisual_DNA(dna_len))

    def calc_fitness(self):
        avg_fit=0
        for i in range(len(self.population)):
            self.population[i].fitness=self.population[i].fitnesses(str(self.population[i].genes),self.text)
            avg_fit=avg_fit+self.population[i].fitness
        
        self.pop_fitness=avg_fit/self.pop_len
    
    def return_parents(self):
        return self.parents

    def selection(self,pop,pop_2,chromosone_len):
        
        selection=Selection(pop,chromosone_len)

        while len(pop_2.population) < TOTAL_POP:
            self.parents.append(selection.tournament(self.parents,5))
            self.parents.append(selection.tournament(self.parents,5))
            crossover=Crossover(self.parents,26)

            if random.random() < self.cross_rate:
                children=crossover.one_point()
                for child in children:
                    pop_2.population.append(child)

            if len(pop_2.population) >=2 and random.random() < self.mutation_rate:
                mutation=Mutation(pop_2.population[int(random.random()+len(pop_2.population)-1)],CHROMOSONE_LEN)
                mutation.inversion()
        return pop_2.population

if __name__=="__main__":
    
    TOTAL_POP=int(input("Population Size: "))
    TOTAL_GEN=int(input("Generations Size: "))
    CROSSOVER_RATE=float(input("Crossover Rate: "))
    MUTATION_RATE=float(input("Mutation Rate: "))
    CHROMOSONE_LEN=int(input("Chromosones Size: "))

    population=Population(TOTAL_POP,CHROMOSONE_LEN,ENCRYPTED,CROSSOVER_RATE,MUTATION_RATE)
    population_2=None
    old_pop_min,new_pop_min=None,None
    record=None

    for i in range(TOTAL_GEN):
        population_2=Population(0,0,ENCRYPTED,CROSSOVER_RATE,MUTATION_RATE)
        population.calc_fitness()
        population_2.population=population_2.selection(population,population_2,CHROMOSONE_LEN)
        population_2.pop_len=len(population_2.population)
        population_2.calc_fitness()
        old_pop_min=min(population.population)
        new_pop_min=min(population_2.population)
        if new_pop_min.fitness < old_pop_min.fitness:
            old_pop_min=copy.deepcopy(new_pop_min)
        else:
            a=max(population_2.population)
            j=population_2.population.index(a)
            population_2.population[j]=copy.deepcopy(old_pop_min)
        print old_pop_min.fitness
        old_pop_min=new_pop_min
        record=[old_pop_min.genes,old_pop_min.fitness]

    print ""
    print "Choromsone len: 26"
    print "".join(record[0]).strip(',')
    print "Fitness:", record[1]

