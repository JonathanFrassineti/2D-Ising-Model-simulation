# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:01:39 2019

@author: Jonathan Frassineti
"""
import numpy as np
from numpy.random import rand
    
def initialstate(N,M):
    """This method generates a random spin configuration for the initial condition.
       
    Parameters
        N : length of the lattice.
        M : width of the lattice.
    
    Returns:
        The state of the initial configuration of the (N*M) spins. 
        
    Raise:
        ValueError if length or width of the lattice is less than 1."""
    if N < 1 or M < 1:
        raise ValueError('Both dimensions of the lattice must be > 1, but are {} and {}'.format(N,M))
    np.random.seed(1)
    initState = np.random.choice([-1,1],size=(N,M)) 
    return initState
        
def montmove(config,beta):
    """This method creates a Monte Carlo 
    move using the Metropolis algorithm.
        
    Parameters:
        config: state of the configuration created by initialstate(N,M).
        beta: 1/kT, where T is temperature and Boltzmann constant k is out equal to 1.
            
    Returns:
        The modified state of the lattice where the energy is lower than the initial one."""
    length = len(config)
    width = len(config[0])
    for i in range(length):
        for j in range(width):
            x = np.random.randint(0,length)
            y = np.random.randint(0,width)
            #State of the (x,y) spin in the lattice.
            spin = config[x,y]
            #State of the nearest neighbours spins in the lattice (there are 4).
            others = config[(x+1)%length,y] + config[x,(y+1)%width] + config[(x-1)%length,y] + config[x,(y-1)%width]
            #Energy change if spin (x,y) is flipped, according to the surrounding spins."        
            energyCost = 2*spin*others
            #If the energy change is negative, accept the move and flip the spin, otherwise accept the move with probability exp(-cost*beta), and flip the spin.
            if energyCost < 0 :
                spin *= -1
            elif rand() < np.exp(-energyCost*beta):
                spin *= -1  
            #New state of the spin."  
            config[x,y] = spin         
    return config
    
def calculateEnergy(config):
    """This method calculates the energy of a given configuration, given the exchange constant J = 1.
        
    Parameters:
        config: state of the configuration created by initialstate(N,M).
            
    Returns:
        The calculated energy of the modified configuration of the lattice."""
    energy = 0
    for i in range(len(config)):
        for j in range(len(config[0])):
            spinEnergy = config[i,j]
            othersEnergy = config[(i+1)%len(config),j] + config[i,(j+1)%len(config[0])] + config[(i-1)%len(config),j] + config[i,(j-1)%len(config[0])]
            #The change in energy is given by the product of the (x,y) spin and the 4 nearest neighbours spins.
            energy += -spinEnergy*othersEnergy
    return energy/4
    
def calculateMagn(config):
    """This method calculates the magnetization of a given configuration of spins.
        
    Parameters:
        config: state of the configuration created by initialstate(N,M).
            
    Returns:
        The magnetization of the modified lattice, which is the sum of all the spins."""
    magnetization = np.sum(config)
    return magnetization
            
def simulate(config,lattice_T):   
    """This module simulates the Ising model lattice 
        for a given temperature, under the critical temperature, 
        where the systemis ordered (ferromagnetic state).
        This also saves an array with the simulation data of the lattice.
        
    Parameters:
        config: state of the configuration created by initialstate(N,M).
            
    Returns:
        The different states during time.
        """
    temperature = lattice_T # Initialise the lattice with a specific temperature.
    initState = config.copy()   
    evolutionSteps = 1001
    states = [initState]
    for i in range(evolutionSteps):
        #print("Simulation at time {}".format(i))
        modState = montmove(config, 1.0/temperature)
        if i == 1:
            state2 = modState.copy() 
            states.append(state2)    
        if i == 4:   
            state3 = modState.copy()
            states.append(state3)
        if i == 32:  
            state4 = modState.copy()
            states.append(state4)
        if i == 100:  
            state5 = modState.copy()
            states.append(state5)
        if i == 1000:   
            state6 = modState.copy()
            states.append(state6)
    return states  
    
    print("Simulation done!") 
    

