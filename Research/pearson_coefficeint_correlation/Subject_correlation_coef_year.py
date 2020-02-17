#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:52:46 2018

@author: adeesha
"""
import pandas as pd
import scipy.stats as stat
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def preprocessData():
    
    southland_data = pd.read_csv('/home/adeesha/Documents/Research/data/full data set.csv', header=1)
    sirisaman_data = pd.read_csv('/home/adeesha/Documents/Research/data/Sirisaman - Perfomance.csv',header=1)
    
    southland_data = southland_data.dropna(axis=1,how='all') 
    southland_data = southland_data.dropna(axis=0,how='all')
    sirisaman_data = sirisaman_data.dropna(axis=1,how='all')
    sirisaman_data = sirisaman_data.dropna(axis=0,how='all')
    
    southland_art_data = southland_data[[ 'Index No.','Art','Eastern Music','Western Music','Dancing','Drama']]
    southland_art_data1 = southland_data[[ 'Index No.','Art.1','Eastern Music.1','Western Music.1','Dancing.1','Drama.1']]
    
    
    southland_art_data['E. Art0'] = southland_art_data[southland_art_data.columns[1:]].apply(lambda x: ','.join(x.dropna().astype(int).astype(str)),axis=1)
    southland_art_data1['E. Art1'] = southland_art_data1[southland_art_data1.columns[1:]].apply(lambda x: ','.join(x.dropna().astype(int).astype(str)),axis=1)
        
    southland_art_data['E. Art0'] = pd.to_numeric(southland_art_data['E. Art0'])
    southland_art_data1['E. Art1'] = pd.to_numeric(southland_art_data1['E. Art1'])
    southland_sub_temp = pd.merge(southland_data,southland_art_data[['Index No.','E. Art0']],on='Index No.',how='outer')
    southland_sub = pd.merge(southland_sub_temp,southland_art_data1[['Index No.','E. Art1']],on='Index No.',how='outer')
    
    southland_sub = southland_sub.drop(['Art','Eastern Music','Western Music','Dancing','Drama','Art.1','Eastern Music.1','Western Music.1','Dancing.1','Drama.1'],axis=1)
    
    southland_sub = southland_sub.dropna()
    sirisaman_sub = sirisaman_data.dropna()
    
    all_data = pd.concat([southland_sub,sirisaman_sub],axis=0)
    
    all_data = all_data.drop(['0','0.1','0.2','0.3'],axis=1)
    
    all_data['Tamil.4'] = pd.to_numeric(all_data['Tamil.4'])
    
    return all_data
    
data = preprocessData()



all_subs = list(data.columns.values)
all_subs.remove("Index No.")
all_subs.remove("Name")
all_subs.remove("Sports")

data=data.drop_duplicates(['Name'],keep='first')

#subjects arrays mean by year(Grade 6)
Religon_6_mean = data[['Religon','Religon.1','Religon.2']]
Sinhala_6_mean = data[['Sinhala','Sinhala.1','Sinhala.2']]
English_6_mean = data[['English','English.1','English.2']]
Maths_6_mean = data[['Maths','Maths.1','Maths.2']]
Science_6_mean = data[['Science','Science.1','Science.2']]
History_6_mean = data[['History','History.1','History.2']]
CE_6_mean = data[['Citizenship Education','Citizenship Education.1','Citizenship Education.2']]
Health_6_mean = data[['Health','Health.1','Health.2']]
Tamil_6_mean = data[['Tamil','Tamil.1','Tamil.2']]
Geography_6_mean = data[['Geography','Geography.1','Geography.2']]
PTS_6_mean = data[['PTS','PTS.1','PTS.2']]
Art_6_mean = data[['E. Art0','E. Art1','E. Art']]

Religon_7_mean = data[['Religon.3','Religon.4','Religon.5']]
Sinhala_7_mean = data[['Sinhala.3','Sinhala.4','Sinhala.5']]
English_7_mean = data[['English.3','English.4','English.5']]
Maths_7_mean = data[['Maths.3','Maths.4','Maths.5']]
Science_7_mean = data[['Science.3','Science.4','Science.5']]
History_7_mean = data[['History.3','History.4','History.5']]
CE_7_mean = data[['Citizenship Education.3','Citizenship Education.4','Citizenship Education.5']]
Health_7_mean = data[['Health.3','Health.4','Health.5']]
Tamil_7_mean = data[['Tamil.3','Tamil.4','Tamil.5']]
Geography_7_mean = data[['Geography.3','Geography.4','Geography.5']]
PTS_7_mean = data[['PTS.3','PTS.4','PTS.5']]
Art_7_mean = data[['E. Art.1','E. Art.2','E. Art.3']]

Religon_8_mean = data[['Religon.6','Religon.7','Religon.8']]
Sinhala_8_mean = data[['Sinhala.6','Sinhala.7','Sinhala.8']]
English_8_mean = data[['English.6','English.7','English.8']]
Maths_8_mean = data[['Maths.6','Maths.7','Maths.8']]
Science_8_mean = data[['Science.6','Science.7','Science.8']]
History_8_mean = data[['History.6','History.7','History.8']]
CE_8_mean = data[['Citizenship Education.6','Citizenship Education.7','Citizenship Education.8']]
Health_8_mean = data[['Health.6','Health.7','Health.8']]
Tamil_8_mean = data[['Tamil.6','Tamil.7','Tamil.8']]
Geography_8_mean = data[['Geography.6','Geography.7','Geography.8']]
PTS_8_mean = data[['PTS.6','PTS.7','PTS.8']]
Art_8_mean = data[['E. Art.4','E. Art.5','E. Art.6']]

data['Religon_6_Mean'] = Religon_6_mean.mean(axis=1)
data['Sinhala_6_Mean'] = Sinhala_6_mean.mean(axis=1)
data['English_6_Mean'] = English_6_mean.mean(axis=1)
data['Maths_6_Mean'] = Maths_6_mean.mean(axis=1)
data['Science_6_Mean'] = Science_6_mean.mean(axis=1)
data['History_6_Mean'] = History_6_mean.mean(axis=1)
data['CE_6_Mean'] = CE_6_mean.mean(axis=1)
data['Health_6_Mean'] = Health_6_mean.mean(axis=1)
data['Tamil_6_Mean'] = Tamil_6_mean.mean(axis=1)
data['Geography_6_Mean'] = Geography_6_mean.mean(axis=1)
data['PTS_6_Mean'] = PTS_6_mean.mean(axis=1)
data['Art_6_Mean'] = Art_6_mean.mean(axis=1)

data['Religon_7_Mean'] = Religon_6_mean.mean(axis=1)
data['Sinhala_7_Mean'] = Sinhala_6_mean.mean(axis=1)
data['English_7_Mean'] = English_6_mean.mean(axis=1)
data['Maths_7_Mean'] = Maths_6_mean.mean(axis=1)
data['Science_7_Mean'] = Science_6_mean.mean(axis=1)
data['History_7_Mean'] = History_6_mean.mean(axis=1)
data['CE_7_Mean'] = CE_6_mean.mean(axis=1)
data['Health_7_Mean'] = Health_6_mean.mean(axis=1)
data['Tamil_7_Mean'] = Tamil_6_mean.mean(axis=1)
data['Geography_7_Mean'] = Geography_6_mean.mean(axis=1)
data['PTS_7_Mean'] = PTS_6_mean.mean(axis=1)
data['Art_7_Mean'] = Art_6_mean.mean(axis=1)

data['Religon_7_Mean'] = Religon_7_mean.mean(axis=1)
data['Sinhala_7_Mean'] = Sinhala_7_mean.mean(axis=1)
data['English_7_Mean'] = English_7_mean.mean(axis=1)
data['Maths_7_Mean'] = Maths_7_mean.mean(axis=1)
data['Science_7_Mean'] = Science_7_mean.mean(axis=1)
data['History_7_Mean'] = History_7_mean.mean(axis=1)
data['CE_7_Mean'] = CE_7_mean.mean(axis=1)
data['Health_7_Mean'] = Health_7_mean.mean(axis=1)
data['Tamil_7_Mean'] = Tamil_7_mean.mean(axis=1)
data['Geography_7_Mean'] = Geography_7_mean.mean(axis=1)
data['PTS_7_Mean'] = PTS_7_mean.mean(axis=1)
data['Art_7_Mean'] = Art_7_mean.mean(axis=1)

data['Religon_8_Mean'] = Religon_8_mean.mean(axis=1)
data['Sinhala_8_Mean'] = Sinhala_8_mean.mean(axis=1)
data['English_8_Mean'] = English_8_mean.mean(axis=1)
data['Maths_8_Mean'] = Maths_8_mean.mean(axis=1)
data['Science_8_Mean'] = Science_8_mean.mean(axis=1)
data['History_8_Mean'] = History_8_mean.mean(axis=1)
data['CE_8_Mean'] = CE_8_mean.mean(axis=1)
data['Health_8_Mean'] = Health_8_mean.mean(axis=1)
data['Tamil_8_Mean'] = Tamil_8_mean.mean(axis=1)
data['Geography_8_Mean'] = Geography_8_mean.mean(axis=1)
data['PTS_8_Mean'] = PTS_8_mean.mean(axis=1)
data['Art_8_Mean'] = Art_8_mean.mean(axis=1)

sub_means_grades= [['Religon_6_Mean','Sinhala_6_Mean','English_6_Mean','Maths_6_Mean','Science_6_Mean','History_6_Mean','CE_6_Mean','Health_6_Mean','Tamil_6_Mean','Geography_6_Mean','PTS_6_Mean','Art_6_Mean'],
            ['Religon_7_Mean','Sinhala_7_Mean','English_7_Mean','Maths_7_Mean','Science_7_Mean','History_7_Mean','CE_7_Mean','Health_7_Mean','Tamil_7_Mean','Geography_7_Mean','PTS_7_Mean','Art_7_Mean'],
            ['Religon_8_Mean','Sinhala_8_Mean','English_8_Mean','Maths_8_Mean','Science_8_Mean','History_8_Mean','CE_8_Mean','Health_8_Mean','Tamil_8_Mean','Geography_8_Mean','PTS_8_Mean','Art_8_Mean']]

Grades = ['Grade 6','Grade 7','Grade 8']
for sub_means in sub_means_grades:
    r_values = []
    for sub_x in sub_means:
        r_sub = []
        for sub_y in sub_means:
            r = stat.pearsonr(data[[sub_x]],data[[sub_y]])
            r_sub.append(r[0])
        r_values.append(r_sub)
    
    feature_cols = ['Rel','Sin','Eng','Math','Sci','His','CE','Hel','Tam','Geo','PTS','Art']
    colors = iter(cm.rainbow(np.linspace(0, 1, len(feature_cols))))
    
    
    
    plt.figure(figsize=(12,9))
    for fea in feature_cols:
        c = next(colors)
        plt.scatter(feature_cols,r_values[feature_cols.index(fea)],color=c,label=fea)
    plt.title(Grades[sub_means_grades.index(sub_means)])
    plt.xlabel('Subjects')
    plt.ylabel('pearson r')
    plt.axis([-1,15,0.4,1])
    
    plt.legend()
    plt.grid(True)
    plt.savefig(Grades[sub_means_grades.index(sub_means)]+"pearson coefficient correlation.pdf",format='pdf')
    plt.show()




