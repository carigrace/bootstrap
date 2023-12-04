#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:07:23 2023

@author: Carina Scholtens, Lilly Parker, Alicia Alexander
"""
#%% imports
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os
import numpy as np

#%%
os.chdir('/Users/carinascholtens/Downloads')
data = pd.read_csv('2017_Fuel_Economy_Data.csv')
dat = data['Combined Mileage (mpg)']
#%% class
class BootCI():
    """This class creates a bootstrap sample, runs the sample n times, and
    plots the results. It can also create a confidence interval."""
    
    def __init__(self, dat = None, stat = None):
        """initializes the class"""
        self.stat = 'mean'
        self.dat = dat
        self.ci_level = .95
        self.boot_stat = []
        self.n_boot = len(self.boot_stat)
        self.boot_df = pd.DataFrame({'x': self.boot_stat})
        
        
    def bootstrap_sample(self, n):
        """
        This function bootstrap samples a sample size n from a given 
        statistic- either median, mean, and standard deviation.

        Parameters
        ----------
        n : integer.
            greater than or equal to 1.

        Raises
        ------
        TypeError
            This error happens when a wrong statistic name is entered. Enter
            'median' = median
            'mean'= mean
            'stdev' = standard deviation

        Returns
        -------
        self.boot_stat : list 
            list of the bootstrap sample of size n from the given statistic.

        """
        n1 = abs(n)
        
        for i in range(n1):
            
            boot_sample = dat.sample(len(self.dat), replace = True)
            
            if  self.stat == 'median':
                self.boot_stat.append(float(boot_sample.median()))
            elif self.stat == 'mean':
                self.boot_stat.append(float(boot_sample.mean()))
            elif self.stat == 'stdev':
                self.boot_stat.append(float(boot_sample.std()))
            else:
                raise TypeError("wrong statistic name")
                
        self.n_boot = len(self.boot_stat)
        return self.boot_stat
    

    def boot_clear(self):
        """clears the list boot_clear, allowing for new data to be sampled."""
        self.boot_stat = []
        return self.boot_stat

    def load_data(self, dat):
        """Loads data to be sampled. The data has to be a pandas series."""
        self.dat = dat
        self.n = len(self.dat)
        return self.dat
    
    def set_statistic(self, stat):
        """allows the user to choose which statistic they want to find and adds
        the statistic to the list, boot_stat. 
      
        The stat can be as follows:
            
            'median' = median
            'mean'= mean
            'stdev' = standard deviation            
        """
        self.stat = stat
        self.boot_stat = []
        return self.stat 
    
    def plot_bootstrap(self):
        """creates a dataframe and plots the dataframe"""
        boot_df = pd.DataFrame({'x': self.boot_stat})
        
        plot = (
         ggplot(boot_df, aes(x = 'x')) + 
         geom_histogram(fill = 'green') 
        )
        return plot
        
        
    def percentile(self, level = 95):
        """takes a level, an integer 0<level<99 and finds that level's 
        percentile. Automatically creates a 95% confidence interval if no 
        level is entered."""
        lb = (100-level)/2 
        ub = 100-lb 
        return np.percentile(self.boot_stat, [lb, ub])
    

#%% testing!!
f = BootCI()

f.load_data(dat)

f.bootstrap_sample(1000)

f.plot_bootstrap()

f.percentile()

f.boot_clear()

    
