#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:50:16 2018

@author: adeesha
"""
import pandas as pd
import scipy.stats as stat

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

data=data.drop_duplicates()

all_subs = list(data.columns.values)
all_subs.remove("Index No.")
all_subs.remove("Name")
all_subs.remove("Sports")




#find pearson correlation coefficient for all subjects combinations
sub_combinations = []
r_values = []
count = 0
for sub in all_subs:
    sub_comb_one = []
    r_values_one = []
    
    count +=1
    y_subs = []
    for temp_sub in all_subs:
        if(temp_sub != sub):
            y_subs.append(temp_sub)
    sub_x = sub
    for sub_y in y_subs:
        r = stat.pearsonr(data[[sub_x]],data[[sub_y]])
        sub_comb_one.append([sub_x,sub_y])
        r_values_one.append(r[0])
        if(r[0]>0.8):
            print (str([sub_x,sub_y])+"    "+str(r[0]))
    r_values.append(max(r_values_one))
    sub_combinations.append(sub_comb_one[r_values_one.index(max(r_values_one))])
    #print (str(count)+"   "+str(sub_comb_one[r_values_one.index(max(r_values_one))])+"     "+str(max(r_values_one)))

print("******************************")
print ("Final   "+str(sub_combinations[r_values.index(max(r_values))])+"     "+str(max(r_values)))

