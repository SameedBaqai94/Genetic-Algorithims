#!/usr/bin/python2
"""
    Name:Sameed Baqai
    Date:2019-11-02
    SN:6560577
"""

from __future__ import division
import math
import re
import copy
import random

#global values
ENCRYPTED= ("xbwdesmhihslwhkktefvktkktcwfpiibihwmosfilojvooegvefwno"+
           "ichsuuspsureifakbnlalzsrsroiejwzgfpjczldokrceoahzshpbdw"+
           "pcjstacgbarfwifwohylckafckzwwomlalghrtafchfetcgfpfrgxc"+
           "lwzocdctmjebx")

TOTAL_POP=None
TOTAL_GEN=None
CROSSOVER_RATE=None
MUTATION_RATE=None
CHROMOSONE_LEN=26

#chosing a random char between 26 and 97
def new_char():
    c=int(random.random() * 26+97)

    return str(unichr(c))
#getting int of each char in list
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
#Selection class
class Selection:
    
    def __init__(self,pop,chromosone_len):
        self.pop=pop
        self.chromosone_len=chromosone_len
    #Tournament Selection
    def tournament(self,selected_parents,i):
        #randomly select some population for each parent and return the min of it
        for j in range(i):
            selected_parents.append(self.pop.population[int(random.random()*len(self.pop.population)-1)])
            return min(selected_parents)
#crossover class
class Crossover:

    def __init__(self,parents,chromosone_len):
        self.parents=parents
        self.chromosone_len=chromosone_len
    #One point crossover   
    def one_point(self):
        children=[]
        #Create 2 genes
        for i in range(2):
            children.insert(i,Indivisual_DNA(CHROMOSONE_LEN))
        #get a pointer betweem some random value to length of chromosome
        pointer=int(random.random()*CHROMOSONE_LEN-1)
        #swap out genes betwween some randon point to lenght of chromosome
        for j in range(pointer,CHROMOSONE_LEN):
            swap=children[0].genes[j]
            children[0].genes[j]=children[1].genes[j]
            children[1].genes[j]=swap
        return children
    #Uniform Order    
    def uniform_order(self):
        children=[]
        mask=[]
        reminder_genes=[]

        #create mask list
        for k in range(len(self.parents[0].genes)):
            mask.append(random.random()+1)
        #create children list
        for i in range(2):
            children.insert(i,Indivisual_DNA(CHROMOSONE_LEN))
        #if mask ==1 then add gene of first parent to first child
        #else leave it blank
        for h in range(len(mask)):
            if mask[h]==1:
                children[0].genes[h]=self.parents[0].genes[h]
            else:
                children[0].genes[h]=''
        #adding the reminder frommp parent 2 if doesnt already existsof genes to child
        for i in range(2):
            for l in range(len(self.parents[1-i].genes)):
                if children[i].genes!=self.parents[1-i].genes[l]:
                    reminder_genes.append(self.parents[1-i].genes[l])
            for k in range(len(children[i].genes)):
                if children[i].genes[k]=='':
                    children[i].genes[k]=reminder_genes.pop()
        return children
                    
#mutation classs
class Mutation:

    def __init__(self,chromosone,chromosone_len):
        self.chromosone=chromosone
        self.chromosone_len=chromosone_len
    #inversion    
    def inversion(self):
        #selecting two points and finding min max of it 
        pointer_1=int(random.random()*len(self.chromosone.genes))-1
        pointer_2=int(random.random()*len(self.chromosone.genes))-1

        minimun_value=min(pointer_1,pointer_2)
        maximum_value=max(pointer_1,pointer_2)
        total=minimun_value-maximum_value
        temp=[]
        for i in range(total):
            #push all genes to temp stack
            temp.append(self.chromosone.genes[minimun_value+i])
        for j in range(total):
            #pop them all back to chromosome genes
            self.chromosone.genes[minimun_value+j]=temp.pop()

#population class
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
    #does fitness caculation
    def calc_fitness(self):
        avg_fit=0
        for i in range(len(self.population)):
            self.population[i].fitness=self.population[i].fitnesses(str(self.population[i].genes),self.text)
            avg_fit+=self.population[i].fitness
        
        self.pop_fitness=avg_fit/TOTAL_POP
    
    def return_parents(self):
        return self.parents

    #GA operation here
    def selection(self,pop,pop_2,chromosone_len):
        
        selection=Selection(pop,chromosone_len)

        while len(pop_2.population) < TOTAL_POP:
            #creating two parents
            self.parents.append(selection.tournament(self.parents,3))
            self.parents.append(selection.tournament(self.parents,3))
            #applying crossover on them
            crossover=Crossover(self.parents,CHROMOSONE_LEN)

            if random.random() < self.cross_rate:
                #COMMENT OUT THE METHOD YOU WANT TO USE
                #BOTH WORK
                children=crossover.one_point()
                #children=crossover.uniform_order()
                #when crossover return children append it to new population
                for child in children:
                    pop_2.population.append(child)
            #mutation 
            if len(pop_2.population) >=2 and random.random() < self.mutation_rate:
                #apply mutation on given random point
                mutation=Mutation(pop_2.population[int(random.random()+len(pop_2.population)-1)],CHROMOSONE_LEN)
                mutation.inversion()
        return pop_2.population
#MAIN 
if __name__=="__main__":
    
    TOTAL_POP=int(input("Population Size(i.e 500): "))
    TOTAL_GEN=int(input("Generations Size(i.e 100): "))
    CROSSOVER_RATE=float(input("Crossover Rate in demcimal(i.e 1.0): "))
    MUTATION_RATE=float(input("Mutation Rate in decimal(i.e 0.1): "))
    #CHROMOSONE_LEN=int(input("Chromosones Size: "))

    #population instance
    population=Population(TOTAL_POP,CHROMOSONE_LEN,ENCRYPTED,CROSSOVER_RATE,MUTATION_RATE)
    population_2=None
    #elitism
    old_pop_min,new_pop_min=None,None
    record=None

    for i in range(TOTAL_GEN):
        population_2=Population(0,0,ENCRYPTED,CROSSOVER_RATE,MUTATION_RATE)
        population.calc_fitness()
        #insert population to new population
        population_2.population=population_2.selection(population,population_2,CHROMOSONE_LEN)
        population_2.pop_len=len(population_2.population)
        population_2.calc_fitness()
        #elitism
        old_pop_min=min(population.population)
        new_pop_min=min(population_2.population)
        if new_pop_min.fitness < old_pop_min.fitness:
            old_pop_min=copy.deepcopy(new_pop_min)
        else:
            #get the max of population2 pop and replace it
            #with elitism
            a=max(population_2.population)
            j=population_2.population.index(a)
            population_2.population[j]=copy.deepcopy(old_pop_min)
        print old_pop_min.fitness
        old_pop_min=new_pop_min
        record=[old_pop_min.genes,old_pop_min.fitness]
    #decrypt with whatever best fit chromosome is 
    decrypted=decrypt("".join(record[0]).strip(','),ENCRYPTED)
    print ""
    print "Choromsone len: ",CHROMOSONE_LEN
    print "".join(record[0]).strip(',')
    print "Fitness: ", record[1]
    print "Average Fitness",population.pop_fitness
    print "Decrypt: ",decrypted

