# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:25:29 2019

@author: Jonathan Frassineti
"""
from ising import Ising
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

#main part of the code

rm = Ising()
nt = 88      #  number of temperature points
N = 16         #  size of the lattice, N x N
eqSteps = 1024      #  number of MC sweeps for equilibration
mcSteps = 1024       #  number of MC sweeps for calculation

T = np.linspace(1.58, 3.38, nt); 
E,M = np.zeros(nt), np.zeros(nt)
n1 = 1.0/(mcSteps*N*N)
# divide by number of samples, and by system size to get intensive values

for tt in range(nt):
    E1 = M1 = 0
    config = rm.initialstate(N)
    iT=1.0/T[tt]
    
    for i in range(eqSteps):         # equilibrate
        rm.montmove(N,config, iT)           # Monte Carlo moves

    for i in range(mcSteps):
        rm.montmove(N,config, iT)           
        Ene = rm.energy(N,config)     # calculate the energy
        Mag = rm.mag(config)        # calculate the magnetisation

        E1 = E1 + Ene
        M1 = M1 + Mag

    E[tt] = n1*E1
    M[tt] = n1*M1

rm.graphPlot(T,E,M)
rm.simulate(N)