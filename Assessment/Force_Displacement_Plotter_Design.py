# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:24:50 2022

@author: VACALDER
"""
import pandas as pd
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt



data_file ='force_displacement_cl_5_0.csv'
main_DF = pd.read_csv(data_file)


#plotting commands
linestyle_str = ['solid', 'dotted','dashed','dashdot','dashed',(0, (3, 5, 1, 5, 1, 5))] 
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.serif':'Times New Roman'})
plt.rcParams.update({'mathtext.fontset':'stix'})
colors = ['#d94545','#519872','#73a8d4','#f7b76d','#545066']

force = list(main_DF['Force'])
displacement = list(main_DF['Total_displacement'])

delta_ls = 0.498
force_ls = 2099.4


plt.figure(1,figsize=(5,4))
plt.plot(displacement,force,color=colors[0],linestyle=linestyle_str[0])
plt.axvline(x = 0.54, color=colors[1], linestyle = linestyle_str[1],linewidth=1.5)
plt.annotate(r'$\Delta_{t}=0.54\%$', xy=(0.54+0.02, 1250),fontweight='bold',color=colors[1],fontsize=11,bbox={'facecolor': 'white', 'alpha': 1.0, 'pad': 3})
plt.axvline(x = 0.43, color=colors[2], linestyle = linestyle_str[1],linewidth=1.5)
plt.annotate(r'$\Delta_{bb}=0.43\%$', xy=(0.43+0.02, 1000),fontweight='bold',color=colors[2],fontsize=11,bbox={'facecolor': 'white', 'alpha': 1.0, 'pad': 3})
plt.axvline(x = 0.42, color=colors[3], linestyle = linestyle_str[2],linewidth=1.5)
plt.annotate(r'$\Delta_{\theta}=0.42\%$', xy=(0.42-0.21, 1250),fontweight='bold',color=colors[3],fontsize=11,bbox={'facecolor': 'white', 'alpha': 1.0, 'pad': 3})
plt.xlim(0,1)
plt.ylim(0,2500)
plt.xlabel('Displacement (m)', fontsize=11)
plt.ylabel('Force (KN)', fontsize=11)
plt.tick_params(direction='out',axis='both',labelsize=10)
plt.grid()
plt.show()

plt.savefig("Force_Displacement_Design_5.pdf",dpi=600,bbox_inches='tight', pad_inches=0)