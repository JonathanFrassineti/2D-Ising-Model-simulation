# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:01:39 2019

@author: Jonathan Frassineti
"""
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

class Ising():
    "This class simulates the Ising model in 2 dimensions."
    def initialstate(self,N):
        "This method generates a random spin configuration for initial condition."
        state = 2*np.random.randint(2,size=(N,N))-1
        return (state)
        
if __name__ == '__main__':
    pass
