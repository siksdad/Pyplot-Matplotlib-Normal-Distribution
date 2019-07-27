#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:27:44 2017

@author: yoon-junkim
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig = plt.figure()
ax = fig.add_subplot(111)
sig = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.2,2.3,2.4,2.5,2.6,2.7]
plt.xlim(-10,10)
 
ims=[]
for add in np.arange(15):
    mu = 0.0   
    sigma= sig[add]
     # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
    v = np.random.normal(mu,sigma,10000)
    # Plot a normalized histogram with 50 bins
    count,bins,patches=plt.hist(v, 50, normed=1)       # matplotlib version (plot)
    curves=plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='k')
#    ims.append(patches)
    ims.append(curves)
   
ani = animation.ArtistAnimation(fig, ims, interval=20, repeat_delay=300, blit=True)  
plt.show()