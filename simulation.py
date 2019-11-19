# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:25:29 2019

@author: Jonathan Frassineti
"""
import ising
import numpy as np
import sys
from sys import argv
import configparser

#main part of the code
config = configparser.ConfigParser()
config.read(sys.argv[1])

N = config.get('settings', 'N')
M = config.get('settings', 'M')
numberTemp = config.get('settings', 'numberTemp')
eqSteps = config.get('settings', 'eqSteps')

N = int(N)
M = int(M)
numberTemp = int(numberTemp)
eqSteps = int(eqSteps)

T = np.linspace(1.50,3.50,numberTemp) 
Energy = np.zeros(numberTemp)
Magn = np.zeros(numberTemp)
inverseTemp = 1.0/T 
n1 = 1.0/(eqSteps*N*M) 

for tempInterval in range(numberTemp):
    
    config = ising.initialstate(N,M)
    Energy1 = Magn1 = 0
    
    for i in range(eqSteps):
        ising.montmove(config,inverseTemp[tempInterval])

    for i in range(eqSteps):
        ising.montmove(config,inverseTemp[tempInterval])           
        Energy = ising.calculateEnergy(config)     # calculate the energy
        Magn = ising.calculateMagn(config)        # calculate the magnetisation
        Energy1 += Energy
        Magn1 +=  Magn

    Energy[tempInterval] = n1*Energy1
    Magn[tempInterval] = n1*Magn1
    
np.save('./data/ene',configuration.Energy)
np.save('./data/mag',configuration.Magn)

totalStates = ising.simulate(ising.initialstate(N,M))
np.save('./data/time',np.asarray(totalStates))