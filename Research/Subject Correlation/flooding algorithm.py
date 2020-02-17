#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:39:40 2018

@author: wolfpack
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

mean_all = pd.read_csv('marks_mean.csv')
mean_all = mean_all.drop("Unnamed: 0",axis=1)
cor_matrix = mean_all.corr()

mat_col = cor_matrix.columns

def flooding(graph,nodelist):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if(graph[i][j]>0.8):
                nodelist[j] = nodelist[j] * graph[i][j]
            else:
                graph[i][j] = 0
    return nodelist
            

mat = cor_matrix.as_matrix()

x = flooding(mat,[1,1,1,1,1,1,1,1,1,1,1,1])

plt.rcdefaults()
y_pos = np.arange(len(mat_col))
performance = x
plt.figure(figsize=(20,5))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, mat_col)
plt.ylabel('Flood score')
plt.title('Flooding subject correlation coefficients')

plt.show()