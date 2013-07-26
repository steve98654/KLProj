#! /usr/bin/python 

from numpy import *
from random import * 
import matplotlib.pyplot as plt

def phi(k,t):
    return sqrt(2)*sin((k - 0.5)*pi*t)

def evl1(k): 
    return 1./((k-0.5)**2*pi*pi)

def BM(phi, evl1, mxmds, mu, sig):
    t = linspace(0,1,mxmds)
    W = zeros(mxmds)

    for i in xrange(1,mxmds):
        tnum = normalvariate(mu, sig)
        W += tnum*phi(i,t)*sqrt(evl1(i)) 

    return (t,W)

# Example plotting a Brownian motions

for j in xrange(10):
    (t,W) = BM(phi, evl1,  100,0,1)

    plt.plot(t, W, '-')

plt.show()

