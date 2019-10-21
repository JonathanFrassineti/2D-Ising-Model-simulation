# 2D Ising model

The Ising Hamiltonian can be written as, 

![equation1](https://latex.codecogs.com/gif.latex?H&space;=&space;-J\sum_{\left&space;\langle&space;ij&space;\right&space;\rangle}S_{i}S_{j})
- The spins ***S<sub>i*** can take values ±1,  
- ***⟨ij⟩*** implies nearest-neighbor interaction only,  
- ***J***>0 is the strength of exchange interaction.  

The system undergoes a 2nd order phase transition at the critical temperature ***T<sub>c***. For temperatures less than ***T<sub>c***, the system magnetizes, and the state is called the ferromagnetic or the ordered state. This amounts to a globally ordered state due to the presence of local interactions between the spin. For temperatures greater than ***T<sub>c***, the system is in the disordered or the paramagnetic state. In this case, there are no long-range correlations between the spins.  

The order parameter 

![equation2](https://latex.codecogs.com/gif.latex?m&space;=&space;\frac{\left&space;\langle&space;S&space;\right&space;\rangle}{N}) 

for this system is the average magnetization. The order parameter distinguishes the two phases realized by the systems. It is zero in the disordered state, while non-zero in the ordered, ferromagnetic, state.
The one dimensional (1D) Ising model does not exhibit the phenomenon of phase transition while higher dimension do; this can be argued based on arguments related to the change in free energy 

![equation3](https://latex.codecogs.com/gif.latex?F&space;=&space;E&space;-&space;TS)

 Here ***E*** and ***S*** are, respectively, the energy and entropy of the system. We estimate the net change in free energy for introducing a disorder in an otherwise ordered system. The ordered state can only be stable if the net change in free energy is positive, ***ΔF>0***, for any non-zero temperature.

In this project we will simulate the ***2D*** Ising model using a Monte-Carlo simulation.

## Monte-Carlo simulation of 2D Ising model

The following code simulates the Ising model in 2D using the Metropolis algorithm. The main steps of Metropolis algorithm are:

1. Prepare an initial configuration of ***N*** spins  
2. Flip the spin of a randomly chosen lattice site.  
3. Calculate the change in energy ***dE***.  
4. If ***dE < 0***, accept the move. Otherwise accept the move with probability ***exp^{-dE/T}***. This satisfies the detailed balance condition, ensuring a final equilibrium state.  

Repeat 2-4. 

For references about Metropolis algorithm, see [this link](https://www.asc.ohio-state.edu/braaten.1/statphys/Ising_MatLab.pdf).

## Structure of the project

This is how I divided my project into blocks:

- In the file [ising](https://github.com/JonathanFrassineti/Software-Project/blob/master/ising.py) I have built the class Ising that estimates and plots energy and magnetization of the system, and for a given temperature plots the time evolution of the system from disordered state to ordered state.  

- In the file [testing](https://github.com/JonathanFrassineti/Software-Project/blob/master/testing.py) I have tested all the methods of class Ising to ensure that all of them work properly.

- In the file [simulation](https://github.com/JonathanFrassineti/Software-Project/blob/master/simulation.py) there is the main part of the code, where I have created an Ising object that executes all the methods in order to calculate the energy and the magnetization of a configuration of spins; in addition, I have printed the time evolution of a given configuration of spins for a specific temperature.

And this is how the simulation of a given configuration looks like, for a given temperature and during the time: ![config](configPlot.png)

