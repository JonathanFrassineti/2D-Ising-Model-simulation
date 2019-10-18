# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:09:18 2019

@author: Jonathan Frassineti
"""

from ising import Ising
import numpy as np
import copy

"Length of the 2D square spin lattice."
N = 15
"Number of temperature intervals."
nt = 50
"Number of steps used to equilibrate the syste with MonteCarlo algorithm."
eqsteps = 100
"Temperature array T from 1.0 to 4.0 (unitless)."
T = np.linspace(1.0,4.0,nt)
"Creation of an Ising object."
state = Ising()

def test_initialstate():
    "Initialazing the model with N*N spins of values 1 and -1."
    model = state.initialstate(N) 
    abs_model = np.abs(model)
    "Test if all the spins have really the values 1 and -1."
    assert abs_model.all() == 1 
    
def test_montmove():
    "Do a cycle in order to range from lowest temperature to highest one."
    for tt in range(nt):
        "Calculation of beta = 1/kT, where k is put equal to 1 for semplicity."
        it = 1.0/T[tt]
        model = state.initialstate(N)
        "Copy the original state in order to compare it with the modified one."
        init = copy.deepcopy(model)
        "Montecarlo moves from the original state to the modified one."
        for i in range (eqsteps):
            config = state.montmove(N,model,it)
        diff = config - init
        "Test if the modified state is really different from the original one."
        assert np.any(diff) == True

def test_energy():
    "This method calculates the energy of a given configuration, given the exchange constant J = 1."
    energy = 0
    "Copy the initial energy in order to compare it with the modified one."
    init = copy.deepcopy(energy)
    model = state.initialstate(N)
    "Test if the final energy is really different from the initial energy."
    assert state.energy(N, model) != init
        
def test_mag():
    "This method calculates the magnetization of a given configuration."
    model = state.initialstate(N)
    "Test if the magnetization is really the sum of all the elements of the configuration."
    assert state.mag(model) == np.sum(model)
    "Test if the magnetization is different from 0."
    assert state.mag(model) != 0
       
if __name__ == "main":
    pass                
            
            


        
         
            
