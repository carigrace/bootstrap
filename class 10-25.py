#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:07:23 2023

@author: carinascholtens
"""

# dat = pd.DataFrame({"handspan": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 21.5, 18, 18, 20.5,
#            20, 20.3, 21.5, 19, 20.4, 22.7, 22.9, 17, 23, 23.8, 22, 21.5,
#             21.5]})


import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os

#%%
class BootCI():
    """docstring"""
    def __init__(self, dat = None, stat = None):
        self.stat = 'mean'
        self.dat = dat
        self.n_boot = 0
        self.ci_level = .95
        self.boot_stat = []
        
        
    def bootstrap_sample(self, n):
        """docstring"""
        
        for i in range(n):
            
            boot_sample = dat.sample(n, replace = True)
            if  self.stat == 'median':
                self.boot_stat.append(float(boot_sample.median()))
            elif self.stat == 'mean':
                self.boot_stat.append(float(boot_sample.mean()))
            elif self.stat == 'stdev':
                self.boot_stat.append(float(boot_sample.std()))
            else:
                raise TypeError("wrong statistic name")
        
        return boot_stat


    def boot_clear(self):
        self.boot_stat = []
        return boot_stat

    def load_data(self, dat):
        self.dat = dat
        n = len(self.dat)
        return self.dat
    
    def change_stat(self, stat):
        self.stat = stat
        return self.stat 
    
    def change_bootstrap(self, n_boot):
        self.n_boot = n_boot
    
    
#%%
os.chdir('/Users/carinascholtens/Downloads')
data = pd.read_csv('2017_Fuel_Economy_Data.csv')
dat = data['Combined Mileage (mpg)']
#%% testing!!
f = BootCI()
f.load_data(dat)
f.bootstrap_sample(10)

f.boot_clear()  
#%%
# n = len(dat) # bootstrap requires samples to be the number of values in df
# n_boot = 10_000
# stat = 'mean'

# boot_stat = []

# for i in range(n_boot):
#     boot_sample = dat.sample(n, replace = True)
#     if stat == 'median':
#         boot_stat.append(float(boot_sample.median()))
#     elif stat == 'mean':
#         boot_stat.append(float(boot_sample.mean()))
#     elif stat == 'stdev':
#         boot_stat.append(float(boot_sample.std()))
#     else:
#         raise TypeError("wrong statistic name")
        

# boot_df = pd.DataFrame({'x': boot_stat}) #ggplot needs a dataframe

# (
# ggplot(boot_df, aes(x = 'x')) + 
# geom_histogram(fill = 'green') 
# )



    
    
    
    
    
