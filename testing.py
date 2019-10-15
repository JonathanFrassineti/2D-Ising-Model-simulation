# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:09:18 2019

@author: Jonathan Frassineti
"""

from Ising import Ising

init_state = 5
model = Ising(state=init_state)

def test_init():
    assert model.state == init_state
    
    
if __name__ == '__main__':
    test_init()