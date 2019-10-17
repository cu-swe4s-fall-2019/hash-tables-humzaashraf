import sys
import hash_functions
import time
import random

class LinearProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.T = [ None for i in range(N) ]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        hash_slot = self.hash_fucntion(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None

class ChainedHash:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.T = [ [] for i in range(N) ]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        self.T[hash_slot].append((key,value))
        self.M += 1
        return True

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for k,v in self.T[hash_slot]:
            if key == k:
                return v
        return None

if __name__ == '__main__':
    