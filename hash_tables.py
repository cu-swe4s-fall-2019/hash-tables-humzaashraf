import os
import sys
import time
import random
import matplotlib.pyplot as plt

def h_ascii(key, N):
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_rolling(key, N, p=53, m=2**64):
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N

class LinearProbe:
    def __init__(self, N, hf):
        self.hash_function = hf
        self.N = N
        self.T = [ None for i in range(N) ]
        self.M = 0
        self.hash = []

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value, test_slot)
                self.M += 1
                self.hash.append(test_slot)
                return True
        return False

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                print(self.T[test_slot][1])
                return self.T[test_slot][1]
        return None

class ChainedHash:
    def __init__(self, N, hf):
        self.hash_function = hf
        self.N = N
        self.T = [ [] for i in range(N) ]
        self.M = 0
        self.hash = []

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        self.T[hash_slot].append((key,value))
        self.M += 1
        self.hash.append(hash_slot)
        return True

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for k,v in self.T[hash_slot]:
            if key == k:
                return v
        return None

if __name__ == '__main__':

    start_time = time.time()

    # file = open('rand_values.txt','w')
    # for i in range(len(values)):
    #     file.write((values[i]) + '\n')
    # file.close()

    keys = []
    for l in open('rand_words.txt'):
        keys.append(str(l.rstrip().split('\n')))
    
    values = []
    for l in open('rand_values.txt'):
        values.append(str(l.rstrip().split('\n')))

    elements = [x for x in range(len(values))]

    LP = LinearProbe(100000, h_rolling)
    for i in range(len(values)):
         LP.add((str(keys[i])),(str(values[i])))

    #LP.search(str(['Mondayish']))
    #print(LP.hash)
    #print(elements)

    print("--- %s seconds ---" % (time.time() - start_time))

    #plt.scatter(elements, LP.hash)
    #plt.savefig('ChainedHash_rolling_N_100000.png')