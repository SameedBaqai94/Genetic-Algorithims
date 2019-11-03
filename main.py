#!/usr/bin/python2
from __future__ import division
import math
import re
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
CHROMOSONE_LEN=26


def new_char():
    c=int(random.random() * 26+97)

    return str(unichr(c))
def split(word):
    return[ord(char) for char in word]

def decrypt(k,c):
    cipher=c.lower()
    cipher=re.sub(r"[^a-z]","",cipher)
    cipher=re.sub(r"\\s","",cipher)

    ke=k.lower()
    ke=re.sub(r"[^a-z]","",ke)
    ke=re.sub(r"\\s","",ke)

    key=list(ke.encode())

    for k in range(len(key)):
        key[k]=ord(key[k])-97
    
    plain=""
    key_ptr=0
    for i in range(len(cipher)):
        if len(key) > 0:
            while key[key_ptr] < 0 or key[key_ptr] > CHROMOSONE_LEN-1:
                key_ptr=(key_ptr+1)%len(key)
            #key_char=key[key_ptr]
            key_ptr=(key_ptr+1)%len(key)
        plain+=chr(((ord(cipher[i])-97+CHROMOSONE_LEN-key[key_ptr%len(key)])%CHROMOSONE_LEN)+97)      
    return plain

class Indivisual_DNA:

    def __init__(self,num):
        self.genes=[]
        self.fitness=0

        for i in range(num):
            self.genes.append(new_char())
        

    def fitnesses(self,k, c):

        expectedFrequencies =[]
        expectedFrequencies.append(0.085) #Expected frequency of a
        expectedFrequencies.append(0.016) #Expected frequency of b
        expectedFrequencies.append(0.0316) #Expected frequency of c
        expectedFrequencies.append(0.0387) #Expected frequency of d
        expectedFrequencies.append(0.121) #Expected frequency of e
        expectedFrequencies.append(0.0218) #Expected frequency of f
        expectedFrequencies.append(0.0209) #Expected frequency of g
        expectedFrequencies.append(0.0496) #Expected frequency of h
        expectedFrequencies.append(0.0733) #Expected frequency of i
        expectedFrequencies.append(0.0022) #Expected frequency of j
        expectedFrequencies.append(0.0081) #Expected frequency of k
        expectedFrequencies.append(0.0421) #Expected frequency of l
        expectedFrequencies.append(0.0253) #Expected frequency of m
        expectedFrequencies.append(0.0717) #Expected frequency of n
        expectedFrequencies.append(0.0747) #Expected frequency of o
        expectedFrequencies.append(0.0207) #Expected frequency of p
        expectedFrequencies.append(0.001) #Expected frequency of q
        expectedFrequencies.append(0.0633) #Expected frequency of r
        expectedFrequencies.append(0.0673) #Expected frequency of s
        expectedFrequencies.append(0.0894) #Expected frequency of t
        expectedFrequencies.append(0.0268) #Expected frequency of u
        expectedFrequencies.append(0.0106) #Expected frequency of v
        expectedFrequencies.append(0.0183) #Expected frequency of w
        expectedFrequencies.append(0.0019) #Expected frequency of x
        expectedFrequencies.append(0.0172) #Expected frequency of y
        expectedFrequencies.append(0.0011) #Expected frequency of z
        
        d=c.lower()
        d=re.sub(r'[^a-z]',"",d)
        d=re.sub(r"\\s","",d)
        
        cipher=[]
        for i in range(len(c)):
            cipher.append(ord(d[i])-97)
        
        ke=k.lower()
        ke=re.sub(r'[^a-z]',"",ke)
        ke=re.sub(r'\\s',"",ke)
        key=list(ke.encode())

        for k in range(len(key)):
            key[k]=ord(key[k])-97
        
        char_counts=[]
        for j in range(CHROMOSONE_LEN):
            char_counts.append(0)
        
        plain=[]

        key_ptr=0
        for k in range(len(cipher)):
            key_char=chr(0)
            if len(key) > 0:
                while key[key_ptr] < 0 or key[key_ptr] > CHROMOSONE_LEN-1 :
                    key_ptr=(key_ptr+1)%len(key)
                key_char=key[key_ptr]
                key_ptr=(key_ptr+1)% len(key)
              
            plain.append((CHROMOSONE_LEN+cipher[k]-key_char)%CHROMOSONE_LEN)


        for h in plain:
            char_counts[h]=char_counts[h]+1
        
        score=0
        for l in range(len(char_counts)):
            score =score+abs((float(char_counts[l])/len(plain)-expectedFrequencies[l])) 
        
        return score

    def genes_str(self):
        return str(self.genes)

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
        
        self.pop_fitness=avg_fit/TOTAL_POP
    
    def return_parents(self):
        return self.parents

    def selection(self,pop,pop_2,chromosone_len):
        
        selection=Selection(pop,chromosone_len)

        while len(pop_2.population) < TOTAL_POP:
            self.parents.append(selection.tournament(self.parents,5))
            self.parents.append(selection.tournament(self.parents,5))
            crossover=Crossover(self.parents,CHROMOSONE_LEN)

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
    #CHROMOSONE_LEN=int(input("Chromosones Size: "))

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
    decrypted=decrypt("".join(record[0]).strip(','),ENCRYPTED)
    print ""
    print "Choromsone len: ",CHROMOSONE_LEN
    print "".join(record[0]).strip(',')
    print "Fitness: ", record[1]
    print "Decrypt: ",decrypted

