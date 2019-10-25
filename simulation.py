# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:25:29 2019

@author: Jonathan Frassineti
"""
import ising
import configuration
import numpy as np

#main part of the code
for tempInterval in range(configuration.numberTemp):
    config = ising.initialstate(configuration.N,configuration.M)
    Energy1 = Magn1 = 0
    
    for i in range(configuration.eqSteps):
        ising.montmove(config,configuration.inverseTemp[tempInterval])

    for i in range(configuration.eqSteps):
        ising.montmove(config,configuration.inverseTemp[tempInterval])           
        Energy = ising.calculateEnergy(config)     # calculate the energy
        Magn = ising.calculateMagn(config)        # calculate the magnetisation
        Energy1 += Energy
        Magn1 +=  Magn

    configuration.Energy[tempInterval] = configuration.n1*Energy1
    configuration.Magn[tempInterval] = configuration.n1*Magn1
    
np.save('./data/ene',configuration.Energy)
np.save('./data/mag',configuration.Magn)

totalStates = ising.simulate(ising.initialstate(configuration.N,configuration.M))
np.save('./data/time',np.asarray(totalStates))