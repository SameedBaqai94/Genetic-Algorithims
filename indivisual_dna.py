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
        expectedFrequencies = []
        expectedFrequencies.append(0.0085)
        expectedFrequencies.append(0.0016)
        expectedFrequencies.append(0.0316)
        expectedFrequencies.append(0.0387)
        expectedFrequencies.append(0.0021)
        expectedFrequencies.append(0.0218)
        expectedFrequencies.append(0.0209)
        expectedFrequencies.append(0.0041)
        expectedFrequencies.append(0.0496)
        expectedFrequencies.append(0.0770)
        expectedFrequencies.append(0.0773)
        expectedFrequencies.append(0.0022)
        expectedFrequencies.append(0.0099)
        expectedFrequencies.append(0.0747)
        expectedFrequencies.append(0.0085)
        expectedFrequencies.append(0.0988)
        expectedFrequencies.append(0.0023)
        expectedFrequencies.append(0.0035)
        expectedFrequencies.append(0.0354)
        expectedFrequencies.append(0.0054)
        expectedFrequencies.append(0.0067)
        expectedFrequencies.append(0.0087)
        expectedFrequencies.append(0.0005)
        expectedFrequencies.append(0.0098)
        expectedFrequencies.append(0.0067)
        expectedFrequencies.append(0.0024)
        expectedFrequencies.append(0.0005)
        
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