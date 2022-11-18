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

destination1 = config.get('paths','my_time')
destination2 = config.get('paths','my_ene')
destination3 = config.get('paths','my_mag')

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
    
    print("Temperature point: {}/{}".format(tempInterval,numberTemp))
    
    config = ising.initialstate(N,M)
    Energy1 = Magn1 = 0
    
    for i in range(eqSteps):
        ising.montmove(config,inverseTemp[tempInterval])

    for i in range(eqSteps):
        ising.montmove(config,inverseTemp[tempInterval])           
        Energy2 = ising.calculateEnergy(config)     # calculate the energy
        Magn2 = ising.calculateMagn(config)        # calculate the magnetisation
        Energy1 += Energy2
        Magn1 +=  Magn2

    Energy[tempInterval] = n1*Energy1
    Magn[tempInterval] = n1*Magn1
  
print("Simulation done!")
    
np.save(destination2,Energy)
np.save(destination3,Magn)

print("Energies and magnetization saved.")

print("Now, simulate the system in the ordered phase along time.")
totalStates = ising.simulate(ising.initialstate(N,M))
np.save(destination1,np.asarray(totalStates))

print("Simulation saved.")