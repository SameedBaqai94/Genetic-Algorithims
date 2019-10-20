#!/usr/bin/python2

from __future__ import division
import random
import math

def new_char():
    c=int(random.uniform(63,122))
    if c==63: c=32
    if c==64: c=46

    return str(unichr(c))

class Indivisual_DNA:

    def __init__(self,num):
        self.genes=[]
        self.fitness=0

        for i in range(num):
            self.genes.append(new_char())
    
    def get_pharse(self):
        return "".join(self.genes)

    def calc_fitness(self,target):
        score=0
        for k in range(len(self.genes)):
            if self.genes[k]==target[k]:
                score=score+1
        
        self.fitness=score/len(target)

    def crossover(self,partner):
        child=Indivisual_DNA(len(self.genes))
        mid_point=int(random.uniform(0,len(self.genes)))

        for i in range(len(self.genes)):
            if i>mid_point:
                child.genes[i]=self.genes[i]
            else:
                child.genes[i]=partner.genes[i]
        return child
    
    def mutate(self,mutate_rate):
        for i in range(len(self.genes)):
            if random.uniform(0,1)<mutate_rate:
                self.genes[i]=new_char()

        