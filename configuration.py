# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:09:14 2019

@author: Jonathan Frassineti
"""

import numpy as np

N = 16 #length of the lattice
M = 16 #width of the lattice

numberTemp = 80 #number of temperature intervals
T = np.linspace(1.50,3.50,numberTemp) #temperature array
Energy = np.zeros(numberTemp)
Magn = np.zeros(numberTemp)
eqSteps = 1024 #MonteCarlo moves for equilibration and calculation
inverseTemp = 1.0/T #inverse temperature = beta

n1 = 1.0/(eqSteps*N*M) #divide by size of the lattice and steps for intensive values