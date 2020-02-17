#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:49:36 2018

@author: wolfpack
"""

import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import os
import sys
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

dirname = os.path.dirname(__file__)
sys.path.append("../data_parser")
import DataParser

#import data
subjects = ["Religion","Sinhala","English","Mathematics","Science","History","Geography","Citizenship Education","Health","Tamil","Art","PTS"]
marks_all = DataParser.get_marks(subjects, index='no')

#handle missing values
marks_all = DataParser.handle_missing_values(marks_all, how='-1', is_nan = True)
marks_all = DataParser.handle_missing_values(marks_all, how='-1', is_nan = False)
marks_all = marks_all.replace({-1:np.nan})
marks_all = marks_all.fillna(method='bfill', axis=1)
marks_all = marks_all.fillna(method='ffill', axis=1)
marks_all = marks_all.dropna(axis=0)

"""
PCA
"""
col_all = marks_all.columns
principalDf = pd.DataFrame()
subs_ex_ratios = []
for sub_year in range (int(len(col_all)/3)):
    if(sub_year%3 == 0):
        col = col_all[sub_year*3].split(".")[0]+"_6"
    elif(sub_year%3 == 1):
        col = col_all[sub_year*3].split(".")[0]+"_7"
    elif(sub_year%3 == 2):
        col = col_all[sub_year*3].split(".")[0]+"_8"
    marks_year_std = marks_all.iloc[:,sub_year*3:(sub_year*3)+3].copy()
    marks_year_std = StandardScaler().fit_transform(marks_year_std)
    pca = PCA(n_components=1)
    principalComponents = pca.fit_transform(marks_year_std)
    principalDf[col] = pd.DataFrame(data = principalComponents, columns = [col])
    subs_ex_ratios.append(pca.explained_variance_ratio_)
    
sub_explained = pd.DataFrame()
pca_cols = principalDf.columns
sub_explained["Subject"] = pd.DataFrame(data = pca_cols, columns = ["Subject"])
sub_explained["Explained ratio"] = pd.DataFrame(data = subs_ex_ratios, columns = ["Explained ratio"])

grade_6 = pd.DataFrame()
grade_7 = pd.DataFrame()
grade_8 = pd.DataFrame()

for col in pca_cols:
    grade = col.split("_")[-1]
    sub = col.split("_")[0]
    if(grade == "6"):
        grade_6[sub] = principalDf[col]
    if(grade == "7"):
        grade_7[sub] = principalDf[col]
    if(grade == "8"):
        grade_8[sub] = principalDf[col]
        
grade_6.to_csv("marks_pca_grade_6.csv")
grade_7.to_csv("marks_pca_grade_7.csv")
grade_8.to_csv("marks_pca_grade_8.csv")
        
col_all = marks_all.columns
principalDf_all = pd.DataFrame()
subs_ex_ratios_all = []
for sub_year in range (int(len(col_all)/9)):
    col = col_all[sub_year*9].split(".")[0]
    marks_year_std = marks_all.iloc[:,sub_year*9:(sub_year*9)+9].copy()
    marks_year_std = StandardScaler().fit_transform(marks_year_std)
    pca = PCA(n_components=1)
    principalComponents = pca.fit_transform(marks_year_std)
    principalDf_all[col] = pd.DataFrame(data = principalComponents, columns = [col])
    subs_ex_ratios_all.append(pca.explained_variance_ratio_)

principalDf_all.to_csv("marks_pca.csv")
    
        


