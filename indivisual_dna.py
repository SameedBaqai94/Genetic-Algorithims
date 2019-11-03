#!/usr/bin/python2

from __future__ import division
import random
import math
import re

def new_char():
    c=int(random.random() * 26+97)

    return str(unichr(c))
def split(word):
    return[ord(char) for char in word]

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
        for j in range(26):
            char_counts.append(0)
        
        plain=[]

        key_ptr=0
        for k in range(len(cipher)):
            while key[key_ptr] < 0 or key[key_ptr] >25:
                key_ptr=key_ptr+1%len(key)
                break
            plain.append((26+cipher[k]-key[key_ptr])%26)

            key_ptr=(key_ptr+1)% len(key)

        for h in plain:
            char_counts[h]=char_counts[h]+1
        
        score=0
        for l in range(len(char_counts)):
            score =score+abs((float(char_counts[l])/len(plain)-expectedFrequencies[l])) 
        
        return score

    def genes_str(self):
        return str(self.genes)