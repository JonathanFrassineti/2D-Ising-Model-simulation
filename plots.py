# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:04:25 2019

@author: Jonathan Frassineti
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from sys import argv
import configparser

configu = configparser.ConfigParser()
configu.read(sys.argv[1])

N = configu.get('settings', 'N')
M = configu.get('settings', 'M')
numberTemp = configu.get('settings', 'numberTemp')

source1 = configu.get('paths','my_time')
source2 = configu.get('paths','my_ene')
source3 = configu.get('paths','my_mag')

destination1 = configu.get('paths','time_pic')
destination2 = configu.get('paths','enemag_pic')


N = int(N)
M = int(M)
numberTemp = int(numberTemp)

T = np.linspace(1.50,3.50,numberTemp)

def configurationPlot():
    """This module plots the configuration once 
    passed to it along with time, for a given T.
        
    Parameters:
        f: figure to plot.
        configuration: state of the configuration created by 
        initialstate(N).
        i: time interval.
        N: length of the square lattice (N*N).
        n: number of subplot."""
    config = np.load(source1) 
    i = [0,1,4,32,100,1000]
    f = plt.figure(figsize=(15, 15), dpi=80)
    X, Y = np.meshgrid(range(N), range(M))
    for n in range(len(i)):
        sp =  f.add_subplot(3, 3, n+1)  
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)      
        plt.pcolormesh(X, Y, config[n], cmap=plt.cm.RdBu)
        plt.title('Time=%d'%i[n]) 
        plt.axis('tight')    
    f.savefig(destination1)
    
def graphPlot():
    """ This method plots the magnetization and the energy of the lattice.
    """
    energy = np.load(source2)   
    magnetization = np.load(source3)    
    f = plt.figure(figsize=(18, 18)) # plot the calculated values    
    sp = f.add_subplot(2, 2, 1 )
    plt.scatter(T, energy, s=50, marker='o', color='IndianRed')
    plt.xlabel("Temperature (T)", fontsize=20)
    plt.ylabel("Energy ", fontsize=20)        
    plt.axis('tight')
    sp =  f.add_subplot(2, 2, 2 )
    plt.scatter(T, abs(magnetization), s=50, marker='o', color='RoyalBlue')
    plt.xlabel("Temperature (T)", fontsize=20) 
    plt.ylabel("Magnetization ", fontsize=20)   
    plt.axis('tight')
    f.savefig(destination2)

configurationPlot()
graphPlot()

print("Figures saved!")