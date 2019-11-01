#!/usr/bin/python2

from __future__ import division
from indivisual_dna import Indivisual_DNA
import random

class Population:

    def __init__(self,pop_len,dna_len,text):


        self.population=[]
        self.pop_fitness=0
        self.pop_len=pop_len
        self.dna_len=dna_len
        self.text=text

        for i in range(pop_len):
            self.population.insert(i,Indivisual_DNA(dna_len))

    def calc_fitness(self):
        avg_fit=0
        for i in range(len(self.population)):
            self.population[i].fitness=self.population[i].fitnesses(str(self.population[i].genes),self.text)
            avg_fit=avg_fit+self.population[i].fitness
            print self.population[i].genes, " ", self.population[i].fitness
        self.pop_fitness=avg_fit/self.pop_len

