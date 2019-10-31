#!/usr/bin/python2

from __future__ import division
import random
import math
import re

def new_char():
    c=int(random.random() * 26+97)

    return str(unichr(c))

class Indivisual_DNA:

    def __init__(self,num):
        self.genes=[]
        self.fitness=0

        for i in range(num):
            self.genes.append(new_char())
    
    def calc_fitness(self):
        score=0
        for k in range(len(self.genes)):
            #if self.genes[k]==target[k]:
                #score=score+1
        
        self.fitness=score/len(target)
    
    def fitness(self,s,c):
        d=c.lower()
        d=re.sub(r'[^a-z]',"",d)
        d=re.sub(r"\\s","",d)
        
        cipher=[len(c)]
        for i in range(len(len(c))):
            cipher.append(ord(d[i])-97)
        
        ke=s.lower()
        ke=re.sub(r'[^a-z]',"",ke)
        ke=re.sub(r'\\s',"",ke)
        for k in range(len(ke)):
            ke[i]=char(ord(ke[i])-97)
        
        char_counts=[26]
        for j in range(len(char_counts)):
            char_counts.append(0)
        
        plain=[len(cipher)]

        int key_ptr=0
        for k in range(len(cipher)):
            while ke[key_ptr] < 0 or ke[key_ptr] >25:
                key_ptr=(key_ptr+1)%len(ke)
            plain[k]=((26+cipher[k]-ke[key_ptr])%26)

            key_ptr=(key_ptr+1)% len(ke)

        for h in plain:
            char_counts[h]=char_counts[h]+1
        
        score=0
        for l in range(len(char_counts)):
            score +=abs(((float(char_counts[l]/len(plain)))))
