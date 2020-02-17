#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:22:28 2018

@author: adeeshaj
"""

import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import os
import sys
from sklearn.preprocessing import Imputer

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

#subjects arrays mean by year(Grade 6)
Religon_6_mean = marks_all[['Religion','Religion.1','Religion.2']]
Sinhala_6_mean = marks_all[['Sinhala','Sinhala.1','Sinhala.2']]
English_6_mean = marks_all[['English','English.1','English.2']]
Maths_6_mean = marks_all[['Mathematics','Mathematics.1','Mathematics.2']]
Science_6_mean = marks_all[['Science','Science.1','Science.2']]
History_6_mean = marks_all[['History','History.1','History.2']]
CE_6_mean = marks_all[['Citizenship Education','Citizenship Education.1','Citizenship Education.2']]
Health_6_mean = marks_all[['Health','Health.1','Health.2']]
Tamil_6_mean = marks_all[['Tamil','Tamil.1','Tamil.2']]
Geography_6_mean = marks_all[['Geography','Geography.1','Geography.2']]
PTS_6_mean = marks_all[['PTS','PTS.1','PTS.2']]
Art_6_mean = marks_all[['Art','Art.1','Art.2']]

#subjects arrays mean by year(Grade 7)
Religon_7_mean = marks_all[['Religion.3','Religion.4','Religion.5']]
Sinhala_7_mean = marks_all[['Sinhala.3','Sinhala.4','Sinhala.5']]
English_7_mean = marks_all[['English.3','English.4','English.5']]
Maths_7_mean = marks_all[['Mathematics.3','Mathematics.4','Mathematics.5']]
Science_7_mean = marks_all[['Science.3','Science.4','Science.5']]
History_7_mean = marks_all[['History.3','History.4','History.5']]
CE_7_mean = marks_all[['Citizenship Education.3','Citizenship Education.4','Citizenship Education.5']]
Health_7_mean = marks_all[['Health.3','Health.4','Health.5']]
Tamil_7_mean = marks_all[['Tamil.3','Tamil.4','Tamil.5']]
Geography_7_mean = marks_all[['Geography.3','Geography.4','Geography.5']]
PTS_7_mean = marks_all[['PTS.3','PTS.4','PTS.5']]
Art_7_mean = marks_all[['Art.3','Art.4','Art.5']]

#subjects arrays mean by year(Grade 8)
Religon_8_mean = marks_all[['Religion.6','Religion.7','Religion.8']]
Sinhala_8_mean = marks_all[['Sinhala.6','Sinhala.7','Sinhala.8']]
English_8_mean =marks_all[['English.6','English.7','English.8']]
Maths_8_mean = marks_all[['Mathematics.6','Mathematics.7','Mathematics.8']]
Science_8_mean = marks_all[['Science.6','Science.7','Science.8']]
History_8_mean = marks_all[['History.6','History.7','History.8']]
CE_8_mean = marks_all[['Citizenship Education.6','Citizenship Education.7','Citizenship Education.8']]
Health_8_mean = marks_all[['Health.6','Health.7','Health.8']]
Tamil_8_mean = marks_all[['Tamil.6','Tamil.7','Tamil.8']]
Geography_8_mean = marks_all[['Geography.6','Geography.7','Geography.8']]
PTS_8_mean = marks_all[['PTS.6','PTS.7','PTS.8']]
Art_8_mean = marks_all[['Art.6','Art.7','Art.8']]

marks_mean_6 = pd.DataFrame()
marks_mean_7 = pd.DataFrame()
marks_mean_8 = pd.DataFrame()

marks_mean_6['Religion'] = Religon_6_mean.mean(axis=1)
marks_mean_6['First Language'] = Sinhala_6_mean.mean(axis=1)
marks_mean_6['English Language'] = English_6_mean.mean(axis=1)
marks_mean_6['Mathematics'] = Maths_6_mean.mean(axis=1)
marks_mean_6['Science'] = Science_6_mean.mean(axis=1)
marks_mean_6['History'] = History_6_mean.mean(axis=1)
marks_mean_6['Citizenship Education'] = CE_6_mean.mean(axis=1)
marks_mean_6['Health'] = Health_6_mean.mean(axis=1)
marks_mean_6['Second Language'] = Tamil_6_mean.mean(axis=1)
marks_mean_6['Geography'] = Geography_6_mean.mean(axis=1)
marks_mean_6['PTS'] = PTS_6_mean.mean(axis=1)
marks_mean_6['Art'] = Art_6_mean.mean(axis=1)


marks_mean_7['Religion'] = Religon_7_mean.mean(axis=1)
marks_mean_7['First Language'] = Sinhala_7_mean.mean(axis=1)
marks_mean_7['English Language'] = English_7_mean.mean(axis=1)
marks_mean_7['Mathematics'] = Maths_7_mean.mean(axis=1)
marks_mean_7['Science'] = Science_7_mean.mean(axis=1)
marks_mean_7['History'] = History_7_mean.mean(axis=1)
marks_mean_7['Citizenship Education'] = CE_7_mean.mean(axis=1)
marks_mean_7['Health'] = Health_7_mean.mean(axis=1)
marks_mean_7['Second Language'] = Tamil_7_mean.mean(axis=1)
marks_mean_7['Geography'] = Geography_7_mean.mean(axis=1)
marks_mean_7['PTS'] = PTS_7_mean.mean(axis=1)
marks_mean_7['Art'] = Art_7_mean.mean(axis=1)

marks_mean_8['Religion'] = Religon_8_mean.mean(axis=1)
marks_mean_8['First Language'] = Sinhala_8_mean.mean(axis=1)
marks_mean_8['English Language'] = English_8_mean.mean(axis=1)
marks_mean_8['Mathematics'] = Maths_8_mean.mean(axis=1)
marks_mean_8['Science'] = Science_8_mean.mean(axis=1)
marks_mean_8['History'] = History_8_mean.mean(axis=1)
marks_mean_8['Citizenship Education'] = CE_8_mean.mean(axis=1)
marks_mean_8['Health'] = Health_8_mean.mean(axis=1)
marks_mean_8['Second Language'] = Tamil_8_mean.mean(axis=1)
marks_mean_8['Geography'] = Geography_8_mean.mean(axis=1)
marks_mean_8['PTS'] = PTS_8_mean.mean(axis=1)
marks_mean_8['Art'] = Art_8_mean.mean(axis=1)

col_all = marks_all.columns
marks_mean = pd.DataFrame()
for i in range(int(len(col_all)/9)):
    sub = col_all[i*9].split(".")[0]
    if (sub[0:3] == "Eng"):
         marks_mean["English Language"] = marks_all[col_all[i*9:(i*9)+9]].mean(axis=1)
    elif (sub[0:3] == "Sin"):
         marks_mean["First Language"] = marks_all[col_all[i*9:(i*9)+9]].mean(axis=1)
    elif (sub[0:3] == "Tam"):
         marks_mean["Second Language"] = marks_all[col_all[i*9:(i*9)+9]].mean(axis=1)
    else:
        marks_mean[str(sub)] = marks_all[col_all[i*9:(i*9)+9]].mean(axis=1)


marks_mean_6.to_csv("marks_mean_grade_6.csv")
marks_mean_7.to_csv("marks_mean_grade_7.csv")
marks_mean_8.to_csv("marks_mean_grade_8.csv")

marks_mean.to_csv("marks_mean.csv")





