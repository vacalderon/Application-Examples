# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:24:50 2022

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
sd = [0,delta_c,delta_c]
periods = [0,4,6]

DSF = np.sqrt(0.07/(0.02+0.15))
delta_c_xi_eff= delta_c*DSF


sd_xi_eff=[0,delta_c_xi_eff,delta_c_xi_eff]

assessment_period = 2.724
delta_cap = 0.629

plt.figure(1,figsize=(4,3))
plt.plot(periods,sd,color=colors[0],linestyle=linestyle_str[0])
plt.plot(periods,sd_xi_eff,color=colors[2],linestyle=linestyle_str[0])
#plt.scatter(assessment_period,delta_cap,s=40, marker='D',color=colors[1])

plt.annotate(r'$\xi=5\%$', xy=(4, delta_c+0.05),fontweight='bold',color=colors[0],fontsize=11)
plt.annotate(r'$\xi_{eff}=15\%$', xy=(4, delta_c_xi_eff+0.05),fontweight='bold',color=colors[2],fontsize=11)

plt.xlim(0,6)
plt.ylim(0,1.25)
plt.xlabel(r'Period, $T$ (s)', fontsize=11)
plt.ylabel(r'Spectral Displacement, $Sd$ (m)', fontsize=11)
plt.tick_params(direction='out',axis='both',labelsize=10)
plt.grid()
plt.show()

plt.savefig("SD_Design_5.pdf",dpi=600,bbox_inches='tight', pad_inches=0)