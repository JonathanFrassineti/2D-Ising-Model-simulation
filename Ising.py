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
    def __init__(self, state=10):
        self.state = state
        
if __name__ == '__main__':
    model = Ising()