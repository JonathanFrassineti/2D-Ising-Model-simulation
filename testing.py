# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:09:18 2019

@author: Jonathan Frassineti
"""

from ising import Ising
import numpy as np

N = 100

def test_initialstate():
    state = Ising()
    model =state.initialstate(N)
    assert model.all() == 1 or model.all() == -1
            
if __name__ == '__main__':
    pass