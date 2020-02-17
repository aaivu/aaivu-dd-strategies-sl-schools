#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:31:13 2018

@author: adeesha
"""

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import itertools


data = pd.read_csv('/home/adeesha/southland_6_1.csv')

feature_cols = ['Religon','Sinhala','English','Maths','Science','History','Citizenship Education','Health','Tamil','Geography','PTS']
final_sub = []
final_err = []
for sub in feature_cols:
    y = data[sub]
    temp_feature_cols =[]
    for x in feature_cols:
        if(x!=sub):
            temp_feature_cols.append(x)
    for i in range(1,len(temp_feature_cols)):
        combs = []
        comb_sqrts = []
        comb_features = []
        for j in range(1,len(temp_feature_cols)+1):
            els = [list(x) for x in itertools.combinations(temp_feature_cols, j)]
            combs.append(els)
        for comb in combs:   
            for sub_feature_cols in comb:
                    X = data[sub_feature_cols]
                    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)
                    linreg = LinearRegression()
                    linreg.fit(X_train,y_train)
                    y_pred = linreg.predict(X_test)
                    sqrt = np.sqrt(metrics.mean_squared_error(y_test,y_pred))
                    comb_sqrts.append(sqrt)
                    comb_features.append(sub_feature_cols)
    print(str(min(comb_sqrts))+"   "+sub+"   "+str( comb_features[comb_sqrts.index(min(comb_sqrts))]))
    final_sub.append(comb_features[comb_sqrts.index(min(comb_sqrts))])
    final_err.append(min(comb_sqrts))
    
fig, ax = plt.subplots()
ax.bar(feature_cols, final_err, edgecolors=(0, 0, 0))
ax.plot([], [min(final_err), max(final_err)], 'k--', lw=4)
ax.set_xlabel('Maths')
ax.set_ylabel('Others')
plt.show()




