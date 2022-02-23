# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:52:32 2022

@author: Robbe Decapmaker
"""

from sympy import *
from sympy.plotting import *
import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(-3,9,100)
plt.figure()
x = symbols('x', real = true)
plt.grid(True, which='both')

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.ylabel("Verplaatsing (m)")
plt.xlabel("\u03C9 t (s)")

def f(x): return np.cos(x + np.pi/2)


plt.plot(xx,f(xx),'r', lw = 1)
plt.hlines(1,-3,9)
plt.hlines(-1,-3,9)
plt.axvline(x=-np.pi/2)
plt.yticks([])
plt.text(-np.pi/2 +0.1, 0.1, '- \u03C6')
plt.text(-2.8, 0.9, 'A')
plt.text(-2.8, -0.95, '- A')
#plt.show()
plt.savefig('Harmonische_Oscillator.pdf')

plt.clf()
xx = np.linspace(-1,1,100)
def f(x) : return x**2
def g(x) : return -x**2 + 1

Potential = plt.plot(xx,f(xx),'r', lw = 1)
Kinetic = plt.plot(xx,g(xx),'g', lw = 1)
plt.xlabel("Verplaatsing (m)")
plt.ylabel("E(x) (J)")
#plt.hlines(1,-1,1)
plt.legend(loc='lower left',labels=['Potentiële energie', 'Kinetische energie'])
#plt.show()
plt.savefig('Energie_Balans.pdf')