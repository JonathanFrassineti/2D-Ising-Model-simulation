# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:09:18 2019

@author: Jonathan Frassineti
"""

import ising
import configuration
import numpy as np
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

@given(N=st.integers(1,configuration.N), M = st.integers(1,configuration.M))
@settings(max_examples = 1)
def test_initialstate(N,M):
    #Initialazing the model with N*M spins of values 1 and -1."
    model = ising.initialstate(N,M) 
    #Test if the dimensions of the lattice are N and M."
    assert len(model) == N
    assert len(model[0]) == M
    abs_model = np.abs(model)
    #Test if all the spins have really the values 1 and -1."
    assert abs_model.all() == 1 

@given(N=st.integers(1,configuration.N), M = st.integers(1,configuration.M), numbTemp = st.integers(50,configuration.numberTemp), mcSteps = st.integers(100,configuration.eqSteps))
@settings(max_examples = 1)   
def test_montmove(N, M, numbTemp, mcSteps):
    #Do a cycle in order to range from lowest temperature to highest one."
    for tempInterval in range(numbTemp):
        #Calculation of beta = 1/kT, where k is put equal to 1 for semplicity."
        model = ising.initialstate(N,M)
        #Copy the original state in order to compare it with the modified one."
        init = model.copy()
        #Montecarlo moves from the original state to the modified one."
        for i in range (mcSteps):
            config = ising.montmove(model,configuration.inverseTemp[tempInterval])
            #Test if the final state is different from the initial one.
            assert ising.calculateEnergy(config) <= ising.calculateEnergy(init)
            assert np.abs(ising.calculateMagn(config)) >= np.abs(ising.calculateMagn(init))

@given(N=st.integers(1,configuration.N), M = st.integers(1,configuration.M))
@settings(max_examples = 1)
def test_simulate(N, M):
    #This method simulates the Ising model of a given configuration for a specific T."
    initState = ising.initialstate(N,M)
    finalState = ising.simulate(initState)
    assert ising.calculateEnergy(finalState[len(finalState)-1]) <= ising.calculateEnergy(finalState[0])
    assert np.abs(ising.calculateMagn(finalState[len(finalState)-1])) >= np.abs(ising.calculateMagn(finalState[0]))
         
        



if __name__ == "main":
    pass                
            
            


        
         
            
