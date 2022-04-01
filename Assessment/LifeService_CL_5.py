# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:33:48 2022

@author: VACALDER
"""
import pandas as pd
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt



#plotting commands
linestyle_str = ['solid', 'dotted','dashed','dashdot','dashed',(0, (3, 5, 1, 5, 1, 5))] 
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.serif':'Times New Roman'})
plt.rcParams.update({'mathtext.fontset':'stix'})
colors = ['#d94545','#519872','#73a8d4','#f7b76d','#545066']

delta_c=1
CL = [0,0,5]
years = [0,18.7,100]

plt.figure(1,figsize=(4,3))
plt.plot(years,CL,color=colors[0],linestyle=linestyle_str[0])



plt.xlim(0,100)
plt.ylim(0,7.5)
plt.xlabel(r'Time, $t$ (years)', fontsize=11)
plt.ylabel(r'Corrosion Level, $CL$ (%)', fontsize=11)
plt.tick_params(direction='out',axis='both',labelsize=10)
plt.grid()
plt.show()

plt.savefig("CorrosionLevel_lifeService_5.pdf",dpi=600,bbox_inches='tight', pad_inches=0)